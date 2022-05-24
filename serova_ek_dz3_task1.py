"""
Задание 1.
Реализуйте функции:
ВНИМАНИЕ: в задании три пункта
НУЖНО выполнить каждый пункт
обязательно отделяя каждый пункт друг от друга
Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""

import time


def time_of_function(function):
    def wrapped(*args):
        start_time = time.perf_counter()
        res = function(*args)
        print(time.perf_counter() - start_time)
        return res
    return wrapped

# task a
'''a) заполнение списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   заполнение словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени'''


@time_of_function
def add_list():
    new_list = []
    for i in range(10):
        new_list.append(i)
    return new_list


@time_of_function
def add_dictionary():
    my_dict = dict()
    for x in range(10):
        my_dict[x] = x
    return my_dict


print(add_list())
print(add_dictionary())

'''Вывод: словарь заполняется быстрее и имеет сложность
0(1) т.к реализован как хэш-таблица. Сложность списка О(n)'''

# task b
'''b) получение элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   получение элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени'''


@time_of_function
def get_list_element():
    new_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    i = 0
    while i < len(new_list):
        print(new_list[i])
        i = i+1
    return new_list


@time_of_function
def get_dictionary():
    my_dict = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}
    for value in my_dict.values():
        print(value)
    return my_dict


get_list_element()
get_dictionary()

'''Вывод: словарь выводится быстрее т.к имеет сложность О(1) и можно обратиться 
   по ключу'''

# task c
'''с) удаление элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   удаление элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени'''


@time_of_function
def del_list_element():
    new_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    i = 0
    while i < len(new_list):
        del new_list[i]
        i = i+1
    return new_list


@time_of_function
def del_dictionary():
    my_dict = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}
    for value in my_dict.values():
        del my_dict[value]
    return my_dict


del_list_element()
del_dictionary()

'''Вывод: элемент словаря удаляется быстрее т.к имеет сложность О(1).
   Изучив материалы, нашла заключение: Поиск, удаление значения в списке занимает O (n) времени,
   потому что весь список необходимо перебирать до тех пор, пока значение не будет найдено. 
   Поиск ключа в словаре занимает O (1) времени, потому что это хеш-таблица. Это может иметь 
   огромное значение во времени,если значений много, поэтому словари обычно рекомендуются
   для скорости.'''