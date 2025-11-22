"""Модуль с функциями hello и add для импорта."""

def hello():
    """Приветсвие из модуля."""
    if __name__ == '__main__':
        print('Hello from module')

def add(a, b):
    """Сумма чисел."""
    return a + b

hello()