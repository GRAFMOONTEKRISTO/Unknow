import requests
from bs4 import BeautifulSoup

# url = 'https://sms-activate.org/ru'
# response = requests.get(url)
#
# if response.status_code == 200:
#     content = response.text
#     soup = BeautifulSoup(content, 'html.parser')
#     elements = soup.find_all("div", class_='choice-service__search-value')
#     for element in elements:
#         print(element.text)
# else:
#     print('Ошибка при получении страницы:', response.status_code)

from selenium import webdriver
# Путь к драйверу браузера (например, Chrome)
driver_path = '/path/to/chromedriver'
# Создание экземпляра браузера
driver = webdriver.Chrome(driver_path)
# URL страницы, которую нужно спарсить
url = 'https://sms-activate.org/ru'
# Загрузка страницы
driver.get(url)
# Поиск элементов на странице по классу
elements = driver.find_elements_by_class_name('choice-service__wrapper')
# Вывод найденных элементов
for element in elements:
    print(element.text)
# Закрытие браузера
driver.quit()