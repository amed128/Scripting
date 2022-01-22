# searchpypi.py  - Opens several search results.

import requests, sys, webbrowser, bs4

print('Searching...')    # display text while downloading the search result page
res = requests.get('https://pypi.org/search/?q='
+ ' '.join(sys.argv[1:]))
# 'https://google.com/search?q=' 
# 'https://pypi.org/search/?q='
res.raise_for_status()

# print(sys.argv[1:])

soup = bs4.BeautifulSoup(res.text, 'html.parser')

# print(soup)

linkElems = soup.select('.package-snippet')
# linkElems = soup.select('.LC20lb MBeuO DKV0Md')

# print(linkElems)

numOpen = min(2, len(linkElems))
for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)