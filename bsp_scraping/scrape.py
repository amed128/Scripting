import requests, bs4
'''
### if we want to retrieve data from a file

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile,'lxml')                               # 'html.parser')
# 'lxml' is faster as a parser than 'html.parser'

# print(type(exampleSoup))

parsed1 = exampleSoup.select('div span')
parsed2 = exampleSoup.select('div > span')
print(parsed1)
print(parsed2)   '''

#### if we want to retrieve data from a website

try:
    dataFromSite = requests.get('https://nostarch.com')
    soup = bs4.BeautifulSoup(dataFromSite.text, 'lxml')
except Exception as exc:
    print('There was a problem: %s' % (exc))

data1 = soup.select('input[name]')  #all 'input' elements that have the attribute 'name' in its attributes
data2 = soup.select('input[type="button"]')

data3 = soup.select('#topics span a')
alltopics = [data.getText() for data in data3]   #getText() to get text inside html tags

# print(data1[0])
# print(data2)
print(alltopics)
print(data3[0].attrs) #print all attributes of the selected tags