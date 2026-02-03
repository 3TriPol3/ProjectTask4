from Models.Base import *

class Transaction(BaseModel):
    '''
    Данный класс описывает таблицу в БД с финансами
    '''
    id = PrimaryKeyField() # id
    category = CharField(unique=True) # Категория дохода/расхода
    amount = FloatField() # Количество (денег)
    type = CharField() # Тип дохода/расхода
    date = DateField() # Дата дохода/расхода
    description = CharField() # Описание дохода/расхода

if __name__ == "__main__":
    mysql_db.create_tables([Transaction])