my_list = [7, 5, 3, 3, 2]
print('текущий рейтинг:', my_list)

user_number = int(input('Введите новый элемент рейтинга: '))
if user_number >= 0:
    for el in my_list:
        if user_number > el:
            my_list.insert(my_list.index(el), user_number)
            print('итоговый рейтинг:', my_list)
            break
        elif user_number == el:
            my_list.insert(my_list.index(el) + 1, user_number)
            print('итоговый рейтинг:', my_list)
            break
        elif user_number < my_list[len(my_list) - 1]:
            my_list.append(user_number)
            print('итоговый рейтинг:', my_list)
            break
else:
    print('Введён отрицательный номер')
