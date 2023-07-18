import requests

inp = input("enter the currency you want to search: ")

resp = requests.get('https://coinmarketcap.com/currencies/'+inp)

if resp.status_code == "404":
    print("Not Found!")
else:
    print(resp.status_code)