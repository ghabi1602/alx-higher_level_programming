#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    listt = [False] * len(my_list)
    for i in range(my_list):
        if (my_list[i] % 2) == 0:
            listt[i] = True
    return listt
