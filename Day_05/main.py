def get_result(n):
    steps = [int(num) for num in lines]
    cur_step = 0
    total_steps = 0
    while 0 <= cur_step < len(steps):
        nex_step = cur_step + steps[cur_step]
        if steps[cur_step] < 3:
            steps[cur_step] += 1
        else:
            steps[cur_step] += n
        cur_step = nex_step
        total_steps += 1
    return total_steps


with open("input.txt") as f:
    lines = f.readlines()

print("Answer part 1:", get_result(1))
print("Answer part 2:", get_result(-1))
