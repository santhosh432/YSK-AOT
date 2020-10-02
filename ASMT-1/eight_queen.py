"""
Author: YSK
Problem: Eight Queen problem

"""
import random


class EightQueenProblem:
    """ Eight queen problem """

    def __init__(self, population_size=None,
                 random_individuals=None,
                 best_individuals=None,
                 random_cross_over_point=None):

        """ Initialize parameters """

        self.population_size = population_size # population_size set at initial stage
        self.random_individuals = random_individuals # random_individuals set at initial stage
        self.best_individuals = best_individuals # best_individuals set at initial stage
        self.random_cross_over_point = random_cross_over_point # random_cross_over_point set at initial stage

    def get_population(self):
        """ create a population by population size """
        print('Population size: ', self.population_size)
        print('Population:')

        set_list = [i for i in range(1,9)]
        population = list()

        for i in range(self.population_size):
            res = random.sample(set_list, len(set_list))
            population.append(res)

        print(population, '\n')

        return population

    def select_n_individual(self):
        """ select n random individuals out of population size """
        population = self.get_population()

        print('Random individuals :', self.random_individuals)
        print('Random individuals from population')

        res = random.sample(population, self.random_individuals)

        print(res, '\n')
        return res

    def select_best_individuals(self):
        res = self.select_n_individual()
        print('Select best individuals:', res)

        # todo select best n
        res = random.sample(res, self.best_individuals)
        print(res)
        return res

    def cut_and_cross(self):
        """ cut and cross fill over """
        res = self.select_best_individuals()
        print('Cut and cross')

        parent_one = res[0]
        parent_two = res[1]

        print('Parent one', parent_one)
        print('Parent two', parent_two)

        print('self.random_cross_over_point:', self.random_cross_over_point)
        child_one = parent_one[:self.random_cross_over_point]
        child_two = parent_two[:self.random_cross_over_point]

        print('child_one ', child_one)
        print('child_two ', child_two)

        for p1 in parent_two:
            if  p1 not in child_one:
                child_one.append(p1)

        for p2 in parent_one:
            if p2 not in child_two:
                child_two.append(p2)

        print('Fchild_one ', child_one)
        print('Fchild_two ', child_two)
        return [child_one, child_two]

    def mutation_process(self):
        """ mutation process , assume child one is off string """
        res = self.cut_and_cross()
        print('Mutation process', res)

        print(res)
        # off_string = random.sample(res, 1)
        off_string = res[0]
        print('Off string :', off_string)

        rv1, rv2 = random.sample(off_string, 2)
        print(rv1, rv2)
        rv1_index = off_string.index(rv1)
        rv2_index = off_string.index(rv2)
        off_string[rv1_index] = rv2
        off_string[rv2_index] = rv1
        print('Output:', off_string)
        return off_string


if __name__ == '__main__':

    obj = EightQueenProblem(population_size=500, random_individuals=300, best_individuals=2, random_cross_over_point=4)
    # obj.get_population()
    # obj.select_n_individual()
    # obj.select_best_individuals()
    obj.mutation_process()