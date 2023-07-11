from llama_index import ListIndex, SimpleWebPageReader
from IPython.display import Markdown, display
import os
## if __name__ == "__main__"
url = "https://ja.wikipedia.org/wiki/%E3%83%A1%E3%82%A4%E3%83%B3%E3%83%9A%E3%83%BC%E3%82%B8"

documents = SimpleWebPageReader(html_to_text=True).load_data(
    #["http://paulgraham.com/worked.html"]
    [url]
)

print(documents)
