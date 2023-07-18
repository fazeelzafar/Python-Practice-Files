import requests
import json

url = "https://www.kaggle.com/api/i/datasets.DatasetService/GetLandingPageTopics"

payload = json.dumps({})
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0',
  'Accept': 'application/json',
  'Accept-Language': 'en-US,en;q=0.5',
  'Accept-Encoding': 'gzip, deflate, br',
  'Referer': 'https://www.kaggle.com/datasets',
  'content-type': 'application/json',
  'x-xsrf-token': 'CfDJ8MCGpmbK0d9IuUUyozUQ8_lL835a6RM9P3KaF-etEF4rJ1GJ3lp6O-JdmaxnXdiH9aVyj_To1uPCnRqIzqVbnoV-t8D0nUaS7EkhPRBQ02SfTw',
  'Origin': 'https://www.kaggle.com',
  'Alt-Used': 'www.kaggle.com',
  'Connection': 'keep-alive',
  'Cookie': '_ga=GA1.1.1218272798.1672934575; _ga_T7QHS60L4Q=GS1.1.1689636053.13.1.1689636074.0.0.0; ACCEPTED_COOKIES=true; ka_sessionid=427da97ba871ac54901c87e25adce01e; CSRF-TOKEN=CfDJ8MCGpmbK0d9IuUUyozUQ8_nfs2iRUHQG5Wl4SH15v9atFNr9bZ69O0BQqJzq5sz0ZW6UNKyIsz9YUElTftW3TaBBECgpCya05uv1j5vzRg; XSRF-TOKEN=CfDJ8MCGpmbK0d9IuUUyozUQ8_lL835a6RM9P3KaF-etEF4rJ1GJ3lp6O-JdmaxnXdiH9aVyj_To1uPCnRqIzqVbnoV-t8D0nUaS7EkhPRBQ02SfTw; CLIENT-TOKEN=eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJpc3MiOiJrYWdnbGUiLCJhdWQiOiJjbGllbnQiLCJzdWIiOm51bGwsIm5idCI6IjIwMjMtMDctMTdUMjM6MjE6MDkuNTAwNjYzNFoiLCJpYXQiOiIyMDIzLTA3LTE3VDIzOjIxOjA5LjUwMDY2MzRaIiwianRpIjoiZGRmZTBiODYtNjM2My00MDZkLTllODYtOWVjZTJkNDBhNmQwIiwiZXhwIjoiMjAyMy0wOC0xN1QyMzoyMTowOS41MDA2NjM0WiIsImFub24iOnRydWUsImZmIjpbIktlcm5lbHNGaXJlYmFzZUxvbmdQb2xsaW5nIiwiQ29tbXVuaXR5TG93ZXJIZWFkZXJTaXplcyIsIkFsbG93Rm9ydW1BdHRhY2htZW50cyIsIkZvcmNlTmF2Rm9vdGVyT25Nb2JpbGVBbmRUYWJsZXQiLCJGcm9udGVuZEVycm9yUmVwb3J0aW5nIiwiQ29tcGV0aXRpb25zUHl0aG9uTWV0cmljcyIsIkRhdGFzZXRzTWFuYWdlZEZvY3VzT25PcGVuIiwiRG9pRGF0YXNldFRvbWJzdG9uZXMiLCJDaGFuZ2VEYXRhc2V0T3duZXJzaGlwVG9PcmciLCJLZXJuZWxFZGl0b3JIYW5kbGVNb3VudE9uY2UiLCJQYWdlVmlzaWJpbGl0eUFuYWx5dGljc1JlcG9ydGVyIiwiTWF1UmVwb3J0IiwiTW9kZWxzQ2FjaGVkVGFnU2VydmljZUVuYWJsZWQiLCJDb21wZXRpdGlvbnNSdWxlc0ttIiwiRGF0YXNldHNTaGFyZWRXaXRoVGhlbVNlYXJjaCIsIkRhdGFzZXRzVm90aW5nQ2hpcHMiLCJUYWdzTWVudVNsaWRlclBhbmVsIiwiTW9kZWxJbnN0YW5jZVJlbmRlcmVkVXNhZ2UiLCJSZWNlbnRseVZpZXdlZE1vZGVsc1NoZWxmIiwiS21FbW9qaVBpY2tlciJdLCJmZmQiOnsiS2VybmVsRWRpdG9yQXV0b3NhdmVUaHJvdHRsZU1zIjoiMzAwMDAiLCJGcm9udGVuZEVycm9yUmVwb3J0aW5nU2FtcGxlUmF0ZSI6IjAiLCJFbWVyZ2VuY3lBbGVydEJhbm5lciI6Int9IiwiQ2xpZW50UnBjUmF0ZUxpbWl0IjoiNDAiLCJGZWF0dXJlZENvbW11bml0eUNvbXBldGl0aW9ucyI6IjM1MzI1LDM3MTc0LDMzNTc5LDM3ODk4LDM3MzU0LDM3OTU5LDM4ODYwIiwiQWRkRmVhdHVyZUZsYWdzVG9QYWdlTG9hZFRhZyI6ImRpc2FibGVkIiwiQ29tcGV0aXRpb25NZXRyaWNUaW1lb3V0TWludXRlcyI6IjMwIn0sInBpZCI6ImthZ2dsZS0xNjE2MDciLCJzdmMiOiJ3ZWItZmUiLCJzZGFrIjoiQUl6YVN5QTRlTnFVZFJSc2tKc0NaV1Z6LXFMNjU1WGE1SkVNcmVFIiwiYmxkIjoiOTBjNDUwYTczOWEwNzVjZmI3NzRkNjUxZWMzYTY2MmIyZjYwZDAyNCJ9.; GCLB=CLCFiZrjtoaGCQ',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'TE': 'trailers'
}

response = requests.request("POST", url, headers=headers, data=payload)

resp = response.json()

for i in range(0,7):
  topicTypes = resp.get('topics')[i].get('topicType')
  dsetCreator = resp.get('topics')[i].get('datasets')[0].get('creatorName')
  print("Topic Names: {}, Top Dataset Creator: {} \n".format(topicTypes, dsetCreator))