# 度量系统集成指南

## 快速开始

在主管道 Step 1 开始处添加：

```python
from metrics.collector import start_collection, get_collector

# 开始收集
collector = start_collection()
collector.record("trigger_type", "manual")  # 或 "auto", "scheduled"
collector.record("user_query", user_input)
```

在各步骤边界添加计时：

```python
# Step 2 开始
collector.step_start("topic_selection")

# Step 2 结束
collector.step_end("topic_selection")
```

在 Step 8 完成时：

```python
# 记录结果
collector.record("word_count", word_count)
collector.record("published", True)
collector.record("pass_on_first_try", True)
collector.record("output_file", output_path)

# 保存数据
execution_id = collector.finalize()
```

## 收集的指标

### 自动收集
- execution_id, timestamp, date, week, month
- total_duration_min（自动计算）
- step_durations（各步骤耗时）

### 需要手动记录
- trigger_type: manual | auto | scheduled
- user_query: 用户原始指令
- topic_source: user_specified | hot_topics | builder_linkage
- word_count: 文章字数
- modification_rounds: 修改轮次
- pass_on_first_try: 是否一次通过
- published: 是否成功发布
- media_id: 微信 media_id
- error_message: 错误信息（如果失败）

## 查看报告

```bash
# 周报告（默认本周）
python3 metrics/reporter.py

# 指定周
python3 metrics/reporter.py 2026-W13

# 月度报告
python3 metrics/reporter.py monthly

# 指定月
python3 metrics/reporter.py monthly 2026-03
```

## 数据位置

- 原始数据：`metrics/data/YYYY-MM-DD.jsonl`
- 报告文件：`metrics/reports/weekly_YYYY-WWW.json`
- 报告文件：`metrics/reports/monthly_YYYY-MM.json`

## 示例数据

```json
{
  "execution_id": "a1b2c3d4",
  "timestamp": "2026-03-31T15:30:00",
  "date": "2026-03-31",
  "week": "2026-W13",
  "month": "2026-03",
  "trigger_type": "manual",
  "user_query": "写公众号",
  "topic_source": "user_specified",
  "total_duration_min": 25.5,
  "step_durations": {
    "topic_selection": 2.1,
    "outline_generation": 3.5,
    "content_writing": 15.2,
    "seo_optimization": 2.0,
    "image_generation": 1.2,
    "conversion": 0.8,
    "publishing": 0.7
  },
  "word_count": 1580,
  "modification_rounds": 0,
  "pass_on_first_try": true,
  "published": true,
  "output_file": "output/2026-03-31-xxx.md",
  "media_id": "xxx"
}
```

## 注意事项

1. **不要在失败时调用 finalize()** — 失败时应记录 error_message 再 finalize
2. **step_start/step_end 必须成对** — 否则该步骤耗时为0
3. **post_publish_metrics 可延后补充** — 使用 record_post_publish() 方法
