def get_result1():
    checksum = 0
    for line in lines:
        nums = [int(num) for num in line.split()]
        checksum += max(nums) - min(nums)
    return checksum


def get_result2():
    checksum = 0
    for line in lines:
        nums = [int(num) for num in line.split()]
        for i1, num1 in enumerate(nums):
            for i2, num2 in enumerate(nums):
                if max(num1, num2) % min(num1, num2) == 0 and i1 != i2:
                    checksum += max(num1, num2) / min(num1, num2)
    return int(checksum/2)


with open("input.txt") as f:
    lines = f.readlines()

print("Answer part 1:", get_result1())
print("Answer part 2:", get_result2())
