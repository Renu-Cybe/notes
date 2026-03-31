# 文档处理技能索引

## 已安装技能

| 技能 | 描述 | 触发条件 |
|------|------|----------|
| **[docx](docx/SKILL.md)** | Word 文档处理 | 提及 `.docx`、Word 文档、报告、备忘录 |
| **[xlsx](xlsx/SKILL.md)** | Excel 电子表格 | 提及 `.xlsx`、`.csv`、电子表格、财务模型 |
| **[pdf](pdf/SKILL.md)** | PDF 文件处理 | 提及 `.pdf`、合并、分割、提取文本 |
| **[pptx](pptx/SKILL.md)** | PowerPoint 演示文稿 | 提及 `.pptx`、幻灯片、演示文稿、deck |

---

## 使用方式

这些技能会在您提及相应文件类型时**自动触发**。

### 示例触发语句

- "帮我读取这个 Word 文档..." → 触发 **docx** 技能
- "分析这个 Excel 文件的数据" → 触发 **xlsx** 技能
- "合并这些 PDF 文件" → 触发 **pdf** 技能
- "创建一份演示文稿" → 触发 **pptx** 技能

---

## 依赖安装

### Python 依赖

```bash
pip install pypdf pdfplumber reportlab pytesseract pdf2image
pip install openpyxl pandas
pip install python-pptx markitdown
pip install docx
```

### 系统工具

**Windows (Chocolatey):**
```bash
choco install libreoffice poppler
```

**macOS (Homebrew):**
```bash
brew install --cask libreoffice poppler
```

---

## 技能位置

所有技能文件位于：`F:\Obsidian\skills\`

每个技能包含：
- `SKILL.md` - 技能指南和触发器
- `scripts/` - 工具脚本
- `LICENSE.txt` - 使用条款
