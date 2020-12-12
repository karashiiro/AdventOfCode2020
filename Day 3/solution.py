import math
import sys

SLOPES = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]

with open(sys.argv[1]) as f:
    input_txt = str(f.read())
    map_tile = [list(row) for row in input_txt.split("\n")]

trees_per_slope = []
for d_x, d_y in SLOPES:
    trees = 0
    x = 0
    y = 0
    while y < len(map_tile):
        if map_tile[y][x] == "#":
            trees += 1
        x += d_x
        y += d_y
        if x >= len(map_tile[0]):
            x -= len(map_tile[0])
    trees_per_slope.append(trees)

print("Trees: %d" %math.prod(trees_per_slope))
