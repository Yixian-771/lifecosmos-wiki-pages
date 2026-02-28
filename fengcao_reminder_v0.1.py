#!/usr/bin/env python3
import json
import re
from pathlib import Path
from datetime import datetime, timezone

import requests
from bs4 import BeautifulSoup

BASE = "https://smcy.xyz/new"
LIST_URL = BASE + "/forum.php?mod=forumdisplay&fid=368"
STATE = Path('/root/.openclaw/workspace/memory/fengcao-reminder-state.json')
COOKIE = Path('/root/.openclaw/credentials/fengcao_forum.cookie')
MSG = '@心舟草 请看主贴封草'


def now_iso():
    return datetime.now(timezone.utc).isoformat()


def load_session():
    s = requests.Session()
    s.headers.update({'User-Agent': 'Mozilla/5.0 OpenClaw FENGCAO Reminder'})
    raw = COOKIE.read_text(encoding='utf-8').strip()
    for p in raw.split(';'):
        if '=' in p:
            k, v = p.strip().split('=', 1)
            s.cookies.set(k, v, domain='smcy.xyz')
    return s


def parse_list(html):
    soup = BeautifulSoup(html, 'html.parser')
    out = []
    for tb in soup.select('tbody[id^="normalthread_"]'):
        a = tb.select_one('a.s.xst, a.xst')
        if not a:
            continue
        href = a.get('href', '')
        m = re.search(r'tid=(\d+)', href)
        if not m:
            continue
        tid = m.group(1)
        pub = (tb.select_one('td.by em span') or tb.select_one('td.by em'))
        pub_text = pub.get_text(' ', strip=True) if pub else ''
        out.append({
            'tid': tid,
            'title': a.get_text(strip=True),
            'url': f"{BASE}/forum.php?mod=viewthread&tid={tid}",
            'pub': pub_text,
        })
    return out


def is_today(pub_text: str) -> bool:
    if any(x in pub_text for x in ['分钟前', '小时前', '今天', '半小时前', '刚刚']):
        return True
    if any(x in pub_text for x in ['昨天', '天前']):
        return False
    return True


def thread_info(s, tid):
    url = f"{BASE}/forum.php?mod=viewthread&tid={tid}"
    r = s.get(url, timeout=20)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, 'html.parser')

    posts = []
    for p in soup.select('#postlist > div[id^="post_"]'):
        author = p.select_one('.authi a.xw1, .authi a')
        body = p.select_one('.t_f')
        posts.append({
            'author': author.get_text(' ', strip=True) if author else '',
            'text': body.get_text('\n', strip=True) if body else '',
        })

    has_seal = any(('心舟草' in x['author']) and ('封草信息' in x['text'] or re.search(r'封.+为.+草', x['text'])) for x in posts)
    has_reminder = any(MSG in x['text'] for x in posts)
    form = soup.select_one('#fastpostform')
    return {'has_seal': has_seal, 'has_reminder': has_reminder, 'form': form}


def post_reminder(s, form, tid):
    action = form.get('action', '')
    post_url = BASE + '/' + action
    if 'inajax=1' not in post_url:
        post_url += '&inajax=1'
    data = {}
    for inp in form.select('input[name]'):
        data[inp.get('name')] = inp.get('value', '')
    data['message'] = MSG
    data['replysubmit'] = 'yes'

    r = s.post(post_url, data=data, timeout=20)
    ok = ('回复发布成功' in r.text) or ('succeedhandle_fastpost' in r.text)
    return ok, r.text[:200]


def load_state():
    if STATE.exists():
        return json.loads(STATE.read_text(encoding='utf-8'))
    return {'reminded': {}, 'history': []}


def save_state(st):
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(st, ensure_ascii=False, indent=2), encoding='utf-8')


def main():
    s = load_session()
    st = load_state()

    html = s.get(LIST_URL, timeout=20).text
    items = parse_list(html)

    actions = []
    for it in items:
        if not is_today(it['pub']):
            continue
        tid = it['tid']
        info = thread_info(s, tid)
        if info['has_seal']:
            continue
        if info['has_reminder']:
            actions.append({'tid': tid, 'title': it['title'], 'action': 'skip_already_replied'})
            continue
        if tid in st['reminded']:
            actions.append({'tid': tid, 'title': it['title'], 'action': 'skip_state_once'})
            continue
        if not info['form']:
            actions.append({'tid': tid, 'title': it['title'], 'action': 'skip_no_form'})
            continue
        ok, brief = post_reminder(s, info['form'], tid)
        if ok:
            st['reminded'][tid] = now_iso()
            actions.append({'tid': tid, 'title': it['title'], 'action': 'posted'})
        else:
            actions.append({'tid': tid, 'title': it['title'], 'action': 'post_failed', 'brief': brief})

    st['history'].append({'ts': now_iso(), 'actions': actions})
    st['history'] = st['history'][-50:]
    save_state(st)

    print(json.dumps({'ts': now_iso(), 'actions': actions}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
