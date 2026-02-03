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

if __name__ == "__main__":


