from openpyxl import load_workbook


def edit_table():
    wb = load_workbook('teams.xlsx')
    ws = wb.active

    column_b = ws.column_dimensions['B']
    column_c = ws.column_dimensions['C']
    column_d = ws.column_dimensions['D']

    column_b.width = 20
    column_c.width = 20
    column_d.width = 20

    wb.save('teams.xlsx')
