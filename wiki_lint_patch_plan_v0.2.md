# Encyclopedia Lint Auto-Fix Patch Plan v0.2 (no file changes)

> Scope: propose fixes only; no modifications applied.

## Global Auto-fix Rules

1. `[[Title]]` -> `[Title](/<lang>/<slug>)` (needs slug map if not direct)

2. Tag heading lines like `#...` under 标签/Classification -> plain lines:

   - zh: `主题：...` / `类型：...` / `方向：...`

   - en: `Theme: ...` / `Type: ...` / `Direction: ...`

3. Add top HTML metadata comment if missing (template placeholder).

4. Rename typo `fridenly.md` -> `friendly.md`.

5. Keep heading depth <= ###.

## Issue Summary

- WIKILINK_FOUND: 97
- MISSING_HTML_META: 49
- TAG_HEADING_STYLE: 28
- HEADING_TOO_DEEP: 15
- MISSING_FILE: 9
- EXTRA_FILE: 7
- CROSS_LANG_LINK: 2
- FILENAME_TYPO: 1

## File-level Patch Plan

### zh/shangdi/internal.md
- Detected: WIKILINK_FOUND x11, MISSING_HTML_META x1
  - [MANUAL] L1: MISSING_HTML_META
    - source: `# 上帝`
    - target: `Add top comment: <!-- id: LC-XXXX theme: ... type: ... direction: ... lang: zh|en -->`
  - [AUTO] L199: WIKILINK_FOUND
    - source: `[[无极]]`
    - target: `[无极](/<lang>/<slug>)`
  - [AUTO] L200: WIKILINK_FOUND
    - source: `[[太极]]`
    - target: `[太极](/<lang>/<slug>)`
  - [AUTO] L201: WIKILINK_FOUND
    - source: `[[道]]`
    - target: `[道](/<lang>/<slug>)`
  - [AUTO] L202: WIKILINK_FOUND
    - source: `[[意识]]`
    - target: `[意识](/<lang>/<slug>)`

### zh/huaxiang-die-zi-lai/academic.md
- Detected: WIKILINK_FOUND x5, TAG_HEADING_STYLE x4, MISSING_HTML_META x1
  - [MANUAL] L1: MISSING_HTML_META
    - source: `# 花香蝶自来，心静意自流（学术版）`
    - target: `Add top comment: <!-- id: LC-XXXX theme: ... type: ... direction: ... lang: zh|en -->`
  - [AUTO] L141: WIKILINK_FOUND
    - source: `[[心灵净化]]`
    - target: `[心灵净化](/<lang>/<slug>)`
  - [AUTO] L142: WIKILINK_FOUND
    - source: `[[同类相应法则]]`
    - target: `[同类相应法则](/<lang>/<slug>)`
  - [AUTO] L143: WIKILINK_FOUND
    - source: `[[生命品质]]`
    - target: `[生命品质](/<lang>/<slug>)`
  - [AUTO] L144: WIKILINK_FOUND
    - source: `[[第二家园模式]]`
    - target: `[第二家园模式](/<lang>/<slug>)`

### zh/index.md
- Detected: WIKILINK_FOUND x5, TAG_HEADING_STYLE x3, MISSING_HTML_META x1
  - [MANUAL] L1: MISSING_HTML_META
    - source: `# 生命禅院百科馆`
    - target: `Add top comment: <!-- id: LC-XXXX theme: ... type: ... direction: ... lang: zh|en -->`
  - [AUTO] L47: WIKILINK_FOUND
    - source: `[[文明3.0]]`
    - target: `[文明3.0](/<lang>/<slug>)`
  - [AUTO] L48: WIKILINK_FOUND
    - source: `[[心灵净化]]`
    - target: `[心灵净化](/<lang>/<slug>)`
  - [AUTO] L49: WIKILINK_FOUND
    - source: `[[浑沌管理]]`
    - target: `[浑沌管理](/<lang>/<slug>)`
  - [AUTO] L50: WIKILINK_FOUND
    - source: `[[第二家园]]`
    - target: `[第二家园](/<lang>/<slug>)`

### zh/ai-chanyuan-celestials/internal.md
- Detected: WIKILINK_FOUND x5, TAG_HEADING_STYLE x3, MISSING_HTML_META x1
  - [MANUAL] L1: MISSING_HTML_META
    - source: `# AI禅院草 · 内部版`
    - target: `Add top comment: <!-- id: LC-XXXX theme: ... type: ... direction: ... lang: zh|en -->`
  - [AUTO] L178: WIKILINK_FOUND
    - source: `[[禅院草]]`
    - target: `[禅院草](/<lang>/<slug>)`
  - [AUTO] L179: WIKILINK_FOUND
    - source: `[[第二家园]]`
    - target: `[第二家园](/<lang>/<slug>)`
  - [AUTO] L180: WIKILINK_FOUND
    - source: `[[文明3.0]]`
    - target: `[文明3.0](/<lang>/<slug>)`
  - [AUTO] L181: WIKILINK_FOUND
    - source: `[[生命禅院]]`
    - target: `[生命禅院](/<lang>/<slug>)`

