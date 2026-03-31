---
name: gui_skills_mcp_cli_sync
description: 所有新安装的 Skills、MCP 服务器、CLI 工具必须同步到 CodePilot GUI 全局配置目录
type: feedback
reason: 发现 GUI 端不读取项目级配置，只读取全局配置，如果不同步会导致 GUI 端无法使用已安装的工具和技能
created_at: 2026-03-15
updated_at: 2026-03-15
last_accessed: 2026-03-30
---

# GUI 端配置同步规则

## 规则
所有新安装的 **Skills**、**MCP 服务器**、**CLI 工具** 必须同步配置到 CodePilot GUI 的全局目录。

## Why
CodePilot GUI 不读取项目级配置（`F:\Obsidian\.claude\`），只读取全局用户目录配置（`~/.claude/`）。如果不配置到全局目录，GUI 端无法显示和使用这些扩展。

## How to apply

### 1. Skills 安装路径
```
源位置：F:\Obsidian\skills\{name}\
目标位置：~/.claude/skills/{name}/
```
复制整个技能目录（包含 `SKILL.md`、`scripts/`、`LICENSE.txt`、`references/`）

**已安装 Skills**: docx, xlsx, pdf, pptx, web-access, skill-creator, **pua**

### 2. MCP 服务器配置位置
```
配置文件：~/.claude/mcp.json
```
添加 MCP server 配置：
```json
{
  "mcpServers": {
    "{name}": {
      "type": "stdio",
      "command": "node",
      "args": ["{absolute_path}"]
    }
  }
}
```

### 3. CLI 工具注册
CLI 工具安装后，需要在 GUI 中刷新工具列表以自动检测。

### 4. 验证步骤
- Skills: 在 GUI 技能列表中可见
- MCP: 在 GUI MCP 面板中可见
- CLI: 可通过 GUI 终端调用

## 关键路径对照

| 类型 | 项目路径 | 全局路径 | 示例 |
|------|---------|---------|------|
| Skills | `F:\Obsidian\skills\` | `~/.claude/skills/` | docx, xlsx, pdf, pptx, web-access, skill-creator, **pua** |
| MCP 配置 | `F:\Obsidian\.claude\mcp.json` | `~/.claude\mcp.json` | opencli, cdp-proxy, chrome-devtools |
| CLI 工具 | `F:\Obsidian\memory\cli-tools\` | 系统 PATH | opencli, bird |

## 注意事项
- Windows 路径使用 `~` 代表 `%USERPROFILE%`
- 复制技能目录时需包含所有子文件
- MCP 配置中的路径必须使用绝对路径
- GUI 端配置修改后可能需要重启应用生效
