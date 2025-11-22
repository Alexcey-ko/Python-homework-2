"""4. Условный оператор и булева логика."""

number = int(input('Введите число: '))
#Проверка знака
if number < 0:
    print('negative')
elif number > 0:
    print('positive')
else:
    print('zero')
#Проверка делимости на 2 и 3 одновременно
if number % 3 == 0 and number % 2 == 0:
    print(f'{number} is divisible by 3 and 2.')