#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) and my_list:
        numerator = 0
        denom = 0
        for tuple in my_list:
            numerator += (tuple[0] * tuple[1])
            denom += (tuple[1])
        return (numerator/denom)
    return 0
