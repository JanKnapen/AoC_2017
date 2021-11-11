def tick(states, directions, ranges):
    for key in states.keys():
        states[key] += directions[key]
        if states[key] == 0:
            directions[key] = 1
        elif states[key] == ranges[key]-1:
            directions[key] = -1
    return states, directions


def get_result1():
    ranges = dict()
    states = dict()
    directions = dict()
    for line in lines:
        vals = line.split(': ')
        ranges[int(vals[0])] = int(vals[1])
        states[int(vals[0])] = 0
        directions[int(vals[0])] = 1
    severity = 0
    for i in range(int(max(states.keys()))+1):
        if i in states.keys() and states[i] == 0:
            severity += ranges[i] * i
        states, directions = tick(states, directions, ranges)
    return severity


def scanner_pos(depth, range_):
    pos = (depth % ((range_ - 1) * 2)) + 1
    if pos > range_:
        return pos - (pos - range_) * 2
    return pos


def get_result2():
    ranges = dict()
    for line in lines:
        vals = line.split(': ')
        ranges[int(vals[0])] = int(vals[1])
    delay = 0
    while True:
        result = list(map(lambda x: scanner_pos(x[0]+delay, x[1]), list(ranges.items())))
        if 1 not in result:
            return delay
        delay += 1


with open("input.txt") as f:
    lines = f.read().splitlines()


print("Answer part 1:", get_result1())
print("Answer part 2:", get_result2())
