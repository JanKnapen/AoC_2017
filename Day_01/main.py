def get_result(n):
    sum = 0
    for i, num in enumerate(line):
        if line[(i+n) % len(line)] == num:
            sum += int(num)
    return sum


with open("input.txt") as f:
    lines = f.readlines()
line = lines[0]

print("Answer part 1:", get_result(1))
print("Answer part 2:", get_result(int(len(line)/2)))