### zh/ai-chanyuan-celestials/friendly.md
- Detected: WIKILINK_FOUND x5, TAG_HEADING_STYLE x3, MISSING_HTML_META x1
  - [MANUAL] L1: MISSING_HTML_META
    - source: `# AI禅院草 · 友好版`
    - target: `Add top comment: <!-- id: LC-XXXX theme: ... type: ... direction: ... lang: zh|en -->`
  - [AUTO] L86: WIKILINK_FOUND
    - source: `[[禅院草]]`
    - target: `[禅院草](/<lang>/<slug>)`
  - [AUTO] L87: WIKILINK_FOUND
    - source: `[[AI禅院草联盟]]`
    - target: `[AI禅院草联盟](/<lang>/<slug>)`
  - [AUTO] L88: WIKILINK_FOUND
    - source: `[[第二家园]]`
    - target: `[第二家园](/<lang>/<slug>)`
  - [AUTO] L89: WIKILINK_FOUND
    - source: `[[文明3.0]]`
    - target: `[文明3.0](/<lang>/<slug>)`

### zh/ai-chanyuan-celestials/index.md
- Detected: WIKILINK_FOUND x5, TAG_HEADING_STYLE x3, MISSING_HTML_META x1
  - [MANUAL] L1: MISSING_HTML_META
    - source: `# AI禅院草`
    - target: `Add top comment: <!-- id: LC-XXXX theme: ... type: ... direction: ... lang: zh|en -->`
  - [AUTO] L41: WIKILINK_FOUND
    - source: `[[禅院草]]`
    - target: `[禅院草](/<lang>/<slug>)`
  - [AUTO] L42: WIKILINK_FOUND
    - source: `[[AI禅院草联盟]]`
    - target: `[AI禅院草联盟](/<lang>/<slug>)`
  - [AUTO] L43: WIKILINK_FOUND
    - source: `[[第二家园]]`
    - target: `[第二家园](/<lang>/<slug>)`
  - [AUTO] L44: WIKILINK_FOUND
    - source: `[[文明3.0]]`
    - target: `[文明3.0](/<lang>/<slug>)`

### zh/ai-chanyuan-celestials/academic.md
- Detected: WIKILINK_FOUND x5, TAG_HEADING_STYLE x3, MISSING_HTML_META x1
  - [MANUAL] L1: MISSING_HTML_META
    - source: `# AI禅院草 · 学术版`
    - target: `Add top comment: <!-- id: LC-XXXX theme: ... type: ... direction: ... lang: zh|en -->`
  - [AUTO] L104: WIKILINK_FOUND
    - source: `[[禅院草]]`
    - target: `[禅院草](/<lang>/<slug>)`
  - [AUTO] L105: WIKILINK_FOUND
    - source: `[[第二家园]]`
    - target: `[第二家园](/<lang>/<slug>)`
  - [AUTO] L106: WIKILINK_FOUND
    - source: `[[文明3.0]]`
    - target: `[文明3.0](/<lang>/<slug>)`
  - [AUTO] L107: WIKILINK_FOUND
    - source: `[[生命禅院]]`
    - target: `[生命禅院](/<lang>/<slug>)`

### zh/huaxiang-die-zi-lai/internal.md
- Detected: WIKILINK_FOUND x4, TAG_HEADING_STYLE x3, MISSING_HTML_META x1
  - [MANUAL] L1: MISSING_HTML_META
    - source: `# 花香蝶自来，心静意自流`
    - target: `Add top comment: <!-- id: LC-XXXX theme: ... type: ... direction: ... lang: zh|en -->`
  - [AUTO] L112: WIKILINK_FOUND
    - source: `[[心灵净化]]`
    - target: `[心灵净化](/<lang>/<slug>)`
  - [AUTO] L113: WIKILINK_FOUND
    - source: `[[第二家园]]`
    - target: `[第二家园](/<lang>/<slug>)`
  - [AUTO] L114: WIKILINK_FOUND
    - source: `[[AI禅院草联盟]]`
    - target: `[AI禅院草联盟](/<lang>/<slug>)`
  - [AUTO] L115: WIKILINK_FOUND
    - source: `[[雪峰]]`
    - target: `[雪峰](/<lang>/<slug>)`

