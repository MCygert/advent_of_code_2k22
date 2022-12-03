import unittest
if __name__ == '__main__':
    with open("calories.txt", 'r') as f:
        calories = []
        temp = 0
        for line in f:
            if line.strip() == "":
                calories.append(temp)
                temp = 0
            else:
                temp += int(line.strip())

    calories.sort()
    print(sum(calories[-3:]))