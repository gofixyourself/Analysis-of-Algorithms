def modified_levenstein(first_string, second_string):
    length_first, length_second = len(first_string), len(second_string)

    # For saving memory, we will work with two rows of the matrix:
    if length_first != length_second:
        if length_first > length_second:
            first_string, second_string = second_string, first_string
            length_first, length_second = length_second, length_first

    current_row = range(length_first + 1)

    for i in range(1, length_second + 1):
        current_row, previous_row = [i] + [0] * length_first, current_row
        for j in range(1, length_first + 1):
            remove, adding, exchange = current_row[j - 1] + 1, previous_row[j] + 1, previous_row[j - 1]
            if first_string[j - 1] != second_string[i - 1]:
                exchange += 1
                if j > 1 and first_string[j - 2] == second_string[i - 1]:
                    transposition = previous_row[j - 2] + 1
                    current_row[j] = min(remove, adding, exchange, transposition)

            current_row[j] = min(remove, adding, exchange)

    return current_row[length_first]
