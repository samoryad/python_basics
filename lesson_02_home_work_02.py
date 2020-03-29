my_list_len = int(input('Введите кол-во элементов списка: '))
my_list = []
i = 1
while i <= my_list_len:
    el = input(f'Введите {i} элемент: ')
    my_list.append(el)
    i += 1
print(my_list)

new_list = []
if len(my_list) % 2 == 0:
    while len(my_list) != 0:
        new_list.append(my_list[1])
        new_list.append(my_list[0])
        my_list = my_list[2:]
else:
    while len(my_list) != 1:
        new_list.append(my_list[1])
        new_list.append(my_list[0])
        my_list = my_list[2:]
    new_list.append(my_list[0])

print(new_list)