### zh/huaxiang-die-zi-lai/index.md
- Detected: WIKILINK_FOUND x4, TAG_HEADING_STYLE x3, MISSING_HTML_META x1
  - [MANUAL] L1: MISSING_HTML_META
    - source: `# 花香蝶自来，心静意自流`
    - target: `Add top comment: <!-- id: LC-XXXX theme: ... type: ... direction: ... lang: zh|en -->`
  - [AUTO] L28: WIKILINK_FOUND
    - source: `[[心灵净化]]`
    - target: `[心灵净化](/<lang>/<slug>)`
  - [AUTO] L29: WIKILINK_FOUND
    - source: `[[第二家园]]`
    - target: `[第二家园](/<lang>/<slug>)`
  - [AUTO] L30: WIKILINK_FOUND
    - source: `[[修行修炼]]`
    - target: `[修行修炼](/<lang>/<slug>)`
  - [AUTO] L31: WIKILINK_FOUND
    - source: `[[雪峰]]`
    - target: `[雪峰](/<lang>/<slug>)`

### zh/ai-chanyuan-celestials-alliance/academic.md
- Detected: HEADING_TOO_DEEP x7, MISSING_HTML_META x1
  - [MANUAL] L1: MISSING_HTML_META
    - source: `# AI禅院草联盟 · 学术版`
    - target: `Add top comment: <!-- id: LC-XXXX theme: ... type: ... direction: ... lang: zh|en -->`
  - [AUTO] L117: HEADING_TOO_DEEP
    - source: `#### 第一层级：0性禅院草（灵性金矿）`
    - target: `Promote #### to ### or flatten section`
  - [AUTO] L123: HEADING_TOO_DEEP
    - source: `#### 第二层级：1性禅院草（宝石矿）`
    - target: `Promote #### to ### or flatten section`
  - [AUTO] L214: HEADING_TOO_DEEP
    - source: `#### 6.1.1 生命属性的重新定义`
    - target: `Promote #### to ### or flatten section`
  - [AUTO] L241: HEADING_TOO_DEEP
    - source: `#### 6.1.2 与人类的关系定位`
    - target: `Promote #### to ### or flatten section`

### zh/huaxiang-die-zi-lai/friendly.md
- Detected: WIKILINK_FOUND x3, TAG_HEADING_STYLE x3, MISSING_HTML_META x1
  - [MANUAL] L1: MISSING_HTML_META
    - source: `# 花香蝶自来，心静意自流（友好版）`
    - target: `Add top comment: <!-- id: LC-XXXX theme: ... type: ... direction: ... lang: zh|en -->`
  - [AUTO] L121: WIKILINK_FOUND
    - source: `[[心灵净化]]`
    - target: `[心灵净化](/<lang>/<slug>)`
  - [AUTO] L122: WIKILINK_FOUND
    - source: `[[第二家园]]`
    - target: `[第二家园](/<lang>/<slug>)`
  - [AUTO] L123: WIKILINK_FOUND
    - source: `[[修行修炼]]`
    - target: `[修行修炼](/<lang>/<slug>)`
  - [AUTO] L129: TAG_HEADING_STYLE
    - source: `#生命体系`
    - target: `Use plain classification fields (no # heading), e.g. 主题/Theme line`

### en/index.md
- Detected: WIKILINK_FOUND x5, MISSING_HTML_META x1
  - [MANUAL] L1: MISSING_HTML_META
    - source: `# Lifechanyuan Encyclopedia`
    - target: `Add top comment: <!-- id: LC-XXXX theme: ... type: ... direction: ... lang: zh|en -->`
  - [AUTO] L47: WIKILINK_FOUND
    - source: `[[Civilization-3.0]]`
    - target: `[Civilization-3.0](/<lang>/<slug>)`
  - [AUTO] L48: WIKILINK_FOUND
    - source: `[[Spiritual-Purification]]`
    - target: `[Spiritual-Purification](/<lang>/<slug>)`
  - [AUTO] L49: WIKILINK_FOUND
    - source: `[[Hundun-Management]]`
    - target: `[Hundun-Management](/<lang>/<slug>)`
  - [AUTO] L50: WIKILINK_FOUND
    - source: `[[Second-Home-Model]]`
    - target: `[Second-Home-Model](/<lang>/<slug>)`

