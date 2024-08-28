#!/usr/bin/python3
'''a function that returns a list of lists of integers
representing the Pascal's triangle'''
def pascal_triangle(n: int) -> list:
    # assigning an empty list
    triangle = []
    if n <= 0:
        return triangle
    for i in range(n):
        pasc = []
        for m in range(i + 1):
            if m  == 0 or m == i:
                pasc.append(1)
            else:
                pasc.append(triangle[i - 1][m -1] + triangle[i - 1][m])
        triangle.append(pasc)
    return triangle

# print(pascal_triangle(5))