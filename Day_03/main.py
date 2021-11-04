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


def get_result2(input_value):
    n = 0
    while (2*n+1)**2 < input_value:
        n += 1

    grid = defaultdict(int)
    grid[0, 0] = 1
    for i in range(1, n):
        x, y = i, -i+1
        grid[x, y] = grid[x - 1, y - 1] + grid[x - 1, y] + grid[x - 1, y + 1] + grid[x, y - 1] + grid[x, y + 1] + grid[
            x + 1, y - 1] + grid[x + 1, y] + grid[x + 1, y + 1]
        if grid[x, y] > input_value:
            return grid[x, y]
        width = 2*i+1
        for j in range(width-2):
            y += 1
            grid[x, y] = grid[x - 1, y - 1] + grid[x - 1, y] + grid[x - 1, y + 1] + grid[x, y - 1] + grid[x, y + 1] + \
                         grid[x + 1, y - 1] + grid[x + 1, y] + grid[x + 1, y + 1]
            if grid[x, y] > input_value:
                return grid[x, y]
        for j in range(width-1):
            x -= 1
            grid[x, y] = grid[x - 1, y - 1] + grid[x - 1, y] + grid[x - 1, y + 1] + grid[x, y - 1] + grid[x, y + 1] + \
                         grid[x + 1, y - 1] + grid[x + 1, y] + grid[x + 1, y + 1]
            if grid[x, y] > input_value:
                return grid[x, y]
        for j in range(width-1):
            y -= 1
            grid[x, y] = grid[x - 1, y - 1] + grid[x - 1, y] + grid[x - 1, y + 1] + grid[x, y - 1] + grid[x, y + 1] + \
                         grid[x + 1, y - 1] + grid[x + 1, y] + grid[x + 1, y + 1]
            if grid[x, y] > input_value:
                return grid[x, y]
        for j in range(width-1):
            x += 1
            grid[x, y] = grid[x - 1, y - 1] + grid[x - 1, y] + grid[x - 1, y + 1] + grid[x, y - 1] + grid[x, y + 1] + \
                         grid[x + 1, y - 1] + grid[x + 1, y] + grid[x + 1, y + 1]
            if grid[x, y] > input_value:
                return grid[x, y]
    return -1


print("Answer part 1:", get_result1(312051))
print("Answer part 2:", get_result2(312051))
