# -*- coding: utf-8 -*-
"""一键启动隐藏渲染队列（取代过去每次手写的 render_*.ps1 / launch_*.ps1）。

用法（在 video-pilot 目录下，用 uv 的 python）：
    python tools\\render_queue.py <配方名> [<配方名> ...] [--queue 队列名] [--clean] [--dry]

· 配方名＝*_narration.py 去掉 .py（例 love_narration love_en_narration）。多个配方在同一条队列里依次渲；
  要并行就分开跑多次（建议同时最多 2 条，渲染吃 CPU）。
· --clean：先删这些配方旧的配音缓存（<NAME>_audio.mp3 / _lines.txt / _subs.srt / _*_padded.mp3 / _*_mix.wav），
  重渲改过口播稿的片子必须带上，否则会沿用旧配音。
· --dry：只生成队列脚本、不启动。
· 队列脚本落在 _queues\\<队列名>.ps1（UTF-8 BOM），进度写 _queues\\<队列名>_progress.txt，每个配方的日志在 _queues\\log_<配方名>.txt。
· 用 WMI Win32_Process.Create 启动并 ShowWindow=0：脱离当前会话、没有黑窗，用户关窗口也不会杀掉。
· 成片出在 video-pilot\\<NAME>_show.mp4；看进度：Get-Content _queues\\<队列名>_progress.txt；
  没有 TEMP_MPY_wvf_snd.mp4 且 progress 里有 done 才算渲完。
· 这个脚本里的路径全部在 Python 里拼好，避开了 PowerShell 里 "\\r"、"\\t" 被吃掉的坑（2026-11-05 踩过）。
"""
import importlib, os, re, subprocess, sys, time

VP = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PY = r"C:\Users\yixia\AppData\Roaming\uv\python\cpython-3.11.15-windows-x86_64-none\python.exe"
PYPATH = r"E:\CodexData\temp\edge_tts_latest;C:\Users\yixia\AppData\Local\hermes\hermes-agent\venv\Lib\site-packages"


def recipe_name(mod):
    sys.path.insert(0, VP)
    m = importlib.import_module(mod)
    return getattr(m, "NAME")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = [a for a in sys.argv[1:] if a.startswith("--")]
    qname = None
    if "--queue" in sys.argv:
        qname = sys.argv[sys.argv.index("--queue") + 1]
        args = [a for a in args if a != qname]
    if not args:
        print(__doc__)
        return
    for a in args:
        assert os.path.exists(os.path.join(VP, a + ".py")), "找不到配方 " + a
    qname = qname or ("q_" + time.strftime("%m%d_%H%M%S"))
    qdir = os.path.join(VP, "_queues")
    os.makedirs(qdir, exist_ok=True)
    if "--clean" in flags:
        for a in args:
            n = recipe_name(a)
            for pat in (n + "_audio.mp3", n + "_lines.txt", n + "_subs.srt"):
                p = os.path.join(VP, pat)
                if os.path.exists(p):
                    os.remove(p); print("删旧缓存", pat)
            for f in os.listdir(VP):
                if re.fullmatch(r"_%s_(padded\.mp3|mix\.wav)" % re.escape(n), f):
                    os.remove(os.path.join(VP, f)); print("删旧缓存", f)
    prog = os.path.join(qdir, qname + "_progress.txt")
    L = ['$py = "%s"' % PY,
         '$env:PYTHONPATH = "%s"' % PYPATH,
         '$env:PYTHONIOENCODING = "utf-8"',
         '$ErrorActionPreference = "Continue"',
         'Set-Location "%s"' % VP]
    for a in args:
        log = os.path.join(qdir, "log_%s.txt" % a)
        L.append('& $py make_show.py --config %s *> "%s"' % (a, log))
        L.append('"done %s $(Get-Date)" | Add-Content "%s"' % (a, prog))
    ps1 = os.path.join(qdir, qname + ".ps1")
    with open(ps1, "w", encoding="utf-8-sig", newline="\r\n") as f:
        f.write("\n".join(L) + "\n")
    print("队列脚本:", ps1)
    if "--dry" in flags:
        return
    ps = ("$s = New-CimInstance -ClassName Win32_ProcessStartup -ClientOnly -Property @{ShowWindow=[uint16]0};"
          "$r = Invoke-CimMethod -ClassName Win32_Process -MethodName Create -Arguments @{"
          "CommandLine='powershell.exe -WindowStyle Hidden -NoProfile -ExecutionPolicy Bypass -File \"%s\"';"
          "CurrentDirectory='%s';ProcessStartupInformation=$s};"
          "'ReturnValue='+$r.ReturnValue+' PID='+$r.ProcessId") % (ps1, VP)
    out = subprocess.run(["powershell.exe", "-NoProfile", "-Command", ps], capture_output=True, text=True)
    print(out.stdout.strip(), out.stderr.strip())
    time.sleep(15)
    chk = subprocess.run(["powershell.exe", "-NoProfile", "-Command",
                          "(Get-CimInstance Win32_Process | ? { $_.CommandLine -match 'make_show' }).Count"],
                         capture_output=True, text=True).stdout.strip()
    print("make_show 进程数:", chk, "（0 表示没起来，看 _queues 里的日志）")
    print("进度文件:", prog)


if __name__ == "__main__":
    main()
