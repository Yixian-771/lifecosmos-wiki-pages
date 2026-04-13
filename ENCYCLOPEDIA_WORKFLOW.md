# 禅院百科词条编写流程与标准 v2.0

> 本文档是实际操作标准，以此为准，忽略旧版文档。

---

## 一、词条文件结构

每个词条共 8 个文件，中英各 4 个，路径完全对称：

```
zh/[slug]/index.md        ← 中文入口页
zh/[slug]/internal.md     ← 中文内部版
zh/[slug]/academic.md     ← 中文学术版
zh/[slug]/friendly.md     ← 中文友好版

en/[slug]/index.md        ← 英文入口页
en/[slug]/internal.md     ← 英文内部版
en/[slug]/academic.md     ← 英文学术版
en/[slug]/friendly.md     ← 英文友好版
```

**slug 以英文为准**，中英文路径使用同一个 slug。

---

## 二、Slug 命名规则

- 全小写，连字符分隔（kebab-case）
- 以英文含义为准，不用拼音
- 参考 `translation-glossary.csv` 和已有词条命名风格
- 示例：归零 → `return-to-zero`，反常思维 → `abnormal-thinking`

---

## 三、各版本内容标准

### index.md（入口页）
```yaml
---
title: [中文词条名]
slug: [slug]
---
```
- 一句话定义（精炼，直接引用或改写导游原文）
- 版本导航表（友好版 / 学术版 / 内部版）
- 相关词条链接（横排，用 `·` 分隔）

### internal.md（内部版）
- 文件头注释：`<!-- id: LC-[缩写]-0001 theme: ... type: 内部版 direction: ... lang: zh -->`
- 严格以母版为准，原文一字不改
- 仅做清晰分章分节（加标题层级、列表化）
- 所有引用标注出处（文集篇目 + 条目编号）
- 文末加相关词条链接

### academic.md（学术版）
- 文件头注释：`<!-- id: LC-[缩写]-0003 ... type: 学术版 ... -->`
- 有摘要
- 有文本来源表格
- 系统分析概念定位、定义层次、与其他概念关系
- 可与外部概念（佛学、哲学等）比较，但以导游原文为基础
- 学术语气，术语精确

### friendly.md（友好版）
- 文件头注释：`<!-- id: LC-[缩写]-0002 ... type: 友好版 ... -->`
- 面向首次接触者
- 用生活类比和叙事引入
- 保留关键原文引用，但加导读上下文
- 可读性强，不浅薄

---

## 四、内链格式

**统一使用绝对路径，带尾斜线：**

```markdown
[上帝](/zh/greatest-creator/)
[The Greatest Creator](/en/greatest-creator/)
```

- 即使目标词条尚未创建，也可先写好内链（将来做了自动生效）
- 禁止使用相对路径跨词条链接（同一词条内的版本跳转除外，用 `friendly/` 等相对路径）
- 禁止中文页面链接到 `/en/` 路径，英文页面链接到 `/zh/` 路径

---

## 五、执行顺序

```
1. 读母版（词条母版/*.txt）
2. 确认 slug（查 translation-glossary.csv 或参照已有词条）
3. 写中文四版（index → internal → academic → friendly）
4. 更新 mkdocs.zh.yml（在 nav 中加一行）
5. 更新 zh/catalog/index.md（加入对应分类）
6. git commit + push
7. 给用户中文入口链接，等待确认
8. 写英文四版（index → internal → academic → friendly）
9. 更新 mkdocs.en.yml
10. 更新 en/catalog/index.md
11. git commit + push
12. 给用户英文入口链接
13. 将母版文件移入 词条母版/已做词条/
```

---

## 六、mkdocs 导航更新

在 `mkdocs.zh.yml` 和 `mkdocs.en.yml` 的 `nav:` 下各加一行：

```yaml
# zh
  - 归零: return-to-zero/index.md

# en
  - Return to Zero: return-to-zero/index.md
```

---

## 七、目录更新（catalog）

`zh/catalog/index.md` 和 `en/catalog/index.md` 按分类加入词条链接。

**分类结构（中文）：**
1. 上帝与道
2. 宇宙时空
3. 生命奥秘
4. 思维奥秘
5. 社会系统
6. 修行修炼

英文对应同结构。**每次做完一个词条立即更新，不攒着。**

---

## 八、质量红线（不可违反）

1. **凡引用导游原文，一字不差，绝不润色**
2. 内部版不压缩、不改写母版原意
3. 所有版本内链必须是绝对路径
4. 中英文 slug 必须完全一致
5. 英文版用重写式翻译（西方受众习惯），不生硬直译

---

## 九、git 提交规范

```
Add [词条中文名] ([英文名]) — Chinese/English 4-version entry

- zh/[slug]/index.md: ...
- zh/[slug]/internal.md: ...
- ...
- mkdocs.zh.yml: added [词条名] to nav
- zh/catalog/index.md: added to Section [X]

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
```

---

## 十、交付格式

- 中文完成后：给用户 `http://wiki.lifecosmos.org/zh/[slug]/` 链接
- 英文完成后：给用户 `http://wiki.lifecosmos.org/en/[slug]/` 链接
- 不需要列出所有子页链接，用户点入口页自己导航

---

## 十一、现有词条母版（待做）

位于 `词条母版/`（已做的在 `词条母版/已做词条/`）：

| 文件 | 建议 slug |
|------|-----------|
| 八无境界.txt | `eight-no-realms` |
| 抱一.txt | `embrace-the-one` |
| 提升振动频率.txt | `raise-vibration-frequency` |
| 灵.txt | `ling-spirit` |
| 灵觉.txt | 已有（`spiritual-sensing`），仅需确认目录 |
| 自洽.txt | `self-coherence` |
| 零态.txt | `zero-state` |

---

## 十二、站点地址

- 中文站：`http://wiki.lifecosmos.org/zh/`
- 英文站：`http://wiki.lifecosmos.org/en/`
- 中文目录：`http://wiki.lifecosmos.org/zh/catalog/`
- 英文目录：`http://wiki.lifecosmos.org/en/catalog/`
- GitHub：`https://github.com/Yixian-771/lifecosmos-wiki-pages`
- 本地路径：`F:\百科馆\lifecosmos-wiki-pages\`
