from flask import trello
import requests
import json


class Item:
    def __init__(self, id, name, status = 'To Do'):
        self.id = id
        self.name = name
        self.status = status
    @classmethod
    def from_trello_card(cls, card, list):
        return cls(card['id'], card['name'], list['name'])


def add_items():
    
    return trello.get('items')

def get_item(id):

    item = Item.from_trello_card(list)

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