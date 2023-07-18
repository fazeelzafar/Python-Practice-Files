import requests

url = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/market-pairs/latest?slug=xrp&start=1&limit=10&category=spot&centerType=all&sort=cmc_rank_advanced&direction=desc"

payload = {}
headers = {
  'authority': 'api.coinmarketcap.com',
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
  'cache-control': 'no-cache',
  'origin': 'https://coinmarketcap.com',
  'platform': 'web',
  'referer': 'https://coinmarketcap.com/',
  'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
  'x-request-id': '8d2f160dbb2840ab8c8a53929d4b4af4'
}

resp = requests.request("GET", url, headers=headers, data=payload)

response = resp.json()

# name = response.get('data').get('marketPairs')[0].get('marketPair')
# print(name)

for i in range(0,10):
    pairName = response.get('data').get('marketPairs')[i].get('marketPair')
    pairVolume = response.get('data').get('marketPairs')[i].get('volumeUsd')
    print("Pair Name: {}, Volume in USD: {}".format(pairName, pairVolume))
