import requests
from bs4 import BeautifulSoup

# スクレーピングするURL
url = "https://ja.wikipedia.org/wiki/%E3%83%A1%E3%82%A4%E3%83%B3%E3%83%9A%E3%83%BC%E3%82%B8"
response = requests.get(url)

# レスポンスの内容を解析
soup = BeautifulSoup(response.text, "html.parser")

# body要素内のテキストを抽出
body_text = soup.body.get_text()

# 本文の表示
print(body_text)