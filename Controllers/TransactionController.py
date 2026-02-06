from  Models.Transaction import *

class TransactionController:
    '''
    добавить транзакцию,
    показать баланс,
    фильтровать по категориям.
    '''

    # Добавить транзакцию
    @classmethod
    def add(cls, category, amount, type, date, description):
        try:
            Transaction.create(
            category = category,
            amount = amount,
            type = type,
            date = date,
            description = description
            )
        except:
            print("Ошибка добавления транзакции")

    # Выводит список записей из таблицы БД
    @classmethod
    def get(cls):
        return Transaction.select()

    # Редактирование
    @classmethod
    def update(cls, id, **kwargs):
        Transaction.update(**kwargs).where(Transaction.id == id).execute()

    # Удалить пост по - id
    @classmethod
    def delete(cls, id):
        Transaction.delete_by_id(id)

    # Найти(фильтровать) транзакцию по категории - category
    @classmethod
    def get_category(cls, category):
        return Transaction.select().where(Transaction.category == category)

    # # Показать баланс
    # @classmethod
    # def get_balance(cls, category):


if __name__ == "__main__":
    # TransactionController.add(  # Добавить транзакцию в таблицу
    #     category="Зарплата",
    #     amount=60000.00,
    #     type="Доход",
    #     date="2024-04-05",
    #     description="Зарплата за март"
    # )

    # TransactionController.update(1, category='Авто') # Редактирование транзакции

    for item in TransactionController.get():  # Выводит список записей из таблицы БД
        print(item.category, item.amount, item.type, item.date, item.description)

    # TransactionController.delete(4) # Удалить транзакцию по - id

    for item in TransactionController.get_category('Продукты'):  # Фильтрация по категории
        print(item.id, item.category, item.amount, item.type, item.date, item.description)


