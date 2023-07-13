import requests
import time

#Iterate through all the pages of this link (approx. 400)
url = "https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A172456&page="
urls = [url + str(i) for i in range(1, 400+1)]

#Start Timer
start = time.time()

#For Loop to send a GET request to all URLs 
for url in urls:
    r = requests.get(url)
    print(r.status_code)

#End Timer & Calculate total execution time
execution_time = time.time() - start
print(f"Execution time: {int(execution_time // 60)} minutes {int(execution_time % 60)} seconds")