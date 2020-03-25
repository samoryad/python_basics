def my_func(a, b, c):
    """ Функция принимает 3 числа, а выводит сумму наибольших двух из них"""

    my_list = [a, b, c]
    my_list = sum(my_list) - min(my_list)
    print(my_list)


my_func(-5, -10, 25.5)
