import string

alphabet_lower = list(string.ascii_lowercase)
alphabet_higher = list(string.ascii_uppercase)

with open('input.txt', 'r') as f:
    lines = [line.rstrip() for line in f]


def split(input: str):
    n = len(input)
    string1 = input[0:n//2]
    string2 = input[n//2:]
    return string1, string2


# def intersection(first: str, second: str) -> str:
#    return ''.join(set(first).intersection(second))


def intersection_three_lines(first: str, second: str, third: str) -> str:
    return set(first) & set(second) & set(third)


def sum_characters(same_letters: str) -> int:
    sum = 0
    for char in intersection:
        if char.islower():
            sum += alphabet_lower.index(char) + 1
        else:
            sum += alphabet_higher.index(char) + 27
    return sum


if __name__ == "__main__":
    sum = 0
    number_of_lines = 0
    tmp = []
    for line in lines:
        # first_half, second_half = split(line)
        # common_characters = intersection(first_half, second_half)
        number_of_lines += 1
        tmp.append(line)
        if number_of_lines == 3:
            intersection = intersection_three_lines(tmp[0], tmp[1], tmp[2])
            sum += sum_characters(intersection)
            number_of_lines = 0
            tmp.clear()
    print(sum)
