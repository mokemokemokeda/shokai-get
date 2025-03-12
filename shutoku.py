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

# APIリクエストのヘッダー
headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}",
}

# @jeleechandayo のユーザーIDを取得
url_user = f"https://api.twitter.com/2/users/by/username/{USERNAME}"
response_user = requests.get(url_user, headers=headers)
user_data = response_user.json()

if response_user.status_code == 200:
    user_id = user_data["data"]["id"]
    print(f"User ID: {user_id}")
else:
    print(f"Error fetching user ID: {response_user.status_code}")
    print("Response:", user_data)
    exit(1)

# フォロワー取得（1人だけ）
url_followers = f"https://api.twitter.com/2/users/{user_id}/followers?max_results=1"
response_followers = requests.get(url_followers, headers=headers)
followers_data = response_followers.json()

if response_followers.status_code == 200 and "data" in followers_data:
    follower = followers_data["data"][0]  # 1人目のフォロワー
    follower_id = follower["id"]
    follower_name = follower["name"]
    follower_username = follower["username"]
    print(f"Follower: {follower_name} (@{follower_username})")

    # フォロワーの自己紹介を取得
    follower_bio = follower.get("description", "No bio available.")
    print(f"Follower Bio: {follower_bio}")

else:
    print(f"Error fetching followers: {response_followers.status_code}")
    print("Response:", followers_data)
