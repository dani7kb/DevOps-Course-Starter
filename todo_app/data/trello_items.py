import os
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
    #pass

    # url = "https://api.trello.com/1/boards/b3L47Acw/lists"

    # headers = {
    #   "Accept": "application/json"
    # }

    # query = {
    #   'key': os.getenv('API_KEY'),
    #   'token': os.getenv('API_TOKEN'),
    #   'cards': 'open'
      
    # }

    # response = requests.request(
    #   "POST",
    #   url,
    #   headers=headers,
    #   params=query
    # )

    # response_json = response.json()

    # cards = []
    # for trello_list in response_json:
    #     for card in trello_list['cards']:
    #         item = Item.from_trello_card(card, trello_list)
    #         cards.append(item)

    
    # return card

def get_items():

    
    url = "https://api.trello.com/1/boards/b3L47Acw/lists"

    headers = {
      "Accept": "application/json"
    }

    query = {
      'key': os.getenv('API_KEY'),
      'token': os.getenv('API_TOKEN'),
      'cards': 'open'
      
    }

    response = requests.request(
      "GET",
      url,
      headers=headers,
      params=query
    )

    response_json = response.json()

    cards = []
    for trello_list in response_json:
        for card in trello_list['cards']:
            item = Item.from_trello_card(card, trello_list)
            cards.append(item)

    print(cards)

    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

    return cards