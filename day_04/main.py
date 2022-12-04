with open('input.txt') as f:
    lines = [line.rstrip() for line in f]


def split(input: str):
    numbers = input.split(",")
    b_f_r, e_f_r = numbers[0].split("-")
    b_s_r, e_s_r = numbers[1].split("-")
    return int(b_f_r), int(e_f_r), int(b_s_r), int(e_s_r)


if __name__ == "__main__":
    count = 0
    for line in lines:
        b_f_r, e_f_r, b_s_r, e_s_r = split(line)
        first = [item for item in range(b_f_r, e_f_r+1)]
        second = [item for item in range(b_s_r, e_s_r+1)]
        if len(first) > len(second):
            solution = list(set(second) & set(first))
            if solution == second:
                count += 1
        elif len(first) < len(second):
            solution = list(set(second) & set(first))
            if solution == first:
                count += 1
        else:
            if second == first:
                count += 1
    print(count)
