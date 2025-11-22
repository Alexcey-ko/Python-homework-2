"""7. Циклы for и while."""

#Вывод квадратов числел от 1 до 5
for i in range(1, 6, 1):
    print(i * i)
#Ввод пароля
while ( password := input('Введите пароль: ') != '1234'):
    print('Неверный пароль')
else:
    print('Успешный вход')