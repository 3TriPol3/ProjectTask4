from tkinter import *
from tkinter import ttk

from Controllers.TransactionController import *

class SortView(Tk):
    def __init__(self, sort_string):
        super().__init__()

        self.sort_string = sort_string  # Из строки поиска в окне TransactionView, занчение предаётся атрибуту self.sort_string

        # Атрибуты окна
        self.title("Фильтрация по категории")
        self.geometry("1280x750")

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







        # Кнопка закрытия окна / перехода в главное
        # переход на главное окно
        self.button_move = ttk.Button(self, text="Вернуться на главную страницу", command=self.move)
        self.button_move.pack(anchor=CENTER)


    # Для обновления данных в таблице создал метод добавления записей из БД
    def table(self):
        # Очистить старые записи
        for item in self.table_data.get_children(self.sort_string):
            self.table_data.delete(item)
        self.el = []
        for el in TransactionController.get():
            self.el.append((el.id, el.category, el.amount, el.type, el.date, el.description))
        # Вывод данных из БД в таблицу
        for item in self.el:
            self.table_data.insert("", END, values=item)
        self.table_data.pack()

    def row_selected(self, event):
        selected = self.table_data.selection()
        # Проверить, если строки не выбранны
        if not selected:
            return  # Завершить работу метода
        self.row = self.table_data.selection()[0]
        self.id = self.table_data.item(self.row, "values")[0]
        return self.id

    def move(self):
        from Views.TransactionView import TransactionView
        window_home = TransactionView()
        self.destroy()


if __name__ == "__main__":
    window = SortView(sort_string="")
    window.mainloop()