import requests

try:

    url = "https://text-translator2.p.rapidapi.com/translate"

    headers = {
      
        "X-RapidAPI-Key": "023bedbb10mshb81fb9c9cadfd9dp1bddaejsnc77e3257a5f8",
        "X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
    }

    data = {
        "source_language": "en",
        "target_language": "ur",
        "text": "Good night"
    }

    response = requests.post(url, data=data, headers=headers)


    if response.status_code == 200:
        print(response.json())

    else:
        print("Error: ", requests.status_codes)

except KeyError as e:
    print("Key Error:", e)

except Exception as e:
    print("Unexpected Error Occured!", e)
