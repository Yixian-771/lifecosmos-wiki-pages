# video-pilot · 词条视频渲染引擎

整个流水线的说明在 `F:\百科馆\交接说明_百科视频流水线_从这里开始.md` 和 `F:\百科馆\词条视频制作发布SOP.md`，这里只讲本目录。

## 里面有什么（只留这几类）

| 内容 | 说明 |
|---|---|
| `make_show.py`、`build_audio_srt.py` | 渲染引擎：配音（edge-tts）→字幕→合成成片 |
| `<名>_narration.py`、`<名>_en_narration.py` | 配方：`SLIDES`（每页逐句解说）、`META`（金句/聚光灯）、`NAME/VOICE/RATE/MUSIC`。`NAME` 带 `_show`，成片就叫 `<NAME>.mp4` |
| `slides_*\` | 配方用的幻灯 png（1376 宽，含修补过的页），渲染输入，别删 |
| `tools\` | wiki 上线脚本（`wiki_NNN_NNN.py`）、`render_queue.py`、`cmp_slides.py` 等 |

渲染产生的 `*_show.mp4`、`*_audio.mp3`、`*_subs.srt`、`*_lines.txt`、`_*_mix.wav`、`_*_padded.mp3`、日志、`_queues\`、`_frames\` 都是中间产物（已被 `.gitignore` 忽略），**核对成片已归档到 `F:\百科馆\百科MP4版\` 后删除**。

## 常用命令（用 uv 的 python，别用 hermes venv 的 python.exe，它被系统策略拦了）

```powershell
cd F:\百科馆\lifecosmos-wiki-pages\video-pilot
$py = "C:\Users\yixia\AppData\Roaming\uv\python\cpython-3.11.15-windows-x86_64-none\python.exe"
$env:PYTHONPATH = "F:\百科馆\小工具\依赖\edge_tts_latest;C:\Users\yixia\AppData\Local\hermes\hermes-agent\venv\Lib\site-packages"
$env:PYTHONIOENCODING = "utf-8"

& $py make_show.py --config <配方名> --stills        # 只配音＋出定格图，打印音频秒数（>600 秒先删句）
& $py tools\render_queue.py <配方> [<配方>…] --queue 名 [--clean]   # 隐藏渲染队列（每条 35–40 分钟）
```

判渲完：`ffprobe -select_streams v:0 -show_entries stream=duration <mp4>` 在 300–600 秒之间，并且没有 `*TEMP_MPY_wvf_snd.mp4`。
