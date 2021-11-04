from collections import defaultdict


def get_result1(input_value):
    n = 0
    while (2*n+1)**2 < input_value:
        n += 1
    num_up = (2*n+1)**2
    width = 2*n+1
    while num_up - (width - 1) > input_value:
        num_up -= (width - 1)
    num_low = num_up - (width - 1)
    cordis = 2*n
    dis = cordis - min(num_up - input_value, input_value - num_low)
    return dis


def get_neighbors_sum(grid, x, y):
    neighbors_sum = 0
    for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        neighbors_sum += grid[x+dx, y+dy]
    return neighbors_sum


def get_result2(input_value):
    max_spiral = 0
    while (2*max_spiral+1)**2 < input_value:
        max_spiral += 1

    grid = defaultdict(int)
    grid[0, 0] = 1

    for spiral in range(1, max_spiral):
        width = 2*spiral+1
        x, y = spiral, 1 - spiral
        grid[x, y] = get_neighbors_sum(grid, x, y)
        if grid[x, y] > input_value:
            return grid[x, y]
        for dx, dy, num_steps in [(0, 1, width-2), (-1, 0, width-1), (0, -1, width-1), (1, 0, width-1)]:
            for i in range(num_steps):
                x, y = x+dx, y+dy
                grid[x, y] = get_neighbors_sum(grid, x, y)
                if grid[x, y] > input_value:
                    return grid[x, y]
    return -1


print("Answer part 1:", get_result1(312051))
print("Answer part 2:", get_result2(312051))
