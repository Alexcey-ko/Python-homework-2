"""6. match/case."""

cmd = input('Введите команду: ')
match cmd:
    case 'start':
        print('Запуск')
    case 'stop':
        print('Остановка')
    case 'pause':
        print('Пауза')
    case _:
        print('Неизвестная команда')