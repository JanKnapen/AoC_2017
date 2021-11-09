def get_register(register):
    try:
        return registers[register]
    except:
        return 0


def check_condition(register, condition, value):
    match condition:
        case '>':
            return get_register(register) > value
        case '<':
            return get_register(register) < value
        case '==':
            return get_register(register) == value
        case '!=':
            return get_register(register) != value
        case '>=':
            return get_register(register) >= value
        case '<=':
            return get_register(register) <= value
        case _:
            raise Exception


def get_results():
    max_allocated = 0
    for instruction in lines:
        instruction = instruction.split()
        if check_condition(instruction[4], instruction[5], int(instruction[6])):
            if instruction[1] == 'inc':
                registers[instruction[0]] = get_register(instruction[0]) + int(instruction[2])
            if instruction[1] == 'dec':
                registers[instruction[0]] = get_register(instruction[0]) - int(instruction[2])
        if len(registers.values()) > 0:
            max_allocated = max(max_allocated, max(registers.values()))
    return max(registers.values()), max_allocated


with open("input.txt") as f:
    lines = f.readlines()

registers = dict()
results = get_results()
print("Answer part 1:", results[0])
print("Answer part 2:", results[1])
