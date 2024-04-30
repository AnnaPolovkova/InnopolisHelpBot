import csv
import pandas as pd

from bs4 import BeautifulSoup
from requests import get


def get_bonuses():
    url_bonus = r"https://apply.innopolis.university/olympiad-bonus/"
    html_bonus = get(url_bonus)
    soup_bonus = BeautifulSoup(html_bonus.content.decode("utf-8"),
                               features="html.parser")

    main_bonuses = soup_bonus.find_all("span", {"class": "landing-node-text"})[
        0].text
    scholarships = soup_bonus.find_all("div", {
        "class": "mainviewport-after-block__main-subtitle"})[0].text
    header_olimps = soup_bonus.find_all("h2", {"class": "section-title"})[
        0].text

    table = soup_bonus.find_all("ul", {"class": "table__ul"})
    lis = table[0].find_all('li')

    with open("olimps.csv", 'w', encoding='utf-8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for el in lis:
            olimp = el.find_all("div", {"class": "table__olympiad"})[0].text
            status = el.find_all("div", {"class": "table__status"})[0].text
            extra = el.find_all("div", {"class": "table__extra"})[0].text
            row = [olimp, status, extra]
            writer.writerow(row)

    df = pd.read_csv('olimps.csv')
    df.to_excel("olimps.xlsx")

    return [(main_bonuses, scholarships)]