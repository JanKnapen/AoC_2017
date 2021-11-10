def get_dis(pos):
    pos = (abs(pos[0]), abs(pos[1]))
    steps = int(pos[1] / 2)
    steps += int(pos[0] / 2) + pos[0] % 2
    return steps


def get_results():
    directions = lines[0].split(',')
    pos = (0, 0)
    direction_vectors = {'n': (0, 2), 'ne': (1, 1), 'se': (1, -1), 's': (0, -2), 'sw': (-1, -1), 'nw': (-1, 1)}
    max_dis = 0
    for direction in directions:
        vector = direction_vectors[direction]
        pos = (pos[0] + vector[0], pos[1] + vector[1])
        max_dis = max(max_dis, get_dis(pos))
    return get_dis(pos), max_dis


with open("input.txt") as f:
    lines = f.read().splitlines()


print("Answer part 1:", get_results()[0])
print("Answer part 2:", get_results()[1])
