#!/usr/bin/env python3
import csv
import os
import argparse
from datetime import datetime
from pathlib import Path

from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = ["https://www.googleapis.com/auth/youtube.upload", "https://www.googleapis.com/auth/youtube"]


def load_service(client_secret_file: str, token_file: str, auth_mode: str = "local"):
    creds = None
    if os.path.exists(token_file):
        creds = Credentials.from_authorized_user_file(token_file, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(client_secret_file, SCOPES)
            if auth_mode == "console":
                print("[AUTH] Console模式在当前库版本不可用，自动切换为本地回调模式。")
                print("[AUTH] 请在浏览器完成授权；如未自动打开，请复制终端中的授权链接手动打开。")
                creds = flow.run_local_server(port=0, open_browser=False)
            else:
                creds = flow.run_local_server(port=0)
        with open(token_file, "w", encoding="utf-8") as f:
            f.write(creds.to_json())
    return build("youtube", "v3", credentials=creds)


def parse_bool(v: str):
    return str(v).strip().lower() in ["1", "true", "yes", "y"]


def upload_video(youtube, row: dict):
    file_path = row["file_path"].strip()
    if not os.path.exists(file_path):
        raise FileNotFoundError(file_path)

    title = row.get("title", "").strip() or Path(file_path).stem
    description = row.get("description", "")
    tags = [t.strip() for t in row.get("tags", "").split(",") if t.strip()]
    category_id = str(row.get("category_id", "22")).strip() or "22"
    privacy_status = row.get("privacy_status", "private").strip() or "private"
    publish_at = row.get("publish_at", "").strip()
    made_for_kids = parse_bool(row.get("made_for_kids", "false"))
    language = row.get("language", "").strip()

    body = {
        "snippet": {
            "title": title,
            "description": description,
            "categoryId": category_id,
            "tags": tags,
        },
        "status": {
            "privacyStatus": privacy_status,
            "selfDeclaredMadeForKids": made_for_kids,
        },
    }

    if language:
        body["snippet"]["defaultLanguage"] = language
        body["snippet"]["defaultAudioLanguage"] = language

    if publish_at:
        # must be ISO8601 UTC e.g. 2026-03-02T12:00:00Z
        datetime.strptime(publish_at, "%Y-%m-%dT%H:%M:%SZ")
        body["status"]["publishAt"] = publish_at
        body["status"]["privacyStatus"] = "private"

    media = MediaFileUpload(file_path, chunksize=-1, resumable=True)
    req = youtube.videos().insert(part="snippet,status", body=body, media_body=media)

    response = None
    while response is None:
        status, response = req.next_chunk()

    video_id = response["id"]

    # thumbnail
    thumb = row.get("thumbnail_path", "").strip()
    if thumb and os.path.exists(thumb):
        youtube.thumbnails().set(videoId=video_id, media_body=MediaFileUpload(thumb)).execute()

    # playlist
    playlist_id = row.get("playlist_id", "").strip()
    if playlist_id:
        youtube.playlistItems().insert(
            part="snippet",
            body={
                "snippet": {
                    "playlistId": playlist_id,
                    "resourceId": {"kind": "youtube#video", "videoId": video_id},
                }
            },
        ).execute()

    return video_id


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", required=True, help="Queue CSV path")
    ap.add_argument("--client-secret", required=True, help="OAuth client secret json")
    ap.add_argument("--token", default="/root/.openclaw/credentials/youtube_token.json")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--auth-mode", choices=["local", "console"], default="local")
    args = ap.parse_args()

    rows = list(csv.DictReader(open(args.csv, "r", encoding="utf-8-sig")))
    if args.dry_run:
        print(f"DRY RUN: {len(rows)} rows")
        for i, r in enumerate(rows, 1):
            print(i, r.get("file_path"), r.get("title"), r.get("publish_at"))
        return

    yt = load_service(args.client_secret, args.token, args.auth_mode)

    for i, row in enumerate(rows, 1):
        try:
            vid = upload_video(yt, row)
            print(f"[{i}/{len(rows)}] OK videoId={vid} file={row.get('file_path')}")
        except Exception as e:
            print(f"[{i}/{len(rows)}] FAIL file={row.get('file_path')} err={e}")


if __name__ == "__main__":
    main()
