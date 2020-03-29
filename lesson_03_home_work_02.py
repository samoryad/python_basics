def my_data(**kwargs):
    """ Функция использует на вводе именные аргументы, а выводит строку значений через пробел"""

    a = kwargs
    a_values = a.values()
    print(' '.join(a_values))


my_data(name='Уася', surname='Пупкинс', born_year='2000', town='Москва',
        e_mail='uasya.pupkins@mail.ru', tel='89261234567')
