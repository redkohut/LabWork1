import sys as s

is_correct = True
result = 0
len_arg = len(s.argv)
i = 1


def _main():
    result =_define()
    if is_correct:
        print("Your result (", is_correct, ',', result, ')')
    else:
        print("Your result (", is_correct, ", None)")


def _define():
    i = 1
    while i < len_arg:
        if not s.argv[len_arg - 1].isdigit():
            is_correct = False
            break
        if i % 2 != 0:  # не парне, тобто 1 + 3 + 5 + 7 - ті, які дійсно потрібні
            if not s.argv[i].isdigit():
                is_correct = False
                break
            elif i == 1:
                result = int(s.argv[i])
        else:

            if s.argv[i] in "+-":
                current_operation = s.argv[i]
                if current_operation == '+':
                    result += int(s.argv[i - 1])
                else:
                    result = result - int(s.argv[i - 1])
            else:
                is_correct = False
                break
        i += 1
    return result


_main()