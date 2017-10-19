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
            if j > 1 and i > 1:
                if first_string[j - 1] != second_string[i - 1]:
                    current_row[j] = min(current_row[j - 1] + 1, previous_row[j] + 1, previous_row[j - 1] + 1,
                                         previous_row[j - 2] + 1)  # for remove, adding, exchange, transposition
                else:
                    current_row[j] = min(current_row[j - 1] + 1, previous_row[j] + 1, previous_row[j - 1],
                                         previous_row[j - 2] + 1)
            else:
                if first_string[j - 1] != second_string[i - 1]:
                    current_row[j] = min(current_row[j - 1] + 1, previous_row[j] + 1,
                                         previous_row[j - 1] + 1)  # for remove, adding, exchange
                else:
                    current_row[j] = min(current_row[j - 1] + 1, previous_row[j] + 1, previous_row[j - 1])

    return current_row[length_first]
