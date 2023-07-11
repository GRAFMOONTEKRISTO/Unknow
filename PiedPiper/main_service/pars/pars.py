import requests
from bs4 import BeautifulSoup as BS

r = requests.get("https://sbermarket.ru/metro/c/priedlozhieniia/skidki")
html = BS(r.content, "lxml")


# for el in html.select("Stores_stores__P76MM > Stores_storeWrapper__Q6wfJ"):
#     market_name = el.select("Picture_root__5uXZZ Store_sideImage__ke01c > img")
#     print(market_name[0]["alt"])

