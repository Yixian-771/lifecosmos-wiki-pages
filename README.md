# 生命禅院百科（wiki.lifecosmos.org）源文件

中英双语百科站的源仓库。push 到 `main` 后由 `.github/workflows/deploy.yml` 自动用 MkDocs 构建并部署。

`zh/`、`en/` 会原样变成网站，**只放读者阅读的内容**；制作记录、编辑规范、流水线脚本都放在它们之外。

## 目录

| 位置 | 内容 |
|---|---|
| `zh/`、`en/` | 词条正文（每条一个 slug 目录：`index.md` 入口＋友好版/学术版/内部版，`slides/` 视频幻灯图集） |
| `mkdocs.zh.yml`、`mkdocs.en.yml` | 中英两站的构建配置（`site/` 是本地构建产物，不提交） |
| `词条母版/` | 编写词条用的母版资料（已做的在 `已做词条/`，申请与编辑要求也在这里） |
| `编辑规范/` | 给编辑看的规范：词条编写流程与标准、建条 SOP、slug 命名、状态追踪、结构说明书、中英译名对照（不在网站目录里，不会发布） |
| `video-pilot/` | 词条视频的渲染流水线（引擎 `make_show.py`、`build_audio_srt.py`，各词条配方 `*_narration.py`，工具 `tools/`）；渲染产物和本机脚本不进仓库（见 `.gitignore`） |

## 视频化流程

完整流程（选题 → 幻灯 → 配方 → 渲染 → YouTube → 百科站 → 论坛）见本地 `F:\百科馆\词条视频制作发布SOP.md`；进度以 `F:\百科馆\生命禅院百科_全部词条制作顺序总控表_v1.xlsx` 为准。

## 本地预览

```
python -m mkdocs serve -f mkdocs.zh.yml
python -m mkdocs build -f mkdocs.en.yml
```
