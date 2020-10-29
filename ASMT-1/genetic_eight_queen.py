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

    def __init__(self, population_size=None, board_size=8, iterations=0):

        """ Initialize parameters """

        self.population_size = population_size # population_size set at initial stage
        self.board_size = board_size  # size of the board eg: n * n
        self.Item = namedtuple('Item', ['individuals', 'fitness']) # storing Individuals and their fitness
        self.fitness_list = list()
        self.population = list() # initial population
        self.iterations = iterations
        print('Initial Population Size: ', self.population_size)

    def get_population(self):
        """ create a population by population size """

        set_list = [i for i in range(self.board_size)]

        for i in range(self.population_size):
            res = random.sample(set_list, len(set_list))
            self.population.append(res)
            # self.population_fitness[i] = self.compute_fitness(res)
            self.fitness_list.append(
                self.Item(res, self.compute_fitness(res))
            )

        return self.fitness_list

    @staticmethod
    def show_board(chromosome=None):
        """ print chess board with eight queens """

        board = np.zeros(64).reshape(8,8)
        # print('Empty board:')
        # print(board)
        for i, j in zip(chromosome, range(8)):
            board[i, j] = 1
        print('=' * 50)
        print('Solution:--')
        print(board)

        print('Chromosome: ', chromosome)
        print('=' * 50)

    @staticmethod
    def compute_fitness(chromosome):
        """
        input: chromosome
        output : Fitness of chromosome
             Compute fitness of the chromosome
             Note : Lower value of fitness represents to closeness of solution , Fitness 0 will be the solution
         """
        # print('Before:-',chromosome)
        # print('chromosome:-',chromosome)
        fitness = 0
        for i in range(len(chromosome)):
            # print('i:-', i)
            for j in range(i+1, len(chromosome)):

                if chromosome[i] == chromosome[j]:
                    fitness+=1
                elif math.fabs(chromosome[i] - chromosome[j]) == j - i:
                    fitness+=1
                elif math.fabs(chromosome[j] - chromosome[i]) == i - j:
                    fitness+=1
                else:
                    pass

        return fitness

    def all_best_individuals(self):
        """ best individuals sorted by their lower fitness values """
        # print('ok')
        population = self.get_population()
        sorted_data = sorted(population, key= lambda x: x.fitness)
        return sorted_data

    @staticmethod
    def cross_over(one, two):
        """ cut and cross fill over """
        # res = self.all_best_individuals()
        # print('Cut and cross')

        parent_one = one
        parent_two = two

        random_number  = random.randint(0, len(one)) # generate random number from 0 to 7
        child_one = parent_one[:random_number]
        child_two = parent_two[:random_number]

        # print('child_one ', child_one)
        # print('child_two ', child_two)

        for p1 in parent_two:
            if  p1 not in child_one:
                child_one.append(p1)

        for p2 in parent_one:
            if p2 not in child_two:
                child_two.append(p2)

        return [child_one, child_two]

    def create_new_generation(self):
        """ new generation """

        # best_ind = self.all_best_individuals()
        best_ind = self.fitness_list
        self.fitness_list = list() # empty the records of fitness list

        for l in range(0, len(best_ind), 2):  # get list with step size 2
            try:
                p = self.cross_over(best_ind[l].individuals, best_ind[l+1].individuals)

                res = self.mutation_process(chromosome=p[0])
                self.fitness_list.append(
                    self.Item(res, self.compute_fitness(res))
                )

                res = self.mutation_process(chromosome=p[1])
                self.fitness_list.append(
                    self.Item(res, self.compute_fitness(res))
                )

            except IndexError:
                """ Index out of range """
                pass

        # print(self.fitness_list)

    @staticmethod
    def mutation_process(chromosome):
        """ mutation process """

        off_string = chromosome

        rv1, rv2 = random.sample(off_string, 2)
        # print(rv1, rv2)
        rv1_index = off_string.index(rv1)
        rv2_index = off_string.index(rv2)

        off_string[rv1_index] = rv2
        off_string[rv2_index] = rv1

        return off_string

    def output(self):
        """ make output """
        self.get_population() # first generation
        result = True
        while result:
            # print('self.fitness_list:', self.fitness_list)
            for k in self.fitness_list:

                if k.fitness == 0:
                    self.show_board(k.individuals)
                    result =False
                    break

            self.create_new_generation() # new generation

            self.iterations += 1
        print('Total Iterations:', self.iterations)


obj = EightQueenProblem(population_size=6)
obj.output()