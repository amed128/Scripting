import requests

# res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

try:
    res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
    # res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))

# print(type(res))
# print(len(res.text))
# print(res.text[:250])

playFile = open('RomeoAndJuliet.txt', 'wb')

for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()