from requests import request
from bs4 import BeautifulSoup

ADDITIONAL_LINK = "https://innopolis.university/"


def is_doc(s: str) -> bool:
    return s[0: 7] == "/upload"


def make_file_tuple(raw_link: str) -> tuple:
    name = raw_link.split("/")[-1]
    link = ADDITIONAL_LINK + raw_link.replace(' ', '%20')
    return link, name


def get_links() -> list:
    data = request(method="GET",
                   url="https://innopolis.university/sveden/apply/",
                   ).content.decode("utf-8")

    soup = BeautifulSoup(data, "html.parser")
    links = []
    for block in soup.find_all(target='_blank'):
        raw_link = block['href']
        if is_doc(raw_link):
            links.append(make_file_tuple(raw_link))
    return links


links = get_links()
for link, name in links:
    response = request(method='GET', url=link)
    with open(name, "wb") as file:
        file.write(response.content)
