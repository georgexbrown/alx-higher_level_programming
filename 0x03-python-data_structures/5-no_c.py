#!/usr/bin/python3
def no_c(my_string):
    replace = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            replace += char
    return replace
