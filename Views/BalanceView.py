from tkinter import *
from tkinter import ttk

from Controllers.TransactionController import *

class BalanceView(Tk):
    def __init__(self):
        super().__init__()

        # Атрибуты окна
        self.title("Показать баланс")
        self.geometry("1280x920")






if __name__ == "__main__":
    window = BalanceView()
    window.mainloop()