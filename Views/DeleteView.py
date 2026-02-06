from tkinter import *
from tkinter import ttk

from Controllers.TransactionController import *

class DeleteView(Tk):
    def __init__(self):
        super().__init__()

        # Атрибуты окна
        self.title("Удаление транзакций")
        self.geometry("1280x920")






if __name__ == "__main__":
    window = DeleteView()
    window.mainloop()