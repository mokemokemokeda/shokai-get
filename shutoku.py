import os
import requests

# GitHub Secrets から BEARER_TOKEN を取得
BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

# BEARER_TOKEN がない場合はエラー
if not BEARER_TOKEN:
    print("Error: BEARER_TOKEN is missing. Check your GitHub Secrets settings.")
    exit(1)

# 取得したいTwitterユーザーのスクリーンネーム
USERNAME = "jeleechandayo"

# Twitter API のエンドポイント（自己紹介文を取得）
url = f"https://api.twitter.com/2/users/by/username/{USERNAME}?user.fields=description"

# APIリクエストのヘッダー
headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}",
}

try:
    response = requests.get(url, headers=headers)
    response_json = response.json()

    if response.status_code == 200:
        user_data = response_json.get("data", {})
        bio = user_data.get("description", "No bio available")
        print(f"User Bio: {bio}")
    else:
        print(f"Error: HTTP {response.status_code}")
        print("Response:", response_json)  # エラーメッセージを表示

except Exception as e:
    print("Error:", str(e))  # 例外の詳細を表示
