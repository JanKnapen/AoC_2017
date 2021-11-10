def get_group(n, s):
    s.add(n)
    line = [x for x in lines if int(x.split()[0]) == n][0]
    nums = list(map(int, ' '.join(line.split()[2:]).split(', ')))
    for num in [x for x in nums if x not in s]:
        nums += list(get_group(num, s))
        s = set(list(s) + nums)
    return set(nums)


def get_result1():
    return len(get_group(0, set()))


def get_result2():
    programs = [int(x.split()[0]) for x in lines]
    visited = set()
    total = 0
    for program in programs:
        if program not in visited:
            new_group = get_group(program, set())
            visited = set(list(visited) + list(new_group))
            total += 1
    return total


with open("input.txt") as f:
    lines = f.read().splitlines()


print("Answer part 1:", get_result1())
print("Answer part 2:", get_result2())
