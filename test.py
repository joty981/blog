import requests


html = requests.get('http://google.com')

print(html.text)