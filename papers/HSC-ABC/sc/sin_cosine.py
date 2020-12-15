"""
author: YSk
Topic: Sin cosine optimization algorithm
"""
import random
import numpy as np
import copy
import math

class SinCosine:
    """ initialize parameters """
    def __init__(self,
                 population_size=None,
                 max_iterations=None,
                 upper_bound=None,
                 lower_bound=None,
                 dim=None):
        self.populations_size = population_size
        self.max_iterations = max_iterations
        self.upper_bound = upper_bound
        self.lower_bound = lower_bound
        self.values = list()
        self.min_value = None
        self.best_value = None
        self.dim = dim


    def fitness(self, p=list()):
        """ objective function for the problem
            input:
                p : list of elements with all dimension [x1, x2, x3, .... xn]

            output:
                squares of all elements

        """
        return sum([i * i for i in p])

    def random_uniform(self):
        """ random two decimal point eg: 0.00 """
        r = random.uniform(0,1)
        return round(r,2)


    def populations(self):
        """ set population """

        # Population : [[3.53, -1.69], [-3.59, 0.34], [-4.29, -1.95], [2.08, -4.75], [0.14, -3.02], [1.39, 4.92]]
        pop = list()
        for _ in range(self.populations_size):
            ind = list()
            for i in range(self.dim):
                ind.append(round(random.uniform(self.lower_bound, self.upper_bound),2))

            pop.append(ind)

        # Population : [[5, -5], [2, 3], [-3, 5], [1, 2], [-5, -4], [-4, -4]]
        # pop = [[random.randint(self.lower_bound, self.upper_bound), random.randint(self.lower_bound, self.upper_bound)] for _ in range(6)]

        # print('Population :', pop)

        for i in range(self.populations_size):
            fit = self.fitness(pop[i])
            self.values.append({'candidate': pop[i],
                                'fitness': fit})

        self.best_value = copy.deepcopy(sorted(self.values, key = lambda x: x['fitness'])[0])

    def run(self):
        """ run process """
        self.populations()
        stop = False
        for t in range(1, self.max_iterations + 1):
            # run over iterations
            # print("Iteration number:-", t)
            source = copy.deepcopy(self.values)
            if stop:
                break
            r1  = (2 - 2 * (t / self.max_iterations))
            for i in range(self.populations_size):

                # run all possible solution
                for j in range(self.dim):
                    # dimension of problem eg: x1, x2 (total parameters)
                    r4 = self.random_uniform()

                    if r4 < 0.5:
                        v = round(source[i]['candidate'][j] + r1 * np.sin(2 * np.pi * self.random_uniform()) * abs(self.random_uniform() * self.best_value['candidate'][j] - source[i]['candidate'][j]), 10)
                        source[i]['candidate'][j] = v
                    else:
                        v = round(source[i]['candidate'][j] + r1 * np.cos(2 * np.pi * self.random_uniform()) * abs(self.random_uniform() * self.best_value['candidate'][j] - source[i]['candidate'][j]), 10)
                        source[i]['candidate'][j] = v

                    if source[i]['candidate'][j] < self.lower_bound:
                        # print('Lower ==================', source[i]['candidate'][j])

                        source[i]['candidate'][j] = self.lower_bound
                    elif source[i]['candidate'][j] > self.upper_bound:
                        # print('Upper ==================', source[i]['candidate'][j])

                        source[i]['candidate'][j] = self.upper_bound
                    else:
                        pass

                source[i]['fitness'] = self.fitness(source[i]['candidate'])

                # if fitness == 0 , solution found
                if source[i]['fitness'] == 0:
                    stop = True
                self.values = copy.deepcopy(source)
                # print(source[i])

            pbest = copy.deepcopy(sorted(source, key = lambda x: x['fitness'])[0])
            # print(pbest['fitness'], self.best_value['fitness'])
            if pbest['fitness'] < self.best_value['fitness']:
                self.best_value = copy.deepcopy(pbest)

if __name__ == '__main__':
    obj = SinCosine(population_size=6, max_iterations=500, upper_bound=100, lower_bound=-100, dim=10)
    obj.run()
    print('Best value :', obj.best_value)


