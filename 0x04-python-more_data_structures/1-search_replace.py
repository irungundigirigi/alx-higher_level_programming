#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def find(n):
        return n if n != search else replace
    return list(map(find, my_list))
