import requests

# Print the version of requests
print(requests.__version__)

# Fetches the google homepage and print the status code
r = requests.get("http://google.com")
print(r.status_code)

r = requests.get("https://gist.githubusercontent.com/qasimy123/2ae16c2de74725cb2d0d947ed5d96164/raw/downloaditself.py")
print(r.text)