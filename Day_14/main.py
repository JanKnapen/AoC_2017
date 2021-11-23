from Day_10.main import get_result2


def hex_to_bin(string):
    digits = [bin(int(letter, 16))[2:].zfill(4) for letter in string]
    return digits


def input_to_rows(string):
    return [string + '-' + str(i) for i in range(128)]


def digits_to_grid(digits):
    return [''.join(row) for row in digits]


def get_neighbours(grid, y, x):
    neighbours = []
    if y-1 >= 0 and grid[y-1][x] > 0:
        neighbours.append((y-1, x))
    if x-1 >= 0 and grid[y][x-1] > 0:
        neighbours.append((y, x-1))
    if y+1 < len(grid) and grid[y+1][x] > 0:
        neighbours.append((y+1, x))
    if x+1 < len(grid[0]) and grid[y][x+1] > 0:
        neighbours.append((y, x+1))
    return neighbours


def update_group(grid, y, x):
    next_group = max(map(max, grid)) + 1
    if grid[y][x] > 0:
        neighbours = get_neighbours(grid, y, x)
        groups = [z for z in list(map(lambda k: grid[k[0]][k[1]], neighbours)) if z > 1]
        if len(groups) == 0:
            grid[y][x] = next_group
            for (y2, x2) in neighbours:
                if grid[y2][x2] != grid[y][x]:
                    grid = update_group(grid, y2, x2)
        else:
            grid[y][x] = max(groups)
            for (y2, x2) in neighbours:
                if grid[y2][x2] != grid[y][x]:
                    grid = update_group(grid, y2, x2)
    return grid


def update_groups(grid):
    grid = [[int(letter) for letter in row] for row in grid]
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            grid = update_group(grid, y, x)
    return grid


def get_results():
    rows = input_to_rows(puzzle)
    knots = [get_result2(row) for row in rows]
    digits = [hex_to_bin(knot) for knot in knots]
    total = sum([''.join(row).count('1') for row in digits])

    grid = digits_to_grid(digits)
    grid = update_groups(grid)
    all_groups = set()
    for z in [set(x) for x in grid]:
        for val in z:
            all_groups.add(val)
    all_groups.remove(0)
    return total, len(all_groups)


puzzle = 'hwlqcszp'
result = get_results()
print("Answer part 1:", result[0])
print("Answer part 2:", result[1])
