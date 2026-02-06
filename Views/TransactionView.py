from tkinter import *
from tkinter import ttk

from Controllers.TransactionController import *

class TransactionView(Tk):
    def __init__(self):
        super().__init__()

        # Атрибуты окна
        self.title("Система учета финансов")
        self.geometry("1280x920")

        # Фрейм Добавить транзакцию
        self.add_frame = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[18], # Внутренние отступы фрейма
        )
        self.add_frame.pack(anchor=CENTER, fill=X, padx=10, pady=10)

        # Фрейм, в котором расположен текст Добавить Пост (Находится внутри фрейма add_frame)
        self.add_title_frame = ttk.Frame(self.add_frame, relief=SOLID, borderwidth=1, padding=[8, 10])
        self.add_title_frame.pack(anchor=CENTER, fill=X, padx=10, pady=10,)

        self.add_title = ttk.Label(self.add_title_frame, text="Добавить пост")
        self.add_title.pack()

        # Фрейм в котором расположены окна ввода данных о Транзакциях (Находится внутри фрейма add_frame)
        self.add_input_frame = ttk.Frame(self.add_frame, relief=SOLID, borderwidth=1, padding=[8, 10])
        self.add_input_frame.pack(fill=X, padx=10, pady=10)

        # Окна ввода данных записи Транзакции для добавления в таблицу БД
        self.add_title_category = ttk.Label(self.add_input_frame, text="Категория")
        self.add_title_category.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        self.add_title_amount = ttk.Label(self.add_input_frame, text="Сумма")
        self.add_title_amount.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        self.add_title_type = ttk.Label(self.add_input_frame, text="Тип транзакции")
        self.add_title_type.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)

        self.add_title_date = ttk.Label(self.add_input_frame, text="Дата транзакции")
        self.add_title_date.grid(row=0, column=3, sticky="nsew", padx=5, pady=5)

        self.add_title_description = ttk.Label(self.add_input_frame, text="Описание")
        self.add_title_description.grid(row=0, column=4, sticky="nsew", padx=5, pady=5)


        self.add_category = ttk.Entry(self.add_input_frame)
        self.add_category.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        self.add_amount = ttk.Entry(self.add_input_frame)
        self.add_amount.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

        self.add_type = ttk.Entry(self.add_input_frame)
        self.add_type.grid(row=1, column=2, sticky="nsew", padx=5, pady=5)

        self.add_date = ttk.Entry(self.add_input_frame)
        self.add_date.grid(row=1, column=3, sticky="nsew", padx=5, pady=5)

        self.add_description = ttk.Entry(self.add_input_frame)
        self.add_description.grid(row=1, column=4, sticky="nsew", padx=5, pady=5)

        # Кнопка добавления транзакции
        self.add_button = ttk.Button(self.add_input_frame, text="Добавить транзакцию", command=self.add_data)
        self.add_button.grid(row=1, column=5, sticky="nsew", padx=5, pady=5)

        # Фрейм Вывод Транзакций
        self.get_data = ttk.Frame(self, relief="raised", borderwidth=3, padding=[5])
        self.get_data.pack(anchor=CENTER)

        # Фрейм Таблицы
        self.table_frame = ttk.Frame(self, padding=[20])
        self.table_frame.pack(anchor=CENTER, pady=10, padx=10)