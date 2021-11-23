def get_results():
    buffer = [0]
    step_length = 359
    pos = 0
    for i in range(2017):
        steps = step_length % len(buffer)
        pos = (pos + steps) % len(buffer)
        buffer.insert(pos+1, i+1)
        pos += 1

    pos = 0
    result2 = -1
    for i in range(50000000):
        steps = step_length % (i+1)
        pos = (pos + steps) % (i+1)
        pos += 1
        if pos == 1:
            result2 = i+1

    return buffer[buffer.index(2017)+1], result2


result = get_results()
print("Answer part 1:", result[0])
print("Answer part 2:", result[1])
