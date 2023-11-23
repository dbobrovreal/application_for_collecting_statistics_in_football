import requests
import os
import json
from handler.data_collection import data_collection
from customization_table.edit_table import edit_table


def request_execution(data):
    if 'Турнирная таблица' in data.get('parameters'):
        with open('json/requests_standings.json', 'r', encoding='utf-8') as file:
            js = json.load(file)

        cookies = js.get(data.get('liga')).get('cookies')

        headers = js.get(data.get('liga')).get('headers')

        r = requests.Session()

        response = r.get(
            js.get(data.get('liga')).get('url'),
            cookies=cookies,
            headers=headers,
        )

        with open('index_liga.html', 'w', encoding='utf-8') as file:
            file.write(response.text)

        data_collection(data.get('parameters'))
        edit_table()
        os.remove('index_liga.html')

    if 'Бомбардиры' in data.get('parameters'):
        with open('json/requests_players.json', 'r', encoding='utf-8') as file:
            js = json.load(file)

        cookies = js.get(data.get('liga')).get('cookies')

        headers = js.get(data.get('liga')).get('headers')

        r = requests.Session()

        response = r.get(
            js.get(data.get('liga')).get('url'),
            cookies=cookies,
            headers=headers,
        )

        with open('index_players.html', 'w', encoding='utf-8') as file:
            file.write(response.text)

        data_collection(data.get('parameters'))
        edit_table()
        os.remove('index_players.html')
