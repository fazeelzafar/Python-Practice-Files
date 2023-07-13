import requests
from multiprocessing.pool import ThreadPool
import time

def SendRequest(url):
    response = requests.get(url)
    print("Request to {} completed with status code: {}".format(url, response.status_code))

if __name__ == "__main__":
    url = "https://www.amazon.com/s?i=computers-intl-ship&bbn=16225007011&rh=n%3A16225007011%2Cn%3A172456&page="

    urls = [url + str(i) for i in range(1, 400+1)]

    # Start the timer
    start= time.time()

    # Create a ThreadPool with 'n' workers
    pool = ThreadPool(6)

    # Send requests in parallel
    pool.map(SendRequest, urls)

    # Close the ThreadPool and wait for the workers to finish execution
    pool.close()
    pool.join()

    # Calculate the total execution time and print it
    total_time = time.time() - start

    print(f"Execution time: {int(total_time // 60)} minutes {int(total_time % 60)} seconds")