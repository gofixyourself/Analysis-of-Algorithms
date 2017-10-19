def levenshtein_disctance_recursion(first_string, second_string):
    length_first, length_second = len(first_string), len(second_string)

    if (length_first == 1) and (length_second == 1):
        if first_string == second_string:
            return 0
        else:
            return 1
    else:
        if (length_first > length_second == 1) or (length_second > length_first == 1):
            return abs(length_first - length_second) + 1

    exchange = 0
    if first_string[-1] != second_string[-1]:
        exchange = 1

    return min(levenshtein_disctance_recursion(first_string[:length_first - 1], second_string) + 1,
               levenshtein_disctance_recursion(first_string, second_string[:length_second - 1]) + 1,
               levenshtein_disctance_recursion(first_string[:length_first - 1],
                                               second_string[:length_second - 1]) + exchange)
