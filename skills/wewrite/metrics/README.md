# wewrite 度量数据

## 目录结构

```
metrics/
├── metrics-definition.yaml    # 指标定义
├── collector.py               # 数据收集器
├── reporter.py                # 报告生成器
├── INTEGRATION.md             # 集成指南
├── data/                      # 原始数据（jsonl）
│   ├── 2026-03-31.jsonl
│   └── ...
└── reports/                   # 生成报告（json）
    ├── weekly_2026-W13.json
    └── monthly_2026-03.json
```

## 使用方法

### 1. 数据收集

由 SKILL.md 执行流程自动调用，无需手动操作。

### 2. 生成报告

```bash
# 周报告
python3 metrics/reporter.py

# 月度报告
python3 metrics/reporter.py monthly
```

### 3. 指标定义

详见 `metrics-definition.yaml`

| 维度 | 指标 | 说明 |
|------|------|------|
| 效率 | total_duration_min | 总耗时（分钟）|
| 效率 | step_durations | 各步骤细分耗时 |
| 质量 | word_count | 文章字数 |
| 质量 | pass_on_first_try | 是否一次通过 |
| 质量 | modification_rounds | 修改轮次 |
| 结果 | published | 是否成功发布 |
| 结果 | media_id | 微信 media_id |

## 首次使用

数据目录会自动创建，无需初始化。

执行一次 wewrite 后，运行 `python3 metrics/reporter.py` 查看报告。
