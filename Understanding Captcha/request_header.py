import requests

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0'}

url = 'https://www.zenrows.com/blog/web-scraping-headers#why-are-http-headers-important'

response = requests.get(url, headers=headers)

print(response.headers)