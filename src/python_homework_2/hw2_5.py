"""5. Операции сравнения."""

x = float(input('Введите число: '))
#Проверка вхождения числа в диапазон
if 10 <= x <= 20:
    print(f'{x} in [10, 20]')
#Проверка на None
x = None
if x is None:
    print('x is None')