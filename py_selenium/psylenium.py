from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By


options = ChromeOptions()
options.headless = True
driver = Chrome()
driver.get('https://quotes.toscrape.com/js/')

soup = BeautifulSoup(driver.page_source, 'lxml')
print(soup)

author_element = soup.find("small", class_="author")
author_elements = soup.select('div > div > span > small')

for author in author_elements:
    print(author.text)


driver.quit()

