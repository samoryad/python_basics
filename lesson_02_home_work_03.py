month = int(input('Введите месяц от 1 до 12: '))

winter = [1, 2, 12]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
if month in winter:
    print('Это зима')
elif month in spring:
    print('Это весна')
elif month in summer:
    print('Это лето')
elif month in autumn:
    print('Это осень')

my_dict = {1: 'Это зима', 2: 'Это зима', 3: 'Это весна', 4: 'Это весна', 5: 'Это весна', 6: 'Это лето', 7: 'Это лето',
        8: 'Это лето', 9: 'Это осень', 10: 'Это осень', 11: 'Это осень', 12: 'Это зима'}
if month in my_dict:
    print(my_dict.get(month))
