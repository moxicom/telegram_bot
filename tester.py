import requests

res = requests.get('https://randomvideo.pythonanywhere.com/')
link = res.text.find('https:')
print(res.text)
print(res.text[link:link + 52])
