import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# 環境変数からトークンを取得
token = os.getenv("SLACK_BOT_TOKEN")

# Slackクライアントを初期化
client = WebClient(token=token)

def SlackSendMessage(channel_id, message):
    try:
        # メッセージを投稿
        response = client.chat_postMessage(
          channel=channel_id,
          text=message
        )
    except SlackApiError as e:
        # エラーメッセージをログに表示
        print(f"Got an error: {e.response['error']}")
        return None
    return response

if __name__ == "__main__":
    response = SlackSendMessage("#llama-chat", "Hello, World!")
    if response is not None:
        print("⚡️ Bolt app is running!")
    else:
        print("Something went wrong while sending the message.")
