# 禅院百科词条编写流程与标准 v2.0

> 本文档是实际操作标准，以此为准，忽略旧版文档。v3.0 起新增母版自编辑阶段。

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

> **入口页是导览页，不是内容页。** 绝不在入口页写分节展开内容。

结构固定为三块，除此之外不加任何 `##` 标题：

```
[文件头注释]

# 词条名

[导言：1-2 段，共约 100-150 字]
  - 第一段：定义三个核心概念及其关系
  - 第二段：点出核心要素/路径，以一个典型意象/例子收尾

---

## 版本导航

| 版本 | 适合读者 | 核心内容 |
[三行表格]

---

## 相关词条

[内链横排，· 分隔]
```

**媒体块（2026-07-03 起）**：已做成视频的词条，在导言之后、「版本导航」之前允许加一个 `## 视频版` 块——内容为 YouTube 嵌入播放器（`youtube-nocookie.com/embed/<ID>`，`aspect-ratio:4/3`，`max-width:760px`）+ 一个 `??? info` 折叠图文幻灯集（图片放本词条 `slides/` 子目录，宽 1280、单张 ≤200KB 左右）。中文页嵌中文视频，英文页嵌英文视频；英文视频未发布前英文页只放 `## Slides` 图集。这是入口页"不加分节"规则的唯一例外。

**参考标准**：`zh/yuhuachengxian/index.md`（可随时对照）

**禁止事项**：入口页不写"一、二、三……"分节，不写参考文献，不放引用块，不展开正文内容。所有详细内容放进 internal / academic / friendly 三个版本。

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

**触发词：用户说"做词条 XXX"**

### 第一阶段：编辑母版（需用户确认）

```
1. 按《编辑禅院百科词条母版要求.txt》执行三轮检索
   （路径：词条母版/编辑禅院百科词条母版要求.txt）
2. 将母版写入 词条母版/[词条名].txt
3. 告知用户母版已完成，等待确认
```

> ⚠️ 母版未获用户确认前，不进入第二阶段。

### 第二阶段：编辑八版本并推送（用户确认母版后执行）

```
4. 确认 slug（查 translation-glossary.csv 或参照已有词条）
5. 写中文四版（index → internal → academic → friendly）
6. 更新 mkdocs.zh.yml（在 nav 中加一行，新词条置顶）
7. 更新 zh/catalog/index.md（加入对应分类）
8. git commit + push
9. 给用户中文入口链接
10. 写英文四版（index → internal → academic → friendly）
11. 更新 mkdocs.en.yml
12. 更新 en/catalog/index.md
13. git commit + push
14. 给用户英文入口链接
15. 将母版文件移入 词条母版/已做词条/
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
