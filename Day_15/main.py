

def get_result1(A, B):
    total_matches = 0
    for i in range(40000000):
        A = (A * 16807) % 2147483647
        B = (B * 48271) % 2147483647
        if bin(A)[-16:] == bin(B)[-16:]:
            total_matches += 1
    return total_matches


def get_result2(A, B):
    total_matches = 0
    for i in range(5000000):
        A = (A * 16807) % 2147483647
        while A % 4 != 0:
            A = (A * 16807) % 2147483647
        B = (B * 48271) % 2147483647
        while B % 8 != 0:
            B = (B * 48271) % 2147483647
        if bin(A)[-16:] == bin(B)[-16:]:
            total_matches += 1
    return total_matches


with open("input.txt") as f:
    lines = f.read().splitlines()


print("Answer part 1:", get_result1(int(lines[0].split()[4]), int(lines[1].split()[4])))
print("Answer part 2:", get_result2(int(lines[0].split()[4]), int(lines[1].split()[4])))
