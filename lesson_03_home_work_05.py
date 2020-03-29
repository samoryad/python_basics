total = 0
while True:
    my_str = input('Введите несколько чисел через пробел и нажмите "enter". Для выхода нажмите "Q".\n - ').split()
    if my_str.count('Q') or my_str.count('q') == 0:
        for el in my_str:
            total += float(el)
        print('сумма', total)
    elif my_str.count('Q') or my_str.count('q') == 1:
        my_str = my_str[:(len(my_str) - 1)]
        for el in my_str:
            total += float(el)
        print('итого:', total)
        break
