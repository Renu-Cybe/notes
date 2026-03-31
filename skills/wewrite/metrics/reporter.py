#!/usr/bin/env python3
"""
wewrite 度量报告生成器
生成周/月度报告
"""
import json
from datetime import datetime, timedelta
from pathlib import Path
from collections import defaultdict
import statistics

METRICS_DIR = Path(__file__).parent
DATA_DIR = METRICS_DIR / "data"
OUTPUT_DIR = METRICS_DIR / "reports"
OUTPUT_DIR.mkdir(exist_ok=True)

class MetricsReporter:
    def __init__(self):
        self.data = []
        self._load_data()

    def _load_data(self, days: int = 30):
        """加载最近N天的数据"""
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)

        for file_path in DATA_DIR.glob("*.jsonl"):
            try:
                file_date = datetime.strptime(file_path.stem, "%Y-%m-%d")
                if start_date <= file_date <= end_date:
                    with open(file_path, "r", encoding="utf-8") as f:
                        for line in f:
                            if line.strip():
                                self.data.append(json.loads(line))
            except ValueError:
                continue

    def weekly_report(self, week_str: str = None) -> dict:
        """生成周报告"""
        if week_str is None:
            week_str = datetime.now().strftime("%Y-W%W")

        week_data = [d for d in self.data if d.get("week") == week_str]

        if not week_data:
            return {"error": f"No data for week {week_str}"}

        # 计算指标
        total = len(week_data)
        successful = sum(1 for d in week_data if d.get("published", False))
        durations = [d.get("total_duration_min", 0) for d in week_data]
        word_counts = [d.get("word_count", 0) for d in week_data if d.get("word_count")]
        first_pass = sum(1 for d in week_data if d.get("pass_on_first_try", False))

        report = {
            "week": week_str,
            "generated_at": datetime.now().isoformat(),
            "executions_count": total,
            "success_rate": round(successful / total * 100, 1) if total > 0 else 0,
            "avg_duration_min": round(statistics.mean(durations), 1) if durations else 0,
            "avg_word_count": round(statistics.mean(word_counts), 0) if word_counts else 0,
            "first_pass_rate": round(first_pass / total * 100, 1) if total > 0 else 0,
            "total_word_output": sum(word_counts),
            "details": week_data
        }

        return report

    def monthly_report(self, month_str: str = None) -> dict:
        """生成月度报告"""
        if month_str is None:
            month_str = datetime.now().strftime("%Y-%m")

        month_data = [d for d in self.data if d.get("month") == month_str]

        if not month_data:
            return {"error": f"No data for month {month_str}"}

        # 基本指标
        total = len(month_data)
        successful = sum(1 for d in month_data if d.get("published", False))
        durations = [d.get("total_duration_min", 0) for d in month_data]
        word_counts = [d.get("word_count", 0) for d in month_data if d.get("word_count")]
        first_pass = sum(1 for d in month_data if d.get("pass_on_first_try", False))

        # 选题来源分布
        topic_sources = defaultdict(int)
        for d in month_data:
            source = d.get("topic_source", "unknown")
            topic_sources[source] += 1

        # 错误类型分布
        error_types = defaultdict(int)
        for d in month_data:
            if d.get("error_message"):
                # 简单分类
                error_msg = d["error_message"].lower()
                if "network" in error_msg or "connection" in error_msg:
                    error_types["network"] += 1
                elif "api" in error_msg:
                    error_types["api_error"] += 1
                elif "timeout" in error_msg:
                    error_types["timeout"] += 1
                else:
                    error_types["other"] += 1

        report = {
            "month": month_str,
            "generated_at": datetime.now().isoformat(),
            "executions_count": total,
            "success_rate": round(successful / total * 100, 1) if total > 0 else 0,
            "avg_duration_min": round(statistics.mean(durations), 1) if durations else 0,
            "avg_word_count": round(statistics.mean(word_counts), 0) if word_counts else 0,
            "first_pass_rate": round(first_pass / total * 100, 1) if total > 0 else 0,
            "total_word_output": sum(word_counts),
            "topic_source_distribution": dict(topic_sources),
            "error_type_distribution": dict(error_types),
            "weekly_breakdown": self._weekly_breakdown(month_data)
        }

        return report

    def _weekly_breakdown(self, month_data: list) -> dict:
        """按周分解月度数据"""
        by_week = defaultdict(list)
        for d in month_data:
            by_week[d.get("week", "unknown")].append(d)

        breakdown = {}
        for week, data in sorted(by_week.items()):
            breakdown[week] = {
                "count": len(data),
                "avg_duration": round(statistics.mean([d.get("total_duration_min", 0) for d in data]), 1)
            }
        return breakdown

    def save_report(self, report: dict, filename: str):
        """保存报告到文件"""
        filepath = OUTPUT_DIR / filename
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        return filepath

    def print_summary(self, report: dict):
        """打印报告摘要"""
        print("=" * 50)
        if "week" in report:
            print(f"📊 wewrite 周报告: {report['week']}")
        else:
            print(f"📊 wewrite 月度报告: {report['month']}")
        print("=" * 50)
        print(f"执行次数: {report['executions_count']}")
        print(f"成功率: {report['success_rate']}%")
        print(f"平均耗时: {report['avg_duration_min']} 分钟")
        print(f"平均字数: {report['avg_word_count']} 字")
        print(f"一次通过率: {report['first_pass_rate']}%")
        print(f"总输出字数: {report['total_word_output']} 字")

        if "topic_source_distribution" in report:
            print("\n选题来源分布:")
            for source, count in report['topic_source_distribution'].items():
                print(f"  - {source}: {count}")

        if "error_type_distribution" in report and report['error_type_distribution']:
            print("\n错误类型分布:")
            for error_type, count in report['error_type_distribution'].items():
                print(f"  - {error_type}: {count}")

        print("=" * 50)

if __name__ == "__main__":
    import sys

    reporter = MetricsReporter()

    if len(sys.argv) > 1 and sys.argv[1] == "monthly":
        # 月度报告
        month_str = sys.argv[2] if len(sys.argv) > 2 else None
        report = reporter.monthly_report(month_str)
        if "error" not in report:
            filename = f"monthly_{report['month']}.json"
            reporter.save_report(report, filename)
            reporter.print_summary(report)
            print(f"\n报告已保存: metrics/reports/{filename}")
    else:
        # 周报告（默认）
        week_str = sys.argv[1] if len(sys.argv) > 1 else None
        report = reporter.weekly_report(week_str)
        if "error" not in report:
            filename = f"weekly_{report['week']}.json"
            reporter.save_report(report, filename)
            reporter.print_summary(report)
            print(f"\n报告已保存: metrics/reports/{filename}")
        else:
            print(report["error"])
