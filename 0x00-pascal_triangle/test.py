#!/usr/bin/python3


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def comb(row, col):
    return factorial(row) // ((factorial(row - col)) * factorial(col))


def pascal_triangle(n):
    if n <= 0:
        return [[]]
    pascal_list = []
    for row in range(n):
        new_list = []
        for col in range(row + 1):
            new_list.append(comb(row, col))
        pascal_list.append(new_list)
    return pascal_list


if __name__ == "__main__":
    def print_triangle(triangle):
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))
    print_triangle(pascal_triangle(0))