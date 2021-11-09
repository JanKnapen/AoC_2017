def get_result1(line):
    score = 0
    idx = 0
    cscore = 0
    while idx < len(line):
        if line[idx] == '{':
            cscore += 1
        elif line[idx] == '}':
            score += cscore
            cscore -= 1
        idx += 1
    return score


def get_result2(line):
    garbage = 0
    while '<' in line and '>' in line:
        start_idx = line.index('<')
        end_idx = line.index('>')
        garbage += end_idx - start_idx - 1
        line = line[:start_idx] + line[end_idx+1:]
    return garbage


def cancel(line):
    idx = 0
    while idx < len(line):
        if line[idx] == '!':
            line = line[:idx] + line[idx+2:]
            idx -= 1
        idx += 1
    return line


def clean(line):
    while '<' in line and '>' in line:
        start_idx = line.index('<')
        end_idx = line.index('>')
        line = line[:start_idx] + line[end_idx+1:]
    return line


with open("input.txt") as f:
    lines = f.readlines()

characters = lines[0].split()[0]
characters = cancel(characters)
result2 = get_result2(characters)
characters = clean(characters)

print("Answer part 1:", get_result1(characters))
print("Answer part 2:", result2)
