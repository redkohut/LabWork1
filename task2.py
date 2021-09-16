import sys as s


def _define():
    if operator == "add":
        return number_1 + number_2
    elif operator == "min":
        return number_1 - number_2
    elif operator == "mul":
        return number_1 * number_2
    else:
        print("Please enter correct!")


if __name__ == '__main__':
    operator = s.argv[1]
    number_1 = int(s.argv[2])
    number_2 = int(s.argv[3])
    print(_define())