#webscraping

import requests, bs4 

def getSoup(link):
    try:
        dataFromSite = requests.get(link)
        soup = bs4.BeautifulSoup(dataFromSite.text, 'lxml')
    except Exception as exc:
        print('There was a problem: %s' % (exc))
    
    return soup

soup = getSoup('https://opensea.io')
# soup = getSoup('https://librivox.org') #search embedded pages
# soup = getSoup('https://quotes.toscrape.com/js/') #dynamic
# soup = getSoup('https://google.com')
# element = soup.select('#gbqfbb')

# # print(element)
# for i in element:
#     print(i.text)

#FETCH EVERY CURRENCY LINK
currency_data = soup.select('#main > div > div > div > div:nth-child(2) > div:nth-child(11) > a > div > div > div > span > div')
# currency_links = ['https://https://coinmarketcap.com' + link.get('href') for link in currency_data]
# currency_names = [link.getText() for link in currency_data]
# print(currency_data)


print(currency_data)








'''

from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
import requests

# options = ChromeOptions()    #headless driver to avoid opening Chrome during scraping
# options.headless = True
# driver = Chrome(options=options)
# driver.get('https://coinmarketcap.com/')

def getSoup(link):
    try:
        dataFromSite = requests.get(link)
        soup = BeautifulSoup(dataFromSite.text, 'lxml')
    except Exception as exc:
        print('There was a problem: %s' % (exc))
    
    return soup


soup = getSoup('https://coinmarketcap.com/')
# soup = BeautifulSoup(driver.page_source, 'lxml')
link_elements = soup.select('tbody > tr td:nth-child(3) > div > a')
currency_links = ['https://https://coinmarketcap.com' + link.get('href') for link in link_elements]

print(currency_links[0])

# PROCESSING EVERY LINK
all_blog_links = []

link = currency_links[0]
link = "'"+link+"'"
# print(link)

# for link in currency_links[:2]:
options = ChromeOptions()    #headless driver to avoid opening Chrome during scraping
options.headless = True
driver = Chrome(options=options)
driver.get('https://https://coinmarketcap.com/currencies/bitcoin/')
# soup = BeautifulSoup(driver.page_source, 'lxml')
# blog_link = soup.select('#__next > div.bywovg-1.fUzJes > div > div.sc-57oli2-0.comDeo.cmc-body-wrapper > div > div.sc-16r8icm-0.eMxKgr.container > div.n78udj-0.jskEGI > div > div.sc-16r8icm-0.hMKivi.linksSection > div > div.sc-16r8icm-0.sc-10up5z1-1.eUVvdh > ul > li:nth-child(3) > a')
# links = [link.get('href') for link in blog_link]

elem_hover = driver.find_element_by_css_selector('#__next > div.bywovg-1.fUzJes > div > div.sc-57oli2-0.comDeo.cmc-body-wrapper > div > div.sc-16r8icm-0.eMxKgr.container > div.n78udj-0.jskEGI > div > div.sc-16r8icm-0.hMKivi.linksSection > div > div.sc-16r8icm-0.sc-10up5z1-1.eUVvdh > ul > li:nth-child(3) > button')
action = ActionChains(driver)
action.move_to_element(elem_hover)
action.perform()

soup = BeautifulSoup(driver.page_source, 'lxml')
blog_links = soup.select('.tippy-content a')
links = [link.get('href') for link in blog_links]

# # for author in author_elements:
# #     print(author.text)
# pass
all_blog_links.extend(links)

print(all_blog_links)

driver.quit()

'''
# second code

'''
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

list_links = ['bitcoin','ethereum']

options = ChromeOptions()    #headless driver to avoid opening Chrome during scraping
options.headless = True

# driver = Chrome()
driver = Chrome(options=options)
driver.get('https://https://coinmarketcap.com/')

for i in range(len(list_links)):
    # find element to click on
    elem_click = driver.find_element(By.PARTIAL_LINK_TEXT, list_links[i])
    action = ActionChains(driver)
    action.click(elem_click)
    action.perform()

    elem_hover = driver.find_element(By.CSS_SELECTOR, '#__next > div.bywovg-1.fUzJes > div > div.sc-57oli2-0.comDeo.cmc-body-wrapper > div > div.sc-16r8icm-0.eMxKgr.container > div.n78udj-0.jskEGI > div > div.sc-16r8icm-0.hMKivi.linksSection > div > div.sc-16r8icm-0.sc-10up5z1-1.eUVvdh > ul > li:nth-child(3) > button')
    # action = ActionChains(driver)
    action.move_to_element(elem_hover)
    action.perform()

    soup = BeautifulSoup(driver.page_source, 'lxml')
    blog_links = soup.select('.tippy-content a')
    links = [link.get('href') for link in blog_links]

    # blog_link = soup.select('#__next > div.bywovg-1.fUzJes > div > div.sc-57oli2-0.comDeo.cmc-body-wrapper > div > div.sc-16r8icm-0.eMxKgr.container > div.n78udj-0.jskEGI > div > div.sc-16r8icm-0.hMKivi.linksSection > div > div.sc-16r8icm-0.sc-10up5z1-1.eUVvdh > ul > li:nth-child(3) > a')
    # links = [link.get('href') for link in blog_link]
    # for author in author_elements:
    #     print(author.text)

    print(links)

driver.quit()


'''