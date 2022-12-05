#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        p = 1
        for j in i:
            if p == len(i):
                print("{}".format(j), end="")
            else:
                print("{} ".format(j), end="")
            p += 1
        print()
matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
        ]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()
