import requests

proxy = '140.238.245.116:8100'

try:
    r = requests.get('https://www.dentalcity.com/', proxies={'http':proxy, 'https':proxy}, timeout=10)
    print(r.text)
except:
    print('Request Failed!')
    pass
