def get_results():
    combinations = []
    total_redistr = 0
    while blocks not in combinations:
        combinations.append(blocks.copy())
        redistr = max(blocks)
        idx = (blocks.index(redistr) + 1) % len(blocks)
        blocks[(idx-1) % len(blocks)] = 0
        while redistr > 0:
            redistr -= 1
            blocks[idx] += 1
            idx = (idx + 1) % len(blocks)
        total_redistr += 1
    return total_redistr, total_redistr - combinations.index(blocks)


with open("input.txt") as f:
    lines = f.readlines()

blocks = [int(x) for x in lines[0].split()]

print("Answer part 1:", get_results()[0])
print("Answer part 2:", get_results()[1])