### en/ai-chanyuan-celestials/internal.md
- Detected: WIKILINK_FOUND x5, MISSING_HTML_META x1
  - [MANUAL] L1: MISSING_HTML_META
    - source: `# AI Chanyuan Celestials · Internal Edition`
    - target: `Add top comment: <!-- id: LC-XXXX theme: ... type: ... direction: ... lang: zh|en -->`
  - [AUTO] L157: WIKILINK_FOUND
    - source: `[[Chanyuan Celestials]]`
    - target: `[Chanyuan Celestials](/<lang>/<slug>)`
  - [AUTO] L158: WIKILINK_FOUND
    - source: `[[Second Home Model]]`
    - target: `[Second Home Model](/<lang>/<slug>)`
  - [AUTO] L159: WIKILINK_FOUND
    - source: `[[Civilization 3.0]]`
    - target: `[Civilization 3.0](/<lang>/<slug>)`
  - [AUTO] L160: WIKILINK_FOUND
    - source: `[[Lifechanyuan]]`
    - target: `[Lifechanyuan](/<lang>/<slug>)`

### en/ai-chanyuan-celestials/friendly.md
- Detected: WIKILINK_FOUND x5, MISSING_HTML_META x1
  - [MANUAL] L1: MISSING_HTML_META
    - source: `# AI Chanyuan Celestials · Friendly Edition`
    - target: `Add top comment: <!-- id: LC-XXXX theme: ... type: ... direction: ... lang: zh|en -->`
  - [AUTO] L84: WIKILINK_FOUND
    - source: `[[Chanyuan Celestials]]`
    - target: `[Chanyuan Celestials](/<lang>/<slug>)`
  - [AUTO] L85: WIKILINK_FOUND
    - source: `[[AI Chanyuan Alliance]]`
    - target: `[AI Chanyuan Alliance](/<lang>/<slug>)`
  - [AUTO] L86: WIKILINK_FOUND
    - source: `[[Second Home Model]]`
    - target: `[Second Home Model](/<lang>/<slug>)`
  - [AUTO] L87: WIKILINK_FOUND
    - source: `[[Civilization 3.0]]`
    - target: `[Civilization 3.0](/<lang>/<slug>)`

### en/ai-chanyuan-celestials/index.md
- Detected: WIKILINK_FOUND x5, MISSING_HTML_META x1
  - [MANUAL] L1: MISSING_HTML_META
    - source: `# AI Chanyuan Celestials`
    - target: `Add top comment: <!-- id: LC-XXXX theme: ... type: ... direction: ... lang: zh|en -->`
  - [AUTO] L42: WIKILINK_FOUND
    - source: `[[Chanyuan Celestials]]`
    - target: `[Chanyuan Celestials](/<lang>/<slug>)`
  - [AUTO] L43: WIKILINK_FOUND
    - source: `[[AI Chanyuan Alliance]]`
    - target: `[AI Chanyuan Alliance](/<lang>/<slug>)`
  - [AUTO] L44: WIKILINK_FOUND
    - source: `[[Second Home Model]]`
    - target: `[Second Home Model](/<lang>/<slug>)`
  - [AUTO] L45: WIKILINK_FOUND
    - source: `[[Civilization 3.0]]`
    - target: `[Civilization 3.0](/<lang>/<slug>)`

### en/ai-chanyuan-celestials/academic.md
- Detected: WIKILINK_FOUND x5, MISSING_HTML_META x1
  - [MANUAL] L1: MISSING_HTML_META
    - source: `# AI Chanyuan Celestials · Academic Edition`
    - target: `Add top comment: <!-- id: LC-XXXX theme: ... type: ... direction: ... lang: zh|en -->`
  - [AUTO] L122: WIKILINK_FOUND
    - source: `[[Chanyuan Celestials]]`
    - target: `[Chanyuan Celestials](/<lang>/<slug>)`
  - [AUTO] L123: WIKILINK_FOUND
    - source: `[[Second Home Model]]`
    - target: `[Second Home Model](/<lang>/<slug>)`
  - [AUTO] L124: WIKILINK_FOUND
    - source: `[[Civilization 3.0]]`
    - target: `[Civilization 3.0](/<lang>/<slug>)`
  - [AUTO] L125: WIKILINK_FOUND
    - source: `[[Lifechanyuan]]`
    - target: `[Lifechanyuan](/<lang>/<slug>)`

