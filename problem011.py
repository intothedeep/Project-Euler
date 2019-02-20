#!/bin/python3

import sys
from functools import reduce

grid = []
for grid_i in range(20):
	grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
	grid.append(grid_t)

max_val = reduce(lambda x, y: x * y, grid[0][0:4], 1)
#horizontal
for i in range(20):
    for j in range(20 - 3):
        max_val = max(max_val, reduce(lambda x, y: x * y, grid[i][j:j + 4], 1))

#vertical
for i in range(20 - 3):
    for j in range(20):
        max_val = max(max_val, grid[i][j] * grid[i + 1][j] * grid[i + 2][j] * grid[i + 3][j])

#diagonal
for i in range(20 - 3):
    for j in range(20 - 3):
        max_val = max(max_val, grid[i][j] * grid[i + 1][j + 1] * grid[i + 2][j + 2] * grid[i + 3][j + 3])

#diagonal
for i in range(3, 20):
    for j in range(20 - 3):
        max_val = max(max_val, grid[i][j] * grid[i - 1][j + 1] * grid[i - 2][j + 2] * grid[i - 3][j + 3])
        
print(max_val)
