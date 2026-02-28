# 百科词条 Lint 规范 v0.1

适用范围：`lifecosmos-wiki-pages` 静态词条仓库（Markdown）
目标：只做扫描报告，不改文件。

## 1. 目录与文件结构

- 词条目录应满足：
  - `zh/<slug>/index.md`
  - `zh/<slug>/friendly.md`
  - `zh/<slug>/academic.md`
  - `zh/<slug>/internal.md`
  - `en/<slug>/index.md`
  - `en/<slug>/friendly.md`
  - `en/<slug>/academic.md`
  - `en/<slug>/internal.md`
- `slug` 规范：小写字母/数字/连字符 `-`，不允许下划线。

## 2. 链接规范

- 禁止 WikiLink：`[[...]]`
- 推荐内部链接：
  - 中文文档：`/zh/<slug>`
  - 英文文档：`/en/<slug>`
- 不做跨语言链（中文链中文，英文链英文）。

## 3. 标签与分类规范

- 标签区禁止 `#标签` 形式（会触发标题样式）。
- 标签区应使用：
  - 中文：
    - `## 体系归属`
    - `主题：...`
    - `类型：...`
    - `方向：...`
  - 英文：
    - `## Classification`
    - `Theme: ...`
    - `Type: ...`
    - `Direction: ...`

## 4. 元数据规范

- 顶部必须包含 HTML 注释元数据（非 YAML front matter）：
  - 例如：`<!-- id: LC-0001 theme: ... type: ... direction: ... lang: zh -->`
- 禁止使用 `---` front matter。

## 5. 标题层级规范

- 允许：`#`、`##`、`###`
- 警告：出现 `####` 及更深层级。

## 6. 术语与命名规范（基础检查）

- 英文命名规则（AI禅院草）：`<Pinyin>zhou Celestial`
- 检查关键拼写异常文件名：例如 `fridenly.md`（应为 `friendly.md`）

## 7. 报告等级

- ERROR：会导致结构/渲染/导航失效的项
- WARN：可能导致风格不统一或后续维护风险
- INFO：建议优化项
