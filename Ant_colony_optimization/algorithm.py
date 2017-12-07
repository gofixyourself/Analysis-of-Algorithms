from random import randint
import numpy

values = {'alpha': 1,  # pheromone weights
          'beta': 1,  # pheromone weights
          'e': 3,  # elite ants
          'Q': 10,  # order of the length of the optimal path
          'p': 0.5}  # pheromone evaporation


def create_distance_matrix(cities_number):
    matrix = numpy.zeros((cities_number, cities_number))
    for i in range(cities_number):
        for j in range(i + 1, cities_number):
            distance = randint(1, 10)  # from the minimum distance to the maximum
            matrix[i][j], matrix[j][i] = distance, distance  # for symmetry of the matrix with respect to the main axis

    return matrix


def ant_colony_optimization(distance_matrix, alpha, beta, e, Q, p, cities_number):
    shortest_route, length_route = None, None  # shortest route and its length
    pheromons = numpy.random.sample((cities_number, cities_number))
    visibility = 1 / distance_matrix

    time = 0

    while time < 300:
        for_all_ants = numpy.zeros((cities_number, cities_number))

        # for every ant:
        for k in range(cities_number):
            ant_town, length_to_town = [k], 0
            current_town = k
            while len(ant_town) != cities_number:
                desired_cities = [r for r in range(cities_number)]
                for visited_town in ant_town:
                    desired_cities.remove(visited_town)
                probability = [0 for t in desired_cities]
                for j in desired_cities:
                    if distance_matrix[current_town][j] != 0:
                        temp = sum(
                            (pheromons[current_town][l] ** alpha) * (visibility[current_town][l] ** beta) for l in
                            desired_cities)
                        probability[desired_cities.index(j)] = \
                            (pheromons[current_town][j] ** alpha) * (visibility[current_town][j] ** beta) / temp
                    else:
                        probability[desired_cities.index(j)] = 0

                max_probability = max(probability)
                if max_probability == 0:
                    return "Current ant is isolated!"

                selected_city = probability.index(max_probability)
                ant_town.append(desired_cities[selected_city])
                length_to_town += distance_matrix[current_town][desired_cities[selected_city]]
                current_town = desired_cities.pop(selected_city)
            if length_route is None \
                    or (length_to_town + distance_matrix[ant_town[0]][ant_town[-1]]) < length_route:
                length_route = length_to_town + distance_matrix[ant_town[0]][ant_town[-1]]
                shortest_route = ant_town

            for pheromone in range(len(ant_town) - 1):
                a = ant_town[pheromone]
                b = ant_town[pheromone + 1]
                for_all_ants[a][b] += Q / length_to_town

        for_elite = (e * Q / length_route) if length_route else 0
        pheromons = (1 - p) * pheromons + for_all_ants + for_elite
        time += 1

    return shortest_route, length_route

