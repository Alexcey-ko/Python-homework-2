"""10. Дополнительно"""

#Проверка числа с помощью тернарного оператора
try:
    number = int(input('Введите число: ')) 

    print(f'{'even' if number % 2 == 0 else 'odd'}')
except ZeroDivisionError:
    print('Деление на 0')
except ValueError as e:
    print(e)

#Проверка вводимой строки на число
try:
    if number := float(input('Ввод: ')):
        print('Это число')
except ValueError:
    print('Это не число')