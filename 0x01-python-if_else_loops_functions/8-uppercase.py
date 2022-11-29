#!/usr/bin/python3
def uppercase(str):
    output = ""
    for i in str: 
        if ord(i) >= 97 and ord(i) <= 122:
            ouput += chr(ord(i) - 32)
        else:
            output += i
    print("{:s}".format(output))
