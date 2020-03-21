my_dict_len = int(input('Введите количество интересующих позиций для анализа: '))
my_dict = dict()
my_tuple = tuple()
my_list = []
new_name = []
new_price = []
new_quant = []
new_item = []
i = 0
while i < my_dict_len:
    value_01 = input('Введите название наименования: ')
    value_02 = input('Введите цену наименования: ')
    value_03 = input('Введите количество наименования: ')
    value_04 = input('В чём измеряем: ')
    my_dict = {'название': value_01, 'цена': value_02, 'Кол-во': value_03, 'ед': value_04}
    my_tuple = (i + 1, my_dict)
    my_list.append(my_tuple)
    new_name.append(my_dict.get('название'))
    new_price.append(my_dict.get('цена'))
    new_quant.append(my_dict.get('Кол-во'))
    new_item.append(my_dict.get('ед'))
    i += 1

new_dict = {'название': new_name, 'цена': new_price, 'Кол-во': new_quant, 'ед': new_item}
print(new_dict)
