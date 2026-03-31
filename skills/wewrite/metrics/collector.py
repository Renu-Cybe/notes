#!/usr/bin/env python3
"""
wewrite 度量数据收集器
每次执行工作流时自动记录数据
"""
import json
import uuid
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional

METRICS_DIR = Path(__file__).parent
DATA_DIR = METRICS_DIR / "data"

class MetricsCollector:
    def __init__(self):
        DATA_DIR.mkdir(exist_ok=True)
        self.execution_id = str(uuid.uuid4())[:8]
        self.start_time = datetime.now()
        self.data = {
            "execution_id": self.execution_id,
            "timestamp": self.start_time.isoformat(),
            "date": self.start_time.strftime("%Y-%m-%d"),
            "week": self.start_time.strftime("%Y-W%W"),
            "month": self.start_time.strftime("%Y-%m"),
            "step_durations": {},
            "post_publish_metrics": {}
        }
        self.step_start_times = {}

    def record(self, field: str, value: Any):
        """记录单个字段"""
        self.data[field] = value

    def step_start(self, step_name: str):
        """开始记录步骤耗时"""
        self.step_start_times[step_name] = datetime.now()

    def step_end(self, step_name: str):
        """结束记录步骤耗时"""
        if step_name in self.step_start_times:
            duration = (datetime.now() - self.step_start_times[step_name]).total_seconds() / 60
            self.data["step_durations"][step_name] = round(duration, 2)

    def finalize(self):
        """完成数据收集，计算总耗时"""
        total_duration = (datetime.now() - self.start_time).total_seconds() / 60
        self.data["total_duration_min"] = round(total_duration, 2)

        # 保存到文件
        date_str = self.start_time.strftime("%Y-%m-%d")
        daily_file = DATA_DIR / f"{date_str}.jsonl"

        with open(daily_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(self.data, ensure_ascii=False) + "\n")

        return self.execution_id

    def record_post_publish(self, execution_id: str, metrics: Dict[str, Any]):
        """记录发布后数据（需要execution_id关联）"""
        # 找到对应记录并更新
        date_str = self.start_time.strftime("%Y-%m-%d")
        daily_file = DATA_DIR / f"{date_str}.jsonl"

        if not daily_file.exists():
            return

        lines = []
        updated = False
        with open(daily_file, "r", encoding="utf-8") as f:
            for line in f:
                record = json.loads(line.strip())
                if record.get("execution_id") == execution_id:
                    record["post_publish_metrics"] = metrics
                    record["post_publish_metrics"]["collected_at"] = datetime.now().isoformat()
                    updated = True
                lines.append(record)

        if updated:
            with open(daily_file, "w", encoding="utf-8") as f:
                for record in lines:
                    f.write(json.dumps(record, ensure_ascii=False) + "\n")

# 全局收集器实例
collector: Optional[MetricsCollector] = None

def start_collection() -> MetricsCollector:
    """开始新的度量收集"""
    global collector
    collector = MetricsCollector()
    return collector

def get_collector() -> Optional[MetricsCollector]:
    """获取当前收集器"""
    return collector
