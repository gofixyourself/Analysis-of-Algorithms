def bubble_sorting(array):
    length = len(array)

    for i in range(length - 1, 0, -1):
        for j in range(i):
            if array[j] > array[j + 1]:
                array[j + 1], array[j] = array[j], array[j + 1]
