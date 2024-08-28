#!/usr/bin/python3
'''a function that returns a list of lists of integers
representing the Pascal's triangle'''


def pascal_triangle(n: int) -> list:
    ''' assigning an empty list '''
    triangle = []
    ''' less than/equal to 0 return an empty list '''
    if n <= 0:
        return triangle
    # looping i = rows
    for i in range(n):
        pasc = []
        # looping m = columns
        for m in range(i + 1):
            if m  == 0 or m == i:
                pasc.append(1)
            else:
                pasc.append(triangle[i - 1][m -1] + triangle[i - 1][m])
        triangle.append(pasc)
    return triangle
# print(pascal_triangle(5))