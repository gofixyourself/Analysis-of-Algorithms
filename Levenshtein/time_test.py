import standard_levenshtein as standard
import modified_levenshtein as modified
import levenshtein_with_recursion as recursion
import time
import generator


def time_tests():
    time_standard, time_modified, time_recursion = 0, 0, 0

    strings_for_test = []

    for i in range(10):
        strings_for_test.append(generator.generator())

    for i in range(9):
        for j in range(100):
            start = time.time()
            first = standard.levenshtein_distance(strings_for_test[i], strings_for_test[i + 1])
            end = time.time()

            time_standard += (end - start)

            start = time.time()
            second = modified.modified_levenstein(strings_for_test[i], strings_for_test[i + 1])
            end = time.time()

            time_modified += (end - start)

            start = time.time()
            third = recursion.levenshtein_disctance_recursion(strings_for_test[i], strings_for_test[i + 1])
            end = time.time()

            time_recursion += (end - start)

    print("{0:f} {1:f} {2:f}".format(time_standard / 100 * 1000, time_modified / 100 * 1000,
                                                  time_recursion / 100 * 1000))


if __name__ == "__main__":
    time_tests()
