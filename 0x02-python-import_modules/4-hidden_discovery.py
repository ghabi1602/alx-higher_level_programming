#!/usr/bin/python3
if __name__ == "__main__":
    import sys, hidden_4
    dir2 = dir(hidden_4.sort())
    for s in dir2:
        if not(s.startswith('__')):
            print("{}".format(s))
