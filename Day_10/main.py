def get_result1(lengths, li, cur=0, skip=0):
    li = list(li)
    for length in lengths:
        rev = li[cur:min(len(li), cur+length)]
        if cur+length > len(li):
            rev += li[0:(cur+length) % len(li)]
        rev.reverse()
        if cur+length > len(li):
            li1 = rev[len(rev) - ((cur+length) % len(li)):]
            li2 = li[(cur+length) % len(li):cur]
            li3 = rev[:len(rev) - ((cur+length) % len(li))]
            li = li1 + li2 + li3
        else:
            li1 = li[:cur]
            li2 = rev
            li3 = li[cur+length:]
            li = li1 + li2 + li3
        cur = (cur + length + skip) % len(li)
        skip += 1
    return li[0] * li[1], li, cur, skip


def get_result2(string):
    lengths = []
    for char in string:
        lengths.append(ord(char))
    lengths += [17, 31, 73, 47, 23]

    cur = 0
    skip = 0
    li = list(range(256))
    for i in range(64):
        result = get_result1(lengths, li.copy(), cur, skip)
        li = result[1]
        cur = result[2]
        skip = result[3]
    dense = []
    for i in range(16):
        xor = li[i * 16]
        for num in li[i * 16 + 1:(i+1) * 16]:
            xor ^= num
        dense.append(xor)
    result = ''
    for num in dense:
        result += hex(num)[2:].zfill(2)
    return result


if __name__ == '__main__':
    with open("input.txt") as f:
        lines = f.read().splitlines()


print("Answer part 1:", get_result1(list(map(int, lines[0].split(','))), list(range(256)))[0])
print("Answer part 2:", get_result2(lines[0]))
