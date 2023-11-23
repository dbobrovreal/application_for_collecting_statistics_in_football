import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror
from main import request_execution


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.request_parameters = dict()
        self.title("Football data")
        self.geometry("600x400")

        self.combo = ttk.Combobox(self, values=["Premier Liga", "La Liga", "Seria A", "Bundesliga", "Liga 1"])
        self.combo.current(0)
        self.combo.pack()

        self.selected_table = tk.IntVar()
        self.chk_table = ttk.Checkbutton(self, text='Турнирная таблица', variable=self.selected_table)

        self.selected_goleador = tk.IntVar()
        self.chk_goleador = ttk.Checkbutton(self, text='Бомбардиры', variable=self.selected_goleador)

        self.chk_table.place(x=100, y=150)
        self.chk_goleador.place(x=250, y=150)

        self.button = ttk.Button(self, text="Получить данные", command=self.on_button_click)
        self.button.pack()

    def on_button_click(self):
        selected_item = self.combo.get()

        list_tables = []

        if self.selected_table.get() == 1:
            list_tables.append('Турнирная таблица')
        if self.selected_goleador.get() == 1:
            list_tables.append('Бомбардиры')

        if not list_tables:
            showerror(title="Error", message="Вы не выбрали информацию которую хотите получить")

        request_parameters = {
            "liga": selected_item,
            'parameters': list_tables
        }

        request_execution(request_parameters)


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
