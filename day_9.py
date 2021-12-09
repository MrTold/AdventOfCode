def basin(mat, y, x):
    if mat_checked[y][x]:
        return 0
    mat_checked[y][x] = True
    size = 1
    if x > 0:
        if mat[y][x - 1] > mat[y][x] and mat[y][x - 1] != 9:
            size += basin(mat, y, x - 1)
    if x < len(mat[0]) - 1:
        if mat[y][x + 1] > mat[y][x] and mat[y][x + 1] != 9:
            size += basin(mat, y, x + 1)
    if y > 0:
        if mat[y - 1][x] > mat[y][x] and mat[y - 1][x] != 9:
            size += basin(mat, y - 1, x)
    if y < len(mat) - 1:
        if mat[y + 1][x] > mat[y][x] and mat[y + 1][x] != 9:
            size += basin(mat, y + 1, x)
    return size


def find_low(mat, y, x):
    low = True
    if y > 0:
        if mat[y - 1][x] < mat[y][x]:
            low = False
    if y < len(mat) - 1:
        if mat[y + 1][x] < mat[y][x]:
            low = False
    if x > 0:
        if mat[y][x - 1] < mat[y][x]:
            low = False
    if x < len(mat[0]) - 1:
        if mat[y][x + 1] < mat[y][x]:
            low = False
    return low


input_file = open("input_9d.txt", "r")
points = [[int(x) for x in list(line)] for line in input_file.read().strip().split('\n')]
print(points)
low_sum = 0
basins = []
mat_checked = []
for i in range(len(points)):
    mat_checked.append([False] * len(points[0]))

for i in range(len(points)):
    for j in range(len(points[0])):
        if find_low(points, i, j):
            low_sum += points[i][j] + 1
            basins.append(basin(points, i, j))

print(f'Solution part one: {low_sum}')

basin_mul = 1
for i in range(3):
    basin_mul *= max(basins)
    basins.remove(max(basins))

print(f'Solution part two: {basin_mul}')


