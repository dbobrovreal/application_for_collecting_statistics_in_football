from bs4 import BeautifulSoup
from customization_table.writing_to_table import writing_to_table_players, writing_to_table_tournament


def data_collection(table):
    if 'Турнирная таблица' in table:
        with open('index_liga.html', 'r', encoding='utf-8') as file:
            text = file.read()

        soup = BeautifulSoup(text, 'lxml')
        countries = soup.find_all('tr', attrs={"class": "clickable"})

        tournament_position = list()

        for elem in countries[20:40]:
            text = " ".join(elem.text.split())
            print(text)
            tournament_position.append(text)

        writing_to_table_tournament(info=tournament_position)

    if 'Бомбардиры' in table:
        with open('index_players.html', 'r', encoding='utf-8') as file:
            text = file.read()
        soup = BeautifulSoup(text, 'lxml')
        countries = soup.find_all('span', attrs={"class": "player-name", "data-team": "1123155064"})
        gol = soup.find_all('td', attrs={"title": "Голы (Голы с пенальти)"})

        position = []
        players = []
        club = []
        number_heads = []

        for index, elem in enumerate(countries):
            text = " ".join(elem.text.split()).split('/')
            players.append(text[0].rstrip())
            club.append(text[1].lstrip())
            position.append(index + 1)

        for item in gol[1:]:
            number_heads.append(" ".join(item.text.split()))

        writing_to_table_players(position=position, players=players, club=club, number_heads=number_heads)

