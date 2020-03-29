def my_f(a, b):
    """Функция проверяет деление на 0 и выводит частное от двух чисел, округлённое до 10 знаков"""
    try:
        return round(a / b, 10)
    except ZeroDivisionError:
        print('Делить на 0 нельзя!')


while True:
    try:
        first = float(input('Введите первое число: '))
        second = float(input('Введите второе число: '))
        break
    except ValueError or TypeError:
        print("Пожалуйста введите число")
print(my_f(first, second))
