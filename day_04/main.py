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
        # if(b_f_r <= b_s_r or e_f_r >= e_s_r) or (b_s_r <= b_f_r or e_s_r >= e_f_r):
        #    count += 1
        if set(range(b_f_r, e_f_r + 1)) & set(range(b_s_r, e_s_r + 1)):
            count += 1
    print(count)
