#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    list_n = []

    for i in my_list:
        if i % 2 == 0:
            list_n.append(True)
        else:
            list_n.append(False)
    return (list_n)
