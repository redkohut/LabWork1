import sys


def _define():
    if len(sys.argv) > 4:
        return False
    elif operator == '*':
        return var1 * var2
    elif operator == '+':
        return var1 + var2
    elif operator == '-':
        return var1 - var2
    elif operator == '/' and var2 != 0:
        return var1 / var2
    else:
        return False


if __name__ == '__main__':
    var1 = int(sys.argv[1])  # data of the first command line argument
    var2 = int(sys.argv[3])  # data of the third command line argument
    operator = sys.argv[2]   # operator
    print(_define())