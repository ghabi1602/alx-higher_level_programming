#!/usr/bin/python3
def pow(a, b):
    p = 1
    if b < 0:
        for i in range(-b):
            p *= a
        return 1/p
    for i in range(b):
        p *= a
    return p
