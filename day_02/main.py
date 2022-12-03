
# a -> Rock
# b -> Paper
# c -> Scissors
# SECOND  COLUMN
# x -> ROCK
# y -> PAPER
# z -> SCISSORS

# rock -> 1
# paper -> 2
# scissors -> 3

# 0 lose
# 3 draw
# 6 win
def choose_hand(line: str):
    first = line[0]
    second = line[2]

    if second == "X":
        if first == "A":
            return first, "Z"
        elif first == "B":
            return first, "X"
        else:
            return first, "Y"

    elif second == "Y":
        if first == "A":
            return first, "X"
        elif first == "B":
            return first, "Y"
        else:
            return first, "Z"
    else:
        if first == "A":
            return first, "Y"
        elif first == "B":
            return first, "Z"
        else:
            return first, "X"


def calculate_winner(first: str, second: str) -> int:
    points = {
        "Y": 2,
        "X": 1,
        "Z": 3
    }

    sum = 0
    if (first == "A" and second == "X") or (first == "B" and second == "Y") or (first == "C" and second == "Z"):
        sum += 3
    elif first == "A" and second == "Z":
        sum += 0
    elif first == "B" and second == "X":
        sum += 0
    elif first == "C" and second == "Y":
        sum += 0
    else:
        sum += 6

    print(f"sum from win ${sum}")
    sum += points[second]
    print(f"sum with chosen type {sum}")
    return sum


if __name__ == "__main__":
    solution = 0
    with open('input.txt') as f:
        for line in f:
            first, second = choose_hand(line)
            print(f"{first}, {second}")
            solution += calculate_winner(first, second)
    print(solution)
