import random
import pandas as pd


lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})


# Функция на проверку данных
def is_value(of: str):
    def inner(what: str) -> int:
        return 1 if what == of else 0
    return inner


# Уникальные значения что у нас есть в этом датафрейме
uniques = data['whoAmI'].unique()


# Пройдем для всех уникальных значений whoAmI в исходном датафрейме
for u in uniques:
    classificator = is_value(u)
    data[u] = data['whoAmI'].apply(classificator)


# Для порядка можно удалить whoAmI
data = data.drop('whoAmI', axis=1)


print(data)