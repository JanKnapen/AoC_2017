def get_value(par, registers):
    try:
        return int(par)
    except:
        return registers[par]


def get_result1():
    i = 0
    instructions = list(map(lambda x: x.split(), lines))
    result1 = 0
    got_result1 = False
    registers = {instr[1]: 0 for instr in instructions}
    while not got_result1:
        instr = instructions[i]
        match instr[0]:
            case 'snd':
                result1 = get_value(instr[1], registers)
            case 'set':
                registers[instr[1]] = get_value(instr[2], registers)
            case 'add':
                registers[instr[1]] += get_value(instr[2], registers)
            case 'mul':
                registers[instr[1]] *= get_value(instr[2], registers)
            case 'mod':
                registers[instr[1]] %= get_value(instr[2], registers)
            case 'rcv':
                if registers[instr[1]] != 0:
                    got_result1 = True
            case 'jgz':
                if get_value(instr[1], registers) > 0:
                    i += get_value(instr[2], registers) - 1
            case _:
                raise Exception
        i += 1
    return result1


def process_instruction(i, instructions, registers, sent):
    instr = instructions[i]
    receiving = False
    match instr[0]:
        case 'snd':
            sent.append(get_value(instr[1], registers))
        case 'set':
            registers[instr[1]] = get_value(instr[2], registers)
        case 'add':
            registers[instr[1]] += get_value(instr[2], registers)
        case 'mul':
            registers[instr[1]] *= get_value(instr[2], registers)
        case 'mod':
            registers[instr[1]] %= get_value(instr[2], registers)
        case 'rcv':
            receiving = True
            i -= 1
        case 'jgz':
            if get_value(instr[1], registers) > 0:
                i += get_value(instr[2], registers) - 1
        case _:
            raise Exception
    i += 1
    return i, registers, sent, receiving


def get_result2():
    i0 = 0
    i1 = 0
    instructions = list(map(lambda x: x.split(), lines))
    registers0 = {instr[1]: 0 for instr in instructions}
    registers1 = {instr[1]: 0 for instr in instructions}
    registers1['p'] = 1
    sent0 = []
    sent1 = []
    receiving0 = False
    receiving1 = False
    total_sent1 = 0
    while not (receiving0 and receiving1):
        if not receiving0:
            i0, registers0, sent0, receiving0 = process_instruction(i0, instructions, registers0, sent0)
        elif len(sent1) > 0:
            registers0[instructions[i0][1]] = sent1[0]
            sent1 = sent1[1:]
            total_sent1 += 1
            i0 += 1
            receiving0 = False

        if not receiving1:
            i1, registers1, sent1, receiving1 = process_instruction(i1, instructions, registers1, sent1)
        elif len(sent0) > 0:
            registers1[instructions[i1][1]] = sent0[0]
            sent0 = sent0[1:]
            i1 += 1
            receiving1 = False
    return total_sent1


with open("input.txt") as f:
    lines = f.read().splitlines()


print("Answer part 1:", get_result1())
print("Answer part 2:", get_result2())
