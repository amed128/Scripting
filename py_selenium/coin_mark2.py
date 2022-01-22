from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait as W
# from selenium.webdriver.support import expected_conditions as E
from selenium.common.exceptions import NoSuchElementException


options = ChromeOptions()    #headless driver to avoid opening Chrome during scraping
options.headless = True
# wait_time = 5
driver = Chrome(options=options)
driver.get('https://coinmarketcap.com/')
# wait = W(driver, wait_time)

soup = BeautifulSoup(driver.page_source, 'lxml')
currency_data = soup.select('tbody > tr td:nth-child(3) > div > a p:nth-child(1)')
# currency_links = ['https://https://coinmarketcap.com' + link.get('href') for link in currency_data]
currency_names = [link.getText() for link in currency_data]

print(currency_names[:4])

# currency_names = ['Tether']
all_blog_links = []

for i in range(len(currency_names[:4])):
    # print(currency_names[i])
    element_click = driver.find_element(By.PARTIAL_LINK_TEXT, currency_names[i])
    # element_click = wait.until(E.presence_of_element_located(By.PARTIAL_LINK_TEXT, i))
    action = ActionChains(driver)
    action.click(element_click)
    action.perform()

    try:
        elem_hover = driver.find_element(By.CSS_SELECTOR ,'#__next > div.bywovg-1.fUzJes > div > div.sc-57oli2-0.comDeo.cmc-body-wrapper > div > div.sc-16r8icm-0.eMxKgr.container > div.n78udj-0.jskEGI > div > div.sc-16r8icm-0.hMKivi.linksSection > div > div.sc-16r8icm-0.sc-10up5z1-1.eUVvdh > ul > li:nth-child(3) > button')
        action = ActionChains(driver)
        action.move_to_element(elem_hover)
        action.perform()

        soup = BeautifulSoup(driver.page_source, 'lxml')
        blog_links = soup.select('.tippy-content a')
        links = [link.get('href') for link in blog_links]
        links = tuple(links)
        
    except NoSuchElementException: 
        soup = BeautifulSoup(driver.page_source, 'lxml')
        blog_link = soup.select('#__next > div.bywovg-1.fUzJes > div > div.sc-57oli2-0.comDeo.cmc-body-wrapper > div > div.sc-16r8icm-0.eMxKgr.container > div.n78udj-0.jskEGI > div > div.sc-16r8icm-0.hMKivi.linksSection > div > div.sc-16r8icm-0.sc-10up5z1-1.eUVvdh > ul > li:nth-child(3) > a')
        links = [link.get('href') for link in blog_link]
        links = tuple(links)

    all_blog_links.append(links)

    driver.back()
for i in all_blog_links:
    print(i)

driver.quit()

