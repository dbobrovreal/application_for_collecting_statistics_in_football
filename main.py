import requests
import pandas
import os
from bs4 import BeautifulSoup
from openpyxl import load_workbook
from pathlib import Path


def edit_table():
    wb = load_workbook('teams.xlsx')
    ws = wb.active
    ws.delete_rows(2, 1)

    column_b = ws.column_dimensions['B']
    column_c = ws.column_dimensions['C']
    column_d = ws.column_dimensions['D']

    column_b.width = 20
    column_c.width = 20
    column_d.width = 20

    wb.save('teams.xlsx')


def writing_to_table(players, club, number_heads):
    df = pandas.DataFrame({
        "Имя игрока": players,
        "Клуб": club,
        "Гол (Пенальти)": number_heads
    })

    df.to_excel('teams.xlsx', sheet_name='Бомбардиры')


def data_collection():
    with open('static/index.html', 'r', encoding='utf-8') as file:
        text = file.read()

    soup = BeautifulSoup(text, 'lxml')
    countries = soup.find_all('span', attrs={"class": "player-name"})
    gol = soup.find_all('td', attrs={"title": "Голы (Голы с пенальти)"})

    players = ['']
    club = ['']
    number_heads = ['']

    for elem in countries:
        text = " ".join(elem.text.split()).split('/')
        players.append(text[0].rstrip())
        club.append(text[1].lstrip())

    for item in gol[1:]:
        number_heads.append(" ".join(item.text.split()))

    writing_to_table(players=players, club=club, number_heads=number_heads)


def request_execution():
    cookies = {
        'spb_abtests_index_n': '351',
        'spbc_uuid': '16b4e6ff839e10c6ae12563cc173758e',
        'getintent': '1700670911671746048',
        '_ym_uid': '1700670911671746048',
        '_ym_d': '1700670911',
        'af_lpdid': '55488:3',
        '___dmpkit___': 'e93a3acd-2374-40e6-aea5-bab87fa1506f',
        '_ga': 'GA1.2.2032607265.1700670911',
        '_gid': 'GA1.2.543736326.1700670911',
        '_gat': '1',
        '_ym_isad': '2',
        '_ym_visorc': 'b',
        'adrdel': '1',
        'adrcid': 'AM57ojAEPdq5tJ5odGov0ZQ',
        '_q_segs': '[]',
        'sp_c_comm_def_tab_active': 'spb',
        'sportbox_comments_flood': '1700670936',
        '_ga_CGK3FE78RZ': 'GS1.2.1700670911.1.1.1700670936.0.0.0',
    }

    headers = {
        'authority': 'news.sportbox.ru',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru,en;q=0.9',
        'cache-control': 'max-age=0',
        'referer': 'https://news.sportbox.ru/Vidy_sporta/Futbol/Evropejskie_chempionaty/Angliya/stats/turnir_20910',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "YaBrowser";v="23"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/116.0.5845.660 YaBrowser/23.9.5.660 Yowser/2.5 Safari/537.36',
    }
    r = requests.Session()

    response = r.get(
        'https://news.sportbox.ru/Vidy_sporta/Futbol/Evropejskie_chempionaty/Angliya/stats/turnir_20910/leaders_1',
        cookies=cookies,
        headers=headers,
    )
    path = 'static'

    if not os.path.exists(path):
        os.mkdir('static')

    with open('static/index.html', 'w', encoding='utf-8') as file:
        file.write(response.text)

    data_collection()
    edit_table()


if __name__ == '__main__':
    request_execution()

    for name_file in Path('static').iterdir():
        os.remove(f'static/{name_file.name}')
    os.rmdir('static')
