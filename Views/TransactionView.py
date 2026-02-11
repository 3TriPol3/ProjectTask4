from tkinter import *
from tkinter import ttk

from Controllers.TransactionController import *
from Views.BalanceView import BalanceView
from Views.DeleteView import DeleteView
from Views.SortView import SortView


class TransactionView(Tk):
    def __init__(self):
        super().__init__()

        # Атрибуты окна
        self.title("Система учета финансов")
        self.geometry("1280x750")

        # Фрейм Добавить транзакцию
        self.add_frame = ttk.Frame(self, borderwidth=1, relief=SOLID, padding=[18], # Внутренние отступы фрейма
        )
        self.add_frame.pack(anchor=CENTER, fill=X, padx=10, pady=10)

        # Фрейм, в котором расположен текст Добавить Пост (Находится внутри фрейма add_frame)
        self.add_title_frame = ttk.Frame(self.add_frame, relief=SOLID, borderwidth=1, padding=[8, 10])
        self.add_title_frame.pack(anchor=CENTER, fill=X, padx=10, pady=10,)

        self.add_title = ttk.Label(self.add_title_frame, text="Добавить Транзакцию")
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

        # Таблица
        self.columns = ('id', "category", 'amount', 'type', 'date', 'description')  # Столбцы
        self.table_data = ttk.Treeview(self.table_frame, columns=self.columns, show='headings')

        # Заголовки таблицы
        self.table_data.heading('id', text="№")
        self.table_data.heading('category', text='Категория')
        self.table_data.heading('amount', text='Сумма')
        self.table_data.heading('type', text='Тип транзакции')
        self.table_data.heading('date', text='Дата транзакции')
        self.table_data.heading('description', text='Описание')
        # Для события выбора строки из таблицы вызову метод row_selected
        self.table_data.bind("<<TreeviewSelect>>", self.row_selected)
        # Превращает объекты из БД в список кортежей для таблицы
        self.table()

        # Фрейм для редактирования транзакции
        self.delete_frame = ttk.Frame(self, padding=[10])
        self.delete_frame.pack(anchor=CENTER, padx=5, pady=5)

        # Фрейм окна удаления транзакций
        self.balance_frame = ttk.Frame(self, padding=[10])
        self.balance_frame.pack(anchor=CENTER, padx=5, pady=5)

        # Фрейм окна баланса
        self.sort_frame = ttk.Frame(self, padding=[10])
        self.sort_frame.pack(anchor=CENTER, padx=5, pady=5)

        # Кнопка перехода в окно удаления транзакций
        self.button_delete = ttk.Button(self.delete_frame, text="Удаление транзакций", command=self.delete_window)
        self.button_delete.grid(row=1, column=2, padx=5, sticky="s")

        # Кнопка перехода в окно редактирования транзакций
        self.button_balance = ttk.Button(self.balance_frame, text="Показать баланс", command=self.balance_window)
        self.button_balance.grid(row=1, column=3, padx=5, sticky="s")

        # Кнопка перехода в окно сортировки транзакций
        self.button_sort = ttk.Button(self.sort_frame, text="Фильтрация транзакций", command=self.sort_window)
        self.button_sort.grid(row=1, column=4, padx=5, sticky="s")


    def delete_window(self):
        window = DeleteView()
        self.destroy()

    def sort_window(self):
        window = SortView()
        self.destroy()

    def balance_window(self):
        window = BalanceView()
        self.destroy()

    # Для обновления данных в таблице создал метод добавления записей из БД
    def table(self):
        # Очистить старые записи
        for item in self.table_data.get_children():
            self.table_data.delete(item)
        self.el = []
        for el in TransactionController.get():
            self.el.append((el.id, el.category, el.amount, el.type, el.date, el.description))
        # Вывод данных из БД в таблицу
        for item in self.el:
            self.table_data.insert("", END, values=item)
        self.table_data.pack()

    def add_data(self):
        self.category = self.add_category.get()
        self.amount = self.add_amount.get()
        self.type = self.add_type.get()
        self.date = self.add_date.get()
        self.description = self.add_description.get()
        TransactionController.add(
            self.category,
            self.amount,
            self.type,
            self.date,
            self.description
        )
        # Обновить данные таблицы Treeview
        self.table()
        # Очистить поля ввода
        self.clear()

    def clear(self):
        '''
        Метод очистит окна Treeview
        :return:
        '''
        self.add_category.delete(0, END)  # c 0-го идекса до конца
        self.add_amount.delete(0, END)  # c 0-го идекса до конца
        self.add_type.delete(0, END)  # c 0-го идекса до конца
        self.add_date.delete(0, END)  # c 0-го идекса до конца
        self.add_description.delete(0, END)  # c 0-го идекса до конца

    def row_selected(self, event):
        selected = self.table_data.selection()
        # Проверить, если строки не выбранны
        if not selected:
            return  # Завершить работу метода
        self.row = self.table_data.selection()[0]
        self.id = self.table_data.item(self.row, "values")[0]
        return self.id

if __name__ == "__main__":
    window = TransactionView()
    window.mainloop()