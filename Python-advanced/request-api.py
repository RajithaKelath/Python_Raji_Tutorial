#The requests module allows you to send HTTP requests using Python.
#The HTTP request returns a Response Object with all the response data (content, encoding, status, etc).

import requests
import json

x = requests.get('https://w3schools.com/python/demopage.htm')

print(x.text)