from requests import request
from bs4 import BeautifulSoup


def get_links() -> dict:
    data = request(method="GET",
                   url="https://apply.innopolis.university/faq/",
                   ).content.decode("utf-8")

    soup = BeautifulSoup(data, "html.parser")

    questions = []
    answers = []

    for block in soup.find_all(class_="expand-panel__header-title"):
        questions.append(block.text)

    for block in soup.find_all(class_="expand-panel__body collapse"):
        answers.append(block.text)

    faqs = dict(zip(questions, answers))

    return list(faqs.items())