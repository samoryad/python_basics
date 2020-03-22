user_str = input('Введите строку через пробел: ')

user_str = list(user_str.split(' '))
for i, n in enumerate(user_str):
    if len(n) < 10:
        print(i + 1, n)
    else:
        print(i + 1, n[:10])