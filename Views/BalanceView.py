from tkinter import *
from tkinter import ttk

from Controllers.TransactionController import TransactionController


class BalanceView(Tk):
    def __init__(self):
        super().__init__()

        self.title("Баланс")
        self.geometry("1280x750")

        # Вычисление баланса
        self.income = 0
        self.expense = 0

        for transaction in TransactionController.get():
            if transaction.type.lower() == "доход":
                self.income += float(transaction.amount)
            elif transaction.type.lower() == "расход":
                self.expense += float(transaction.amount)

        self.balance = self.income - self.expense

        # Фрейм для отображения баланса
        self.balance_frame = ttk.Frame(self, padding=20)
        self.balance_frame.pack(anchor=CENTER)

        # Заголовок
        self.title_label = ttk.Label(
            self.balance_frame,
            text="Текущий баланс"
        )
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Доходы
        self.income_label = ttk.Label(self.balance_frame, text="Общий доход:")
        self.income_value = ttk.Label(self.balance_frame, text=f"{self.income} рублей")

        self.income_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.income_value.grid(row=1, column=1, sticky="e", padx=10, pady=5)

        # Расходы
        self.expense_label = ttk.Label(self.balance_frame, text="Общий расход")
        self.expense_value = ttk.Label(self.balance_frame, text=f"{self.expense} рублей")

        self.expense_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.expense_value.grid(row=2, column=1, sticky="e", padx=10, pady=5)

        # Баланс (итого)
        self.total_label = ttk.Label(self.balance_frame, text="Баланс")
        self.total_value = ttk.Label(
            self.balance_frame,
            text=f"{self.balance} рублей",
            foreground="green" if self.balance >= 0 else "red" # Определяет цвет текста в зависимости от значения self.balance.
        )

        self.total_label.grid(row=3, column=0, sticky="w", padx=10, pady=10)
        self.total_value.grid(row=3, column=1, sticky="e", padx=10, pady=10)

        # Кнопка закрытия окна / перехода в главное
        # переход на главное окно
        self.button_move = ttk.Button(self, text="Вернуться на главную страницу", command=self.move)
        self.button_move.pack(anchor=CENTER)

    def move(self):
        from Views.TransactionView import TransactionView
        window_home = TransactionView()
        self.destroy()


if __name__ == "__main__":
    window = BalanceView()
    window.mainloop()