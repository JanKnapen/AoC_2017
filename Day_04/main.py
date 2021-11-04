def is_valid1(password):
    words = []
    for word in password.split():
        if word in words:
            return False
        words.append(word)
    return True


def get_result1():
    total_valid = 0
    for line in lines:
        if is_valid1(line):
            total_valid += 1
    return total_valid


def get_dicts(password):
    dicts = []
    for word in password.split():
        word_dict = {}
        for letter in word:
            try:
                word_dict[letter] += 1
            except:
                word_dict[letter] = 1
        dicts.append(word_dict)
    return dicts


def is_valid2(dicts):
    checked_dicts = []
    for word_dict in dicts:
        if word_dict in checked_dicts:
            return False
        checked_dicts.append(word_dict)
    return True


def get_result2():
    total_valid = 0
    for line in lines:
        if is_valid2(get_dicts(line)):
            total_valid += 1
    return total_valid


with open("input.txt") as f:
    lines = f.readlines()

print("Answer part 1:", get_result1())
print("Answer part 2:", get_result2())
