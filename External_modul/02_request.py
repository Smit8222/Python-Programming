import requests

r = requests.get('https://www.baidu.com')

with open('baidu.html', 'w', encoding='utf-8') as f:
    f.write(r.text)