"""
Author: YSK
Problem: Eight Queen problem using genetic algorithm

"""
import random
import numpy as np
import math
from collections import namedtuple

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
        self.board_size = 8
        self.queens = 8
        self.Item = namedtuple('Item', ['individuals', 'fitness'])
        self.fitness_list = list()
        self.population = list()
        print('Population size: ', self.population_size)

    def get_population(self):
        """ create a population by population size """

        set_list = [i for i in range(8)]

        for i in range(self.population_size):
            res = random.sample(set_list, len(set_list))
            self.population.append(res)
            # self.population_fitness[i] = self.compute_fitness(res)
            self.fitness_list.append(
                self.Item(res, self.compute_fitness(res))
            )
            # print(self.compute_fitness(res))

        # print(self.population, '\n')

        return self.fitness_list


    def show_board(self, chromosome=None):
        """ print chess board with eight queens """

        board = np.zeros(64).reshape(8,8)
        # print('Empty board:')
        # print(board)
        for i, j in zip(chromosome, range(8)):
            board[i, j] = 1
        print('=' * 50)
        print('Solution:')
        print(board)
        print('Chromosome', chromosome)

    @staticmethod
    def compute_fitness(chromosome):
        """ Compute fitness """
        # print('Before:-',chromosome)
        # chromosome = self.shift_board(chromosome)
        # print('chromosome:-',chromosome)
        Fitness = 0
        for i in range(len(chromosome)):
            # print('i:-', i)
            for j in range(i+1, len(chromosome)):
                # print('   j:-', j)

                #if i + j == nqueen + 1 :
                #    Fitness+=1
                #elif i == j:
                #    Fitness+=1
                if chromosome[i] == chromosome[j]:
                    Fitness+=1
                elif math.fabs(chromosome[i] - chromosome[j]) == j - i:
                    Fitness+=1
                elif math.fabs(chromosome[j] - chromosome[i]) == i - j:
                    Fitness+=1


        return Fitness

    def all_best_individuals(self):
        """ best individuals """
        # print('ok')
        pop = self.get_population()
        # print(pop)
        sorted_data = sorted(pop, key= lambda x: x.fitness)
        return sorted_data

    def parent_selection(self):
        """ parent selection """
        # print('Parent start')
        p = self.all_best_individuals()[:self.best_individuals]
        # print(len(parents))
        print('P', p)
        parents = list()
        # for i in range(len(p)):
        #     print('i:',i)
        #     ind = p[i].individuals
        #     print(ind)
        #     parents.append(self.population[p[i].individuals])
        # return parents
        return p

    def cut_and_cross(self):
        """ cut and cross fill over """
        res = self.parent_selection()
        # print('Cut and cross')

        parent_one = res[0].individuals
        parent_two = res[1].individuals

        # print('Parent one', parent_one)
        # print('Parent two', parent_two)

        # print('self.random_cross_over_point:', self.random_cross_over_point)
        child_one = parent_one[:self.random_cross_over_point]
        child_two = parent_two[:self.random_cross_over_point]

        # print('child_one ', child_one)
        # print('child_two ', child_two)

        for p1 in parent_two:
            if  p1 not in child_one:
                child_one.append(p1)

        for p2 in parent_one:
            if p2 not in child_two:
                child_two.append(p2)

        return [child_one, child_two]

    def mutation_process(self):
        """ mutation process , assume child one is off string """
        res = self.cut_and_cross()
        # print('Mutation process', res)

        # print(res)
        # off_string = random.sample(res, 1)
        off_string = res[0]
        # print('Off string :', off_string)

        rv1, rv2 = random.sample(off_string, 2)
        # print(rv1, rv2)
        rv1_index = off_string.index(rv1)
        rv2_index = off_string.index(rv2)
        off_string[rv1_index] = rv2
        off_string[rv2_index] = rv1
        # print('Output:', off_string)

        self.fitness_list.append(
            self.Item(off_string, self.compute_fitness(off_string))
        )

        return off_string


    def output(self):
        """ make output """
        i = 0
        # print(op)
        result = True
        while result:
            self.mutation_process()
            print('self.fitness_list:', self.fitness_list)
            for k in self.fitness_list:
                if k.fitness == 0:
                    self.show_board(k.individuals)
                    result =False
                    break
            print('Total Iterations:', i)
            i += 1
            print('Total size population ', len(self.fitness_list))


obj = EightQueenProblem(population_size=500, best_individuals=2)

# print(obj.get_population())
# obj.show_board()

# print(obj.compute_fitness([1, 3, 5, 2, 7, 4, 6, 8]))
# print(obj.compute_fitness([0, 2, 4, 1, 6, 3, 5, 7]))
# print(obj.compute_fitness([0, 1, 2, 3, 4, 5, 6, 7]))

# print(obj.all_best_individuals())
# print(obj.parent_selection())
# print(obj.cut_and_cross())
# print(obj.mutation_process())
obj.output()