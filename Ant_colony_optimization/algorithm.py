from random import randint, random
import numpy

values = {'alpha' : 1,    # pheromone weights
          'beta' : 1,       # pheromone weights
          'e' : 3,          # elite ants
          'Q' : 10,         # order of the length of the optimal path
          'p' : 0.5}

def create_distance_matrix(cities_number):
    matrix = numpy.zeros((cities_number, cities_number))
    for i in range(cities_number):
        for j in range(i + 1, cities_number):
            distance = randint(1, 10)  # from the minimum distance to the maximum
            matrix[i][j], matrix[j][i] = distance, distance  # for symmetry of the matrix with respect to the main axis

    return matrix

if __name__ == "__main__":


