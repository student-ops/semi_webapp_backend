import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# 環境変数からトークンを取得

# Slackクライアントを初期化

def SlackSendMessage(channel_id, message):

    token = os.getenv("SLACK_BOT_TOKEN")
    client = WebClient(token=token)
    question_dict =[]
    if message not in question_dict:
        question_dict.append(message)
    else:
        print("question already asked")
        return None
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
