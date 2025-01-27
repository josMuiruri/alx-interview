#!/usr/bin/python3

'''Island perimeter computing module
'''


def island_perimeter(grid: list[list[int]]) -> int:
    """Calculate the perimeter of island

    Parameters:
    grid (List[List[int]]): 2D list representing the map where 0 is water and 1 is land

    Returns:
    int: The perimeter of the island
    """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter


grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

print(island_perimeter(grid))
