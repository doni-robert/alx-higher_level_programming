#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = []
    list(map((lambda x: new_list.append(replace) if x == search
         else new_list.append(x)), my_list))
    return new_list