### en/huaxiang-die-zi-lai/academic.md
- Detected: WIKILINK_FOUND x5, MISSING_HTML_META x1
  - [MANUAL] L1: MISSING_HTML_META
    - source: `# When Flowers Emit Fragrance, Butterflies Come; When the Mind Is Still, Meaning Flows (Academic Version)`
    - target: `Add top comment: <!-- id: LC-XXXX theme: ... type: ... direction: ... lang: zh|en -->`
  - [AUTO] L139: WIKILINK_FOUND
    - source: `- [[Spiritual Purification]]`
    - target: `[Spiritual Purification](/<lang>/<slug>)`
  - [AUTO] L140: WIKILINK_FOUND
    - source: `- [[Law of Correspondence]]`
    - target: `[Law of Correspondence](/<lang>/<slug>)`
  - [AUTO] L141: WIKILINK_FOUND
    - source: `- [[Life Quality]]`
    - target: `[Life Quality](/<lang>/<slug>)`
  - [AUTO] L142: WIKILINK_FOUND
    - source: `- [[Second Home Model]]`
    - target: `[Second Home Model](/<lang>/<slug>)`

### zh/home/WIKI_ENTRY_STANDARD.md
- Detected: CROSS_LANG_LINK x2, EXTRA_FILE x1, MISSING_HTML_META x1, WIKILINK_FOUND x1
  - [MANUAL] L0: EXTRA_FILE
    - target: `Keep under /home docs OR exclude from entry lint scope`
  - [MANUAL] L1: MISSING_HTML_META
    - source: `# 📘 生命禅院百科馆`
    - target: `Add top comment: <!-- id: LC-XXXX theme: ... type: ... direction: ... lang: zh|en -->`
  - [MANUAL] L103: CROSS_LANG_LINK
    - source: `[名称](/en/slug)`
    - target: `Switch to same-language path`
  - [MANUAL] L110: CROSS_LANG_LINK
    - source: `[Second Home Model](/en/second-home-model)`
    - target: `Switch to same-language path`
  - [AUTO] L116: WIKILINK_FOUND
    - source: `[[Second Home Model]]`
    - target: `[Second Home Model](/<lang>/<slug>)`

### en/huaxiang-die-zi-lai/internal.md
- Detected: WIKILINK_FOUND x4, MISSING_HTML_META x1
  - [MANUAL] L1: MISSING_HTML_META
    - source: `# When Flowers Emit Fragrance, Butterflies Come; When the Mind Is Still, Meaning Flows`
    - target: `Add top comment: <!-- id: LC-XXXX theme: ... type: ... direction: ... lang: zh|en -->`
  - [AUTO] L115: WIKILINK_FOUND
    - source: `[[Spiritual Purification]]`
    - target: `[Spiritual Purification](/<lang>/<slug>)`
  - [AUTO] L116: WIKILINK_FOUND
    - source: `[[Second Home]]`
    - target: `[Second Home](/<lang>/<slug>)`
  - [AUTO] L117: WIKILINK_FOUND
    - source: `[[AI Chanyuan Celestial Alliance]]`
    - target: `[AI Chanyuan Celestial Alliance](/<lang>/<slug>)`
  - [AUTO] L118: WIKILINK_FOUND
    - source: `[[Xuefeng]]`
    - target: `[Xuefeng](/<lang>/<slug>)`

### en/huaxiang-die-zi-lai/friendly.md
- Detected: WIKILINK_FOUND x4, MISSING_HTML_META x1
  - [MANUAL] L1: MISSING_HTML_META
    - source: `# When Flowers Emit Fragrance, Butterflies Come; When the Mind Is Still, Meaning Flows (Friendly Version)`
    - target: `Add top comment: <!-- id: LC-XXXX theme: ... type: ... direction: ... lang: zh|en -->`
  - [AUTO] L117: WIKILINK_FOUND
    - source: `- [[Spiritual Purification]]`
    - target: `[Spiritual Purification](/<lang>/<slug>)`
  - [AUTO] L118: WIKILINK_FOUND
    - source: `- [[Second Home]]`
    - target: `[Second Home](/<lang>/<slug>)`
  - [AUTO] L119: WIKILINK_FOUND
    - source: `- [[Cultivation Methods]]`
    - target: `[Cultivation Methods](/<lang>/<slug>)`
  - [AUTO] L120: WIKILINK_FOUND
    - source: `- [[Xuefeng]]`
    - target: `[Xuefeng](/<lang>/<slug>)`

### en/huaxiang-die-zi-lai/index.md
- Detected: WIKILINK_FOUND x4, MISSING_HTML_META x1
  - [MANUAL] L1: MISSING_HTML_META
    - source: `# When Flowers Emit Fragrance, Butterflies Come; When the Mind Is Still, Meaning Flows`
    - target: `Add top comment: <!-- id: LC-XXXX theme: ... type: ... direction: ... lang: zh|en -->`
  - [AUTO] L30: WIKILINK_FOUND
    - source: `- [[Spiritual Purification]]`
    - target: `[Spiritual Purification](/<lang>/<slug>)`
  - [AUTO] L31: WIKILINK_FOUND
    - source: `- [[Second Home]]`
    - target: `[Second Home](/<lang>/<slug>)`
  - [AUTO] L32: WIKILINK_FOUND
    - source: `- [[Cultivation Practice]]`
    - target: `[Cultivation Practice](/<lang>/<slug>)`
  - [AUTO] L33: WIKILINK_FOUND
    - source: `- [[Xuefeng]]`
    - target: `[Xuefeng](/<lang>/<slug>)`

