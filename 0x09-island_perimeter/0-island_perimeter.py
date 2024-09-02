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
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                ''' check top
                '''
                if r == 0 or grid[r - 1][c] == 0:
                    perimeter += 1
                ''' check bottom
                '''
                if r == rows - 1 or grid[r + 1][c] == 0:
                    perimeter += 1
                ''' check left
                '''
                if c == 0 or grid[r][c - 1] == 0:
                    perimeter += 1
                ''' check right
                '''
                if c == cols - 1 or grid[r][c + 1] == 0:
                    perimeter += 1
    return perimeter


grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

print(island_perimeter(grid))
