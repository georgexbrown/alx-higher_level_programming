#!/usr/bin/python3
def uppercase(str):
    alpha = ""
    for c in str:
        if ord(c) in range(97, 123):
            alpha += chr(ord(c) - 32)
        else:
            alpha += c
    print("{}".format(alpha))
