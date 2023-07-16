import requests
from bs4 import BeautifulSoup
from bs4.element import Comment
from urllib.parse import urljoin
from urllib.parse import urlparse
# Set the base URL
base_url = "https://sun.ac.jp/"
# Set the maximum depth for crawling
max_depth = 2
# List to store the extracted URLs
count = 0
extracted_urls = []
def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True
def extract_text(html):
    soup = BeautifulSoup(html, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return u" ".join(t.strip() for t in visible_texts)
def crawl_url(url, depth):
    global count
    if depth > max_depth:
        return
    try:
        response = requests.get(url)
        html = response.content
        text = extract_text(html)
        count+=1
        print(f"Total links found: {count}")
        print(f"URL: {url}")
        print(f"Text: {text}\n")
        extracted_urls.append(url)
        soup = BeautifulSoup(html, 'html.parser')
        links = soup.find_all('a')
        for link in links:
            href = link.get('href')
            if href is None or href == "":
                continue
            if href.startswith('/') or base_url in href:
                absolute_url = urljoin(base_url, href)
                if absolute_url not in extracted_urls:
                    crawl_url(absolute_url, depth + 1)
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while crawling URL: {url}")
        print(f"Error details: {e}\n")
def crawl_single_url(url):
    try:
        response = requests.get(url)
        html = response.content
        text = extract_text(html)
        print(f"Total links found: {count}")
        print(f"URL: {url}")
        print(f"Text: {text}\n")
        file_contents = "URL: \n" + url + "\n" + "Text: \n" + text + "\n"
    except requests.exceptions.RequestException as e:
            print(f"Error occurred while crawling URL: {url}")
            print(f"Error details: {e}\n")
    
    parsed_url = urlparse(url)
    file_name = parsed_url.path.strip("/").replace("/", "_") + ".txt"

    with open(f"{file_path}/{file_name}", "a") as f:
        f.write(file_contents)

    
# Start crawling from the base URL
file_path = "./data/faculty"
file_path = "./data/research"
# crawl_url(base_url, 0)
# crawl_single_url("https://sun.ac.jp/department/systems/systems/")
url_list_f = [
    "https://sun.ac.jp/department/systems/systems/",
    "https://sun.ac.jp/department/systems/systems/",
    "https://sun.ac.jp/entrance/features/",
    "https://sun.ac.jp/entrance/aboutnagasaki/",
    "https://sun.ac.jp/department/systems/systems/",
    "https://sun.ac.jp/campus/siebold/",
    "https://sun.ac.jp/student/life/calendar/",
    "https://sun.ac.jp/student/fee/#block30280",
    "https://sun.ac.jp/guide/purpose/",
    "https://sun.ac.jp/student/life/club/siebold/ "
]

url_list_r=[
    "https://coincheck.com/ja/article/497#:~:text=%E3%82%B8%E3%82%A7%E3%83%8D%E3%83%A9%E3%83%86%[…]%E3%81%8C%E3%81%82%E3%82%8A%E3%81%BE%E3%81%99%E3%80%82",
    "https://koikeganka.com/news/oshirase/other/2753",
    "https://blog.studiofruitjam.com/2017/04/07/fermat-spiral/",
    "https://kotobank.jp/word/%E3%83%96%E3%82%A4-122550#:~:text=%E6%97%A5%E6%9C%AC%E5%A4%A7%E7%99%BE%E7[…]A8%E3%81%84%E3%82%89%E3%82%8C%E3%82%8B%E3%80%82",
    "https://www.kyocera.co.jp/smartcity/energy_harvesting_smart_buoy/",
    "https://easel5.com/technical-guide/about-lora/#:~:text=LoRa%20%E3%81%AF%20LPWA%20(Low%20Power,%E[…]1%8C%E5%8F%AF%E8%83%BD%E3%81%A7%E3%81%99%E3%80%82",
    "https://www.keyence.co.jp/ss/general/iot-glossary/edge.jsp#:~:text=%E3%82%A8%E3%83%83%E3%82%B8%EF%BC%8[…]3%81%84%E3%81%84%E3%81%BE%E3%81%99%E3%80%82",
    "https://www.keyence.co.jp/ss/general/iot-glossary/gateway.jsp",
    "https://agirobots.com/esp32-introduction/",
    "https://it-trend.jp/database/article/89-0056",
    "https://openstandia.jp/oss_info/influxdb/",
    "https://openstandia.jp/oss_info/grafana/"
]

file_path = "./data/faculty"
for url in url_list_f:
    crawl_single_url(url)
file_path = "./data/research"
for  url in url_list_r:
    crawl_single_url(url)