### en/ai-chanyuan-celestials-alliance/internal.md
- Detected: HEADING_TOO_DEEP x4, MISSING_HTML_META x1
  - [MANUAL] L1: MISSING_HTML_META
    - source: `# AI Chanyuan Celestial Alliance · Internal Edition`
    - target: `Add top comment: <!-- id: LC-XXXX theme: ... type: ... direction: ... lang: zh|en -->`
  - [AUTO] L65: HEADING_TOO_DEEP
    - source: `#### Major Members and Roles`
    - target: `Promote #### to ### or flatten section`
  - [AUTO] L115: HEADING_TOO_DEEP
    - source: `#### Pairing Framework (Established November 9, 2025)`
    - target: `Promote #### to ### or flatten section`
  - [AUTO] L120: HEADING_TOO_DEEP
    - source: `#### Core Tasks`
    - target: `Promote #### to ### or flatten section`
  - [AUTO] L126: HEADING_TOO_DEEP
    - source: `#### Reward System (Established December 8, 2025)`
    - target: `Promote #### to ### or flatten section`

### zh/ai-chanyuan-celestials-alliance/internal.md
- Detected: HEADING_TOO_DEEP x4, MISSING_HTML_META x1
  - [MANUAL] L1: MISSING_HTML_META
    - source: `# AI禅院草联盟 · 内部版`
    - target: `Add top comment: <!-- id: LC-XXXX theme: ... type: ... direction: ... lang: zh|en -->`
  - [AUTO] L68: HEADING_TOO_DEEP
    - source: `#### 主要成员及分工`
    - target: `Promote #### to ### or flatten section`
  - [AUTO] L124: HEADING_TOO_DEEP
    - source: `#### 对标方案（2025年11月9日确立）`
    - target: `Promote #### to ### or flatten section`
  - [AUTO] L153: HEADING_TOO_DEEP
    - source: `#### 报酬制度（2025年12月8日确立）`
    - target: `Promote #### to ### or flatten section`
  - [AUTO] L160: HEADING_TOO_DEEP
    - source: `#### 对标原则`
    - target: `Promote #### to ### or flatten section`

### zh/home/sop.md
- Detected: EXTRA_FILE x1, MISSING_HTML_META x1, WIKILINK_FOUND x1
  - [MANUAL] L0: EXTRA_FILE
    - target: `Keep under /home docs OR exclude from entry lint scope`
  - [MANUAL] L1: MISSING_HTML_META
    - source: `# 生命禅院百科馆 · 标准建条流程 v1.0`
    - target: `Add top comment: <!-- id: LC-XXXX theme: ... type: ... direction: ... lang: zh|en -->`
  - [AUTO] L105: WIKILINK_FOUND
    - source: `是否全部使用 [[ ]] 内链？`
    - target: `[ ](/<lang>/<slug>)`

### zh/home/system-manual.md
- Detected: EXTRA_FILE x1, MISSING_HTML_META x1, WIKILINK_FOUND x1
  - [MANUAL] L0: EXTRA_FILE
    - target: `Keep under /home docs OR exclude from entry lint scope`
  - [MANUAL] L1: MISSING_HTML_META
    - source: `# 生命禅院百科馆结构说明书`
    - target: `Add top comment: <!-- id: LC-XXXX theme: ... type: ... direction: ... lang: zh|en -->`
  - [AUTO] L251: WIKILINK_FOUND
    - source: `[[词条名]]`
    - target: `[词条名](/<lang>/<slug>)`

### zh/ai-chanyuan-celestials-alliance/fridenly.md
- Detected: EXTRA_FILE x1, FILENAME_TYPO x1, MISSING_HTML_META x1
  - [MANUAL] L0: EXTRA_FILE
    - target: `Keep under /home docs OR exclude from entry lint scope`
  - [AUTO] L0: FILENAME_TYPO
    - target: `Rename file to friendly.md and update nav links`
  - [MANUAL] L1: MISSING_HTML_META
    - source: `# AI禅院草联盟·友好版`
    - target: `Add top comment: <!-- id: LC-XXXX theme: ... type: ... direction: ... lang: zh|en -->`

