# 技能库 MOC

> 当前技能: **5 个** | 最后更新: 2026-03-31

---

## 技能分类

### 🏢 软件开发双核

| 技能 | 角色 | 定位 | 核心能力 |
|------|------|------|----------|
| **[[gstack]]** | CEO | 产品战略 | YC方法论、虚拟团队、知识复利 |
| **[[superpowers]]** | CTO | 技术执行 | TDD、代码审查、高能动性、设计标准 |

**使用方式**:
- 定方向 → **CEO (gstack)**: /office-hours, /plan-ceo-review, /compound
- 定质量 → **CTO (superpowers)**: /plan-eng-review, TDD, /review, 设计审查
- 完整体系 → CEO → CTO 串联使用

---

### 📝 内容生产

| 技能 | 用途 | 核心流程 |
|------|------|----------|
| **[[wewrite]]** | 公众号文章 | 热点抓取 → 选题 → 框架 → 写作 → SEO → 视觉 → 排版 → 推送 |
| **[[follow-builders]]** | AI行业监测 | X/Twitter + YouTube播客 → 摘要 → 素材库 |

---

## 技能触发速查

| 你想... | 说... | 激活技能 |
|---------|-------|----------|
| **开发功能** | "build this" / "开发功能" / "写代码" | gstack + superpowers |
| **修复Bug** | "fix this bug" / "修复" / "debug" | superpowers (TDD + 系统化调试) |
| **产品规划** | "I want to build" / "brainstorm" / "计划" | gstack (/office-hours, /plan-ceo-review) |
| **代码审查** | "review my code" / "审查" / "检查" | superpowers (/review + 设计标准) |
| **发布部署** | "ship it" / "deploy" / "发布" | gstack (/ship, /land-and-deploy) |
| **安全审计** | "security check" / "安全" | gstack (/cso) |
| **问题复盘** | "problem solved" / "that worked" | gstack (/compound) 知识复利 |
| **前端设计** | "design this" / "前端" / "UI" | superpowers (设计审查标准) |
| **公众号文章** | "写公众号" / "推文" / "选题" | wewrite (8步全自动) |
| **AI行业监测** | "follow builders" / "AI动态" | follow-builders |

---

## CEO (gstack) 完整能力

源自 Garry Tan (YC CEO) 的 gstack，整合 Compound Engineering 的知识复利。

| 命令 | 虚拟角色 | 功能 |
|------|---------|------|
| `/office-hours` | YC Partner | 6个强制问题重新定义产品 |
| `/plan-ceo-review` | CEO | 10星产品挖掘 |
| `/plan-eng-review` | Eng Manager | 架构锁定、数据流、边界情况 |
| `/plan-design-review` | Senior Designer | 设计审核，AI slop检测 |
| `/review` | Staff Engineer | 代码审查 |
| `/qa` | QA Lead | 浏览器测试 |
| `/ship` | Release Engineer | 发布工作流 |
| `/cso` | Security Officer | OWASP + STRIDE 安全审计 |
| `/canary` | SRE | 生产监控 |
| `/retro` | - | 每周复盘 |
| `/compound` | Knowledge Lead | **知识复利** — 文档化解决方案 |

### 知识复利 (/compound)

**Why compound?** 第一次解决"N+1 query"需要30分钟研究，文档化后下次只需2分钟查找。

**触发词**: "that worked" / "it's fixed" / "problem solved"

---

## CTO (superpowers) 完整能力

源自 Jesse Vincent 的 superpowers，整合 frontend-design 和 pua 的高能动性。

| 模块 | 功能 |
|------|------|
| **brainstorming** | 头脑风暴与规格定义 |
| **writing-plans** | 编写详细实施计划（2-5分钟/任务）|
| **subagent-driven-development** | 子代理驱动开发 |
| **test-driven-development** | TDD 铁律（Red-Green-Refactor）|
| **systematic-debugging** | 4阶段根因分析 |
| **high-agency-execution** | 高能动性执行（三条红线）|
| **design-review-standards** | 前端设计审查（反AI-slop）|
| **code-review** | 两阶段代码审查 |
| **git-worktrees** | 隔离开发 |

### 高能动性三条红线

🚫 **红线一：闭环意识** — 声称"已完成"前必须跑验证命令、贴出证据。

🚫 **红线二：事实驱动** — 说"可能是环境问题"前，你用工具验证了吗？

🚫 **红线三：穷尽一切** — 说"无法解决"前，5步方法论走完了吗？

### 设计审查标准

| 维度 | 标准 | 反例 |
|------|------|------|
| **字体** | 独特、有特色，避免 Arial/Inter | ❌ 通用系统字体 |
| **色彩** | 大胆方案，避免紫色渐变 cliché | ❌ 紫色渐变 + 白底 |
| **动效** | CSS 动画、页面加载编排 | ❌ 无动画或过度动画 |
| **布局** | 非对称、打破网格、对角线流动 | ❌ 标准网格布局 |
| **背景** | 渐变网格、噪点纹理、几何图案 | ❌ 纯色背景 |

---

## 技能整合说明

**已整合并删除的技能** (亮点已合并到 CEO/CTO):

| 原技能 | 整合位置 | 保留能力 |
|--------|---------|----------|
| compound-engineering | gstack | /compound 知识复利系统 |
| frontend-design | superpowers | 设计审查标准、反AI-slop |
| pua | superpowers | 高能动性执行、三条红线 |
| docx/xlsx/pdf/pptx | 工具集 | 作为基础工具能力 |
| ljg-roundtable | 删除 | 可手动模拟多视角讨论 |

---

## 目录结构

```
skills/
├── gstack/
│   └── SKILL.md              # CEO - 产品战略 + 知识复利
├── superpowers/
│   └── SKILL.md              # CTO - 技术执行 + 设计标准 + 高能动性
├── wewrite/
│   ├── SKILL.md              # 公众号全流程
│   └── ...
├── follow-builders/
│   ├── SKILL.md              # AI监测
│   └── ...
├── MOC-技能库.md             # 本文件
└── INDEX.md                  # 文档处理技能索引（保留）
```

---

## 更新日志

| 日期 | 变更 |
|------|------|
| 2026-03-31 | **整合优化**: 合并 compound-engineering, frontend-design, pua 到 CEO/CTO; 删除冗余技能; 精简至5个核心技能 |
| 2026-03-31 | 新增: gstack (CEO), superpowers (CTO), compound-engineering, frontend-design, pua |
| 2026-03-30 | 新增: wewrite, follow-builders, docx, xlsx, pdf, pptx, ljg-roundtable |
