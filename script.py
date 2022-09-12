import requests

# Print the version of requests
print(requests.__version__)

# Fetches the google homepage and print the status code
r = requests.get("http://google.com")
print(r.status_code)

r = requests.get("https://raw.githubusercontent.com/qasimy123/CMPUT404Lab1/main/script.py")
print(r.text)