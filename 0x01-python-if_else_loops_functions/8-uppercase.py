#!/usr/bin/python3
def uppercase(str):
    for char in str:
        uppercase_char = char
        if ord(uppercase_char) >= 97 and ord(uppercase_char) <= 122:
            uppercase_char = chr(ord(char) - 32)
        print("{}".format(uppercase_char), end='')
    print()
