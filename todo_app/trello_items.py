from flask import trello

def add_items():
    
    return trello.get('items')

import requests
import json

url = "https://api.trello.com/1/boards/b3L47Acw/lists"

headers = {
  "Accept": "application/json"
}

query = {
  'key': 'APIKey',
  'token': 'APIToken'
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   params=query
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))