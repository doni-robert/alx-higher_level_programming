#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list is None:
        return 0
    num = list(map((lambda x, y: (x * y)), my_list))
    print (num)
    return 2 


