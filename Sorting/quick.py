def quick_sort(array):
    if array:
        return quick_sort([x for x in array if x < array[0]]) + [x for x in array if x == array[0]]\
               + quick_sort([x for x in array if x > array[0]])
    return array
