#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list.copy()
    for x in range(len(new_list)):
        if new_list[x] % 2 == 0:
            new_list[x] = True
        else:
            new_list[x] = False
    return new_list
