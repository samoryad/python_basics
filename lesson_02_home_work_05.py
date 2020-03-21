my_list = [7, 5, 3, 3, 2]

user_number = int(input('Введите номер рейтинга: '))
if user_number >= 0:
    for el in my_list:
        if user_number > el:
            my_list.insert(my_list.index(el), user_number)
            print(my_list)
            break
        elif user_number == el:
            my_list.insert(my_list.index(el) + 1, user_number)
            print(my_list)
            break
        elif user_number < my_list[len(my_list) - 1]:
            my_list.append(user_number)
            print(my_list)
            break
else:
    print('Введён отрицательный номер')
