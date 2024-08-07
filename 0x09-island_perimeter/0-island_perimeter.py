#!/usr/bin/python3
from typing import List

def island_perimeter(grid: List[List[int]]) -> int:
    
    """
    Calculate the perimeter of island described grid
    Parameters:
    grid (List[List[int]])

    Returns:
    int: The perimeter of the island
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][w] == 1:
                # check top
                if r == 0 or grid[r - 1][c] == 0:
                    perimeter += 1
                # check bottom
                if r == rows - 1 or grid[r + 1][c] == 0:
                    perimeter += 1
                # check left
                if c == 0 or grid[r][c - 1] == 0:
                    perimeter += 1
                # check right
                if  c == cols - 1 or grid[r][c + 1] == 0:
                    perimeter += 1
    return perimeter

print(island_perimeter)