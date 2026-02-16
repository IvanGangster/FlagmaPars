import requests
from bs4 import BeautifulSoup
from time import sleep
import random

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/121.0.0.0 Safari/537.36",
    "Accept-Language": "ru-RU,ru;q=0.9,en;q=0.8",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9",
    "Connection": "keep-alive"}
session = requests.Session()
session.headers.update(headers)

numb_page = 1



while True:
# for count in range(1, total_pages + 14):
    sleep(random.uniform(3, 7))
    url = f"https://flagma.pl/vacancies/inzynierowie-technolodzy/page-{numb_page}/"
    response = session.get(url, timeout=10)
    if response.status_code == 403:
        print("Тебя заблокировали")
        break

    page_html = BeautifulSoup(response.text, "lxml")
    offers_html = page_html.find_all("div", class_="page-list-item container job")

    if not offers_html:
        print("Страницы закончились")
        break

    offers_name = page_html.select("h2")
    offer_url = page_html.find_all("div", class_=lambda c: c and "header" in c and "job" in c)

    # for offer in offers_name[:-2]:
    #     print(offer.get_text(strip=True))

    # for div_link in offer_url:
    #     link = div_link.find("a")["href"]
    #     print(link)
    list_of_offers_url = []

    for offer, div_link in zip(offers_name[:-2], offer_url):
        # name = offer.get_text(strip=True)
        link = div_link.find("a")["href"]
        list_of_offers_url.append(link)
        # print(name)
        # print(link)
        # print("-" * 30)
    # Через for чтобы вывести пару данных используем zip, [:-2] это не берёт последние две со страница, так как тоже содержит тег h2.`

    for url_in_offer in list_of_offers_url:
        sleep(random.uniform(2, 5))
        response = session.get(url_in_offer, timeout=10)
        if response.status_code == 403:
            print("Бан внутри вакансии")
            break

        page_html = BeautifulSoup(response.text, "lxml")
        offers_blocks = page_html.find("div", class_="desc-block")
        # nameInOffer = offers_html.find("h1").text
        # opisOffers = offers_html.find("div", id = "description").text
        if offers_blocks:
            nameInOffer = offers_blocks.find("h1").text.strip()
            opisOffers = offers_blocks.find("div", id="description").text.strip()
            print(nameInOffer)
    
    if numb_page == 2:   # тест — остановиться на 4 странице и пройдёт её тоже, а если пишем через for и count в url, то писать на одну больше
        break
    numb_page += 1
    



# def download(url):
#   resp = requests.get(url, stream=True)
#   url = url.split("/")[-1]
#   r = open("/Users/vanyaokrugin228/Desktop/imagParser/" + url, "wb")
#   for value in resp.iter_content(1024*1024):
#     r.write(value)
#   r.close()

# # headers = {"Mozilla/5.0 (platform; rv:gecko-version) Gecko/gecko-trail Firefox/firefox-version"}

# # list_card_url = [] меняем список на генератор, добавляем фун и вконце yield
    