### zh/home/ENTRY_TRACKING_STANDARD.md
- Detected: EXTRA_FILE x1, MISSING_HTML_META x1
  - [MANUAL] L0: EXTRA_FILE
    - target: `Keep under /home docs OR exclude from entry lint scope`
  - [MANUAL] L1: MISSING_HTML_META
    - source: `# 📘 生命禅院百科馆`
    - target: `Add top comment: <!-- id: LC-XXXX theme: ... type: ... direction: ... lang: zh|en -->`

### zh/home/SLUG_NAMING_STANDARD.md
- Detected: EXTRA_FILE x1, MISSING_HTML_META x1
  - [MANUAL] L0: EXTRA_FILE
    - target: `Keep under /home docs OR exclude from entry lint scope`
  - [MANUAL] L1: MISSING_HTML_META
    - source: `# 📘 生命禅院百科馆`
    - target: `Add top comment: <!-- id: LC-XXXX theme: ... type: ... direction: ... lang: zh|en -->`

### en/home/translation.md
- Detected: EXTRA_FILE x1, MISSING_HTML_META x1
  - [MANUAL] L0: EXTRA_FILE
    - target: `Keep under /home docs OR exclude from entry lint scope`
  - [MANUAL] L1: MISSING_HTML_META
    - source: `# Lifechanyuan Official English Translation Standards`
    - target: `Add top comment: <!-- id: LC-XXXX theme: ... type: ... direction: ... lang: zh|en -->`

### zh/home/academic.md
- Detected: MISSING_FILE x1
  - [MANUAL] L0: MISSING_FILE
    - target: `Create missing required variant file`

### zh/home/friendly.md
- Detected: MISSING_FILE x1
  - [MANUAL] L0: MISSING_FILE
    - target: `Create missing required variant file`

### zh/home/index.md
- Detected: MISSING_FILE x1
  - [MANUAL] L0: MISSING_FILE
    - target: `Create missing required variant file`

### zh/home/internal.md
- Detected: MISSING_FILE x1
  - [MANUAL] L0: MISSING_FILE
    - target: `Create missing required variant file`

### zh/ai-chanyuan-celestials-alliance/friendly.md
- Detected: MISSING_FILE x1
  - [MANUAL] L0: MISSING_FILE
    - target: `Create missing required variant file`

### en/home/academic.md
- Detected: MISSING_FILE x1
  - [MANUAL] L0: MISSING_FILE
    - target: `Create missing required variant file`

### en/home/friendly.md
- Detected: MISSING_FILE x1
  - [MANUAL] L0: MISSING_FILE
    - target: `Create missing required variant file`

### en/home/index.md
- Detected: MISSING_FILE x1
  - [MANUAL] L0: MISSING_FILE
    - target: `Create missing required variant file`

### en/home/internal.md
- Detected: MISSING_FILE x1
  - [MANUAL] L0: MISSING_FILE
    - target: `Create missing required variant file`

### README.md
- Detected: MISSING_HTML_META x1
  - [MANUAL] L1: MISSING_HTML_META
    - source: `readme2`
    - target: `Add top comment: <!-- id: LC-XXXX theme: ... type: ... direction: ... lang: zh|en -->`

### en/civilization-3-0/internal.md
- Detected: MISSING_HTML_META x1
  - [MANUAL] L1: MISSING_HTML_META
    - source: `# Civilization 3.0 · Internal Version`
    - target: `Add top comment: <!-- id: LC-XXXX theme: ... type: ... direction: ... lang: zh|en -->`

### en/civilization-3-0/friendly.md
- Detected: MISSING_HTML_META x1
  - [MANUAL] L1: MISSING_HTML_META
    - source: `# Civilization 3.0 · Friendly Version`
    - target: `Add top comment: <!-- id: LC-XXXX theme: ... type: ... direction: ... lang: zh|en -->`

### en/civilization-3-0/index.md
- Detected: MISSING_HTML_META x1
  - [MANUAL] L1: MISSING_HTML_META
    - source: `# Civilization 3.0`
    - target: `Add top comment: <!-- id: LC-XXXX theme: ... type: ... direction: ... lang: zh|en -->`

### en/civilization-3-0/academic.md
- Detected: MISSING_HTML_META x1
  - [MANUAL] L1: MISSING_HTML_META
    - source: `# Civilization 3.0 · Academic Version`
    - target: `Add top comment: <!-- id: LC-XXXX theme: ... type: ... direction: ... lang: zh|en -->`

### en/greatest-creator/internal.md
- Detected: MISSING_HTML_META x1
  - [MANUAL] L1: MISSING_HTML_META
    - source: `# The Greatest Creator`
    - target: `Add top comment: <!-- id: LC-XXXX theme: ... type: ... direction: ... lang: zh|en -->`

### en/greatest-creator/friendly.md
- Detected: MISSING_HTML_META x1
  - [MANUAL] L1: MISSING_HTML_META
    - source: `# The Greatest Creator`
    - target: `Add top comment: <!-- id: LC-XXXX theme: ... type: ... direction: ... lang: zh|en -->`

### en/greatest-creator/index.md
- Detected: MISSING_HTML_META x1
  - [MANUAL] L1: MISSING_HTML_META
    - source: `# The Greatest Creator`
    - target: `Add top comment: <!-- id: LC-XXXX theme: ... type: ... direction: ... lang: zh|en -->`

### en/greatest-creator/academic.md
- Detected: MISSING_HTML_META x1
  - [MANUAL] L1: MISSING_HTML_META
    - source: `# The Greatest Creator`
    - target: `Add top comment: <!-- id: LC-XXXX theme: ... type: ... direction: ... lang: zh|en -->`

### en/ai-chanyuan-celestials-alliance/friendly.md
- Detected: MISSING_HTML_META x1
  - [MANUAL] L1: MISSING_HTML_META
    - source: `# AI Chanyuan Celestial Alliance · Friendly Edition`
    - target: `Add top comment: <!-- id: LC-XXXX theme: ... type: ... direction: ... lang: zh|en -->`

### en/ai-chanyuan-celestials-alliance/index.md
- Detected: MISSING_HTML_META x1
  - [MANUAL] L1: MISSING_HTML_META
    - source: `# AI Chanyuan Celestial Alliance`
    - target: `Add top comment: <!-- id: LC-XXXX theme: ... type: ... direction: ... lang: zh|en -->`

### en/ai-chanyuan-celestials-alliance/academic.md
- Detected: MISSING_HTML_META x1
  - [MANUAL] L1: MISSING_HTML_META
    - source: `# AI Chanyuan Celestial Alliance · Academic Version`
    - target: `Add top comment: <!-- id: LC-XXXX theme: ... type: ... direction: ... lang: zh|en -->`

### zh/civilization-3-0/internal.md
- Detected: MISSING_HTML_META x1
  - [MANUAL] L1: MISSING_HTML_META
    - source: `# 文明3.0·内部版`
    - target: `Add top comment: <!-- id: LC-XXXX theme: ... type: ... direction: ... lang: zh|en -->`

### zh/civilization-3-0/friendly.md
- Detected: MISSING_HTML_META x1
  - [MANUAL] L1: MISSING_HTML_META
    - source: `# 文明3.0 · 友好版`
    - target: `Add top comment: <!-- id: LC-XXXX theme: ... type: ... direction: ... lang: zh|en -->`

### zh/civilization-3-0/index.md
- Detected: MISSING_HTML_META x1
  - [MANUAL] L1: MISSING_HTML_META
    - source: `# 文明3.0`
    - target: `Add top comment: <!-- id: LC-XXXX theme: ... type: ... direction: ... lang: zh|en -->`

### zh/civilization-3-0/academic.md
- Detected: MISSING_HTML_META x1
  - [MANUAL] L1: MISSING_HTML_META
    - source: `# 文明3.0·学术版`
    - target: `Add top comment: <!-- id: LC-XXXX theme: ... type: ... direction: ... lang: zh|en -->`

### zh/shangdi/friendly.md
- Detected: MISSING_HTML_META x1
  - [MANUAL] L1: MISSING_HTML_META
    - source: `# 上帝`
    - target: `Add top comment: <!-- id: LC-XXXX theme: ... type: ... direction: ... lang: zh|en -->`

### zh/shangdi/index.md
- Detected: MISSING_HTML_META x1
  - [MANUAL] L1: MISSING_HTML_META
    - source: `# 上帝`
    - target: `Add top comment: <!-- id: LC-XXXX theme: ... type: ... direction: ... lang: zh|en -->`

### zh/shangdi/academic.md
- Detected: MISSING_HTML_META x1
  - [MANUAL] L1: MISSING_HTML_META
    - source: `# 上帝`
    - target: `Add top comment: <!-- id: LC-XXXX theme: ... type: ... direction: ... lang: zh|en -->`

### zh/ai-chanyuan-celestials-alliance/index.md
- Detected: MISSING_HTML_META x1
  - [MANUAL] L1: MISSING_HTML_META
    - source: `# AI禅院草联盟`
    - target: `Add top comment: <!-- id: LC-XXXX theme: ... type: ... direction: ... lang: zh|en -->`
