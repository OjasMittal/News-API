import requests

r = requests.get('https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2022-2-27&to=2022-2-28&sortBy=popularity&language=en&apiKey=f6fcf829fb5840cd8695085bc153b89d')
content = r.json()
print(content['articles'])