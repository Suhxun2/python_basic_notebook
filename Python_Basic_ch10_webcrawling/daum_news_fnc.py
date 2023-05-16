import requests
from bs4 import BeautifulSoup


def get_news_title_and_content(url):
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    title = doc.select("h3.tit_view")[0].get_text()
    contents = doc.select("section > p")
    content = ""
    # contents.pop(-1)
    for tag in contents:
        content = content + tag.get_text()

    return title, content
