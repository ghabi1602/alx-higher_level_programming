#!/usr/bin/python3
def uppercase(str):
    new_str = str
    for i in range(0, len(str)):
        if ord(str[i]) in range(97, 123):
            new_str = new_str[:i] + chr(ord(new_str[i]) - 32) + new_str[i+1:]
    print("{}".format(new_str))
