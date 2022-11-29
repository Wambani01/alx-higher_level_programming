#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(i) in range(97, 123):
            i = ord(i) - 32
        print("{}".format(chr(i)), end="")
    print()
