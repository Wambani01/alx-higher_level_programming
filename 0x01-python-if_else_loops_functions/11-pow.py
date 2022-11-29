#!/usr/bin/python3
def pow(a, b):
    if b >= 0:
        return int(a**b)
    else:
        return (1/(a**abs(b)))
