import requests

# Send a GET request
def send_get_request(url):
    response = requests.get(url)
    return response.content, response.status_code

# Send a POST request
def send_post_request(url, data):
    response = requests.post(url, data=data)
    return response.content

# Send a PUT request
def send_put_request(url, data):
    response = requests.put(url, data=data)
    return response.content

# Send a DELETE request
def send_delete_request(url):
    response = requests.delete(url)
    return response.text

# Send a HEAD request
def send_head_request(url):
    response = requests.head(url)
    return response.headers

# Example usage
get_url = 'https://my-json-server.typicode.com'
post_url = 'https://my-json-server.typicode.com/typicode/demo/posts'
put_delete_url = 'https://my-json-server.typicode.com/typicode/demo/posts/1'


# GET request
response_text = send_get_request(get_url)
print('GET Response:', response_text)

# # POST request
# data = {'title': 'this is a test run'}
# response_text = send_post_request(post_url, data)
# print('POST Response:', response_text)

# PUT request
# data = {'title': 'this is a test PUT request'}
# response_text = send_put_request(put_delete_url, data)
# print('PUT Response:', response_text)

# # DELETE request
# response_text = send_delete_request(put_delete_url)
# print('DELETE Response:', response_text)

# # HEAD request
# response_headers = send_head_request(put_delete_url)
# print('HEAD Response Headers:', response_headers)