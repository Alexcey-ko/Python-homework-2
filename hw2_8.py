"""8. Исключения"""

try:
    number = 10 / int(input('Введите число: ')) 
except ZeroDivisionError:
    print('Деление на 0')
except ValueError:
    print('Некорректный ввод')
finally:
    print('Программа завершена')