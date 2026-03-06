# YouTube 批量上传与定时发布（v0.1）

## 0. 目标
- 批量上传电脑视频
- 自动填写标题/描述/标签
- 定时发布
- 不依赖浏览器手动点点点

---

## 1. 准备 Google Cloud（一次性）
1. 打开 https://console.cloud.google.com/
2. 新建项目（如：openclaw-youtube-publisher）
3. 启用 API：**YouTube Data API v3**
4. OAuth 同意屏幕：选择 External（测试即可）
5. 创建 OAuth 凭证：`Desktop app`
6. 下载 `client_secret_xxx.json`
7. 把 json 放到服务器，例如：
   - `/root/.openclaw/credentials/youtube_client_secret.json`

> 注意：首次授权会弹出浏览器登录 Google 账号。

---

## 2. 安装依赖（服务器）
```bash
pip install --user google-api-python-client google-auth google-auth-oauthlib
```

---

## 3. 准备上传队列表
模板文件：`youtube_queue_template_v0.1.csv`

字段说明：
- `file_path`: 视频绝对路径
- `title`: 标题
- `description`: 描述（支持换行）
- `tags`: 逗号分隔
- `category_id`: 常用 22（People & Blogs）
- `privacy_status`: private/unlisted/public（建议 private）
- `publish_at`: UTC 时间，格式 `YYYY-MM-DDTHH:MM:SSZ`
- `playlist_id`: 可空
- `made_for_kids`: true/false
- `language`: 如 `zh-CN`
- `thumbnail_path`: 封面图路径（可空）

---

## 4. 先 Dry Run 检查
```bash
python3 /root/.openclaw/workspace/youtube_batch_uploader_v0.1.py \
  --csv /root/.openclaw/workspace/youtube_queue_template_v0.1.csv \
  --client-secret /root/.openclaw/credentials/youtube_client_secret.json \
  --dry-run
```

---

## 5. 正式执行上传
```bash
python3 /root/.openclaw/workspace/youtube_batch_uploader_v0.1.py \
  --csv /root/.openclaw/workspace/youtube_queue_template_v0.1.csv \
  --client-secret /root/.openclaw/credentials/youtube_client_secret.json
```

首次会自动 OAuth 授权，成功后生成：
- `/root/.openclaw/credentials/youtube_token.json`

后续就无需再次登录（除非 token 失效）。

---

## 6. 定时发布说明
- `publish_at` 填 UTC 时间。
- 脚本会把视频先上传为 private，并写入 publishAt。
- 到时间 YouTube 自动公开（按频道规则）。

### 中国时间换算
- 北京时间 = UTC + 8
- 例如北京时间 20:00 => UTC 12:00
- 填：`2026-03-02T12:00:00Z`

---

## 7. 常见问题
1. `quotaExceeded`
   - 当天 API 配额用完，次日再传或减批次。
2. `invalidPublishAt`
   - 时间格式错误，必须是 UTC ISO8601。
3. `forbidden`
   - OAuth 权限或账号频道权限不足。
4. 文件找不到
   - 检查 `file_path` 是否为服务器真实路径。

---

## 8. 推荐工作流（最省事）
1. 你只维护 CSV（文件+标题+发布时间）
2. 我补全描述/标签模板
3. 脚本一次性上传+排程
4. 输出成功/失败日志

