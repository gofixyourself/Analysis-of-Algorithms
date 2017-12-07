from random import randint
import numpy


def create_distance_matrix(cities_number):
    matrix = numpy.zeros((cities_number, cities_number))
    for i in range(cities_number):
        for j in range(i + 1, cities_number):
            distance = randint(1, 10)
            matrix[i][j] = distance
            matrix[j][i] = distance

    return matrix

if __name__ == "__main__":


