import requests
import json

response = requests.get('https://api.github.com/users/samuelluzsantana')

print(response.json())