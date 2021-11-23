def dance(order):
    for command in commands:
        match command[0]:
            case 's':
                order = order[-command[1]:] + order[:-command[1]]
            case 'x':
                order = order[:command[1]] + order[command[2]] + order[command[1]+1:command[2]] + order[command[1]] + order[command[2]+1:]
            case 'p':
                positions = [order.index(command[1]), order.index(command[2])]
                pos1 = min(positions)
                pos2 = max(positions)
                order = order[:pos1] + order[pos2] + order[pos1+1:pos2] + order[pos1] + order[pos2+1:]
            case _:
                raise Exception
    return order


def parse_command(command):
    match command[0]:
        case 's':
            steps = int(command[1:]) % 16
            return ['s', steps]
        case 'x':
            positions = [int(command[1:].split('/')[0]), int(command[1:].split('/')[1])]
            pos1 = min(positions)
            pos2 = max(positions)
            return ['x', pos1, pos2]
        case 'p':
            return ['p', command[1], command[3]]
        case _:
            raise Exception


def get_results():
    order = 'abcdefghijklmnop'
    order1 = dance(order)
    i1 = -1
    i = 0
    while i < 1000000000:
        order = dance(order)
        if order == 'abcdefghijklmnop':
            if i1 == -1:
                i1 = i
            else:
                skip_length = i - i1
                i = 1000000000 - ((1000000000 - i1) % skip_length)
        i += 1
    return order1, order


with open("input.txt") as f:
    lines = f.read().splitlines()


commands = list(map(parse_command, lines[0].split(',')))
result = get_results()
print("Answer part 1:", result[0])
print("Answer part 2:", result[1])
