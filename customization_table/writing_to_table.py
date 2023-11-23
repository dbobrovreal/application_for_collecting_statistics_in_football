import pandas


def writing_to_table_players(position, players, club, number_heads):
    df = pandas.DataFrame({
        "№": position,
        "Имя игрока": players,
        "Клуб": club,
        "Гол (Пенальти)": number_heads
    })

    df.to_excel('teams.xlsx', sheet_name='Бомбардиры', index=False)


def writing_to_table_tournament(info):
    print(info)
    # df = pandas.DataFrame({
    #     "Позиция": info[0],
    #     "Клуб": info[1],
    #     "Игр": info[2]
    # })
    #
    # df.to_excel('Turnir.xlsx', sheet_name='Турнирная таблица')
