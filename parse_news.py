from pprint import pprint

from requests import request
from bs4 import BeautifulSoup

ADDITIONAL_LINK = "https://innopolis.university"


def is_success_story(s: str) -> bool:
    if s is None:
        return False
    return s[:16] == "/success-stories"


def make_story_link(raw_link: str) -> str:
    link = ADDITIONAL_LINK + raw_link
    return link


def get_name(url: str) -> str:
    response = request(method="GET", url=url).content.decode('utf-8')

    soup = BeautifulSoup(response, "html.parser")

    name = "None"
    for block in soup.find_all(class_='history-title'):
        name = block.text

    return name


def get_links2():
    data = request(method="GET",
                   url="https://apply.innopolis.university/",
                   ).content.decode("utf-8")

    soup = BeautifulSoup(data, "html.parser")

    titles = []
    links = []

    for block in soup.find_all(class_="uni-main__news-bottom-title"):
        titles.append(block.text)

    for block in soup.find_all(class_="uni-main__news-bottom news-item"):
        link = block.get('href')
        links.append(link)

    news = dict(zip(titles, links))

    return list(news.items())