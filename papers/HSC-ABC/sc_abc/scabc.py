
import json
import random
import matplotlib.pyplot as plt
import copy
import numpy as np

class ABC:

    def __init__(self, population_size, iterations, dim, lower_bound, upper_bound, limit):
        self.population_size = population_size
        self.iterations= iterations
        # self.limit = ( self.population_size / 2 ) * dim
        self.limit = limit
        self.employed_bee_size = self.population_size
        self.onlooker_bee_size = self.population_size
        self.scout_bee_phase_size = self.population_size
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.dim = dim
        self.best = dict()
        self.index = 0
        self.initial_pop = list()

    def function(self, I=list()):
        """ function with d dimensional
            I = list() list of elements eg [x1, x2]
        """
        return round(I[0]*I[0] - I[0]*I[1] + I[1] * I[1] + 2* I[0] + 4*I[1] + 3, 4)
        # return x1*x1 - x1*x2 + x2 * x2 + 2* x1 + 4*x2 + 3

    @staticmethod
    def fitness(fun):
        """ fitness of the function """
        if fun >= 0:
            f = 1 / (1 + fun)
        else:
            f = 1 + abs(fun)

        return round(f,4)

    def initial_population(self):
          # {'candidate: [1,2], 'fit': 25, 'fitness': 0.02, 'trail': 0}
        for i in range(self.population_size):
            initial = dict()
            # print(i)
            X = list()
            for j in range(self.dim):
                n = self.lower_bound + random.uniform(0,1) * (self.upper_bound - self.lower_bound)
                X.append(round(n, 4))

            initial['candidate'] = X
            initial['fit'] = self.function(I=X)
            initial['fitness'] = self.fitness(self.function(I=X))
            initial['trail'] = 0
            self.initial_pop.append(initial)
        self.best = sorted(self.initial_pop, key=lambda x: x['fitness'])[0]
        return self.initial_pop

    def greedy_selection(self, old, new, trail):
        """ greedy selection for new fitness"""

        old_fit = self.function(old)
        new_fit = self.function(new)

        old_fitness = self.fitness(old_fit)
        new_fitness = self.fitness(new_fit)
        greedy = {}
        # print(new, old)
        # print(new_fitness, old_fitness)
        if new_fitness < old_fitness:
            greedy['candidate'] = new
            greedy['fit'] = new_fit
            greedy['fitness'] = new_fitness
            greedy['trail'] = trail
        else:
            greedy['candidate'] = old
            greedy['fit'] = old_fit
            greedy['fitness'] = old_fitness
            greedy['trail'] = trail + 1
        return greedy

    def best_solution(self, pop):

        current_best = sorted(pop, key=lambda x: x['fit'], reverse=True)[0]
        # print(current_best, '--', self.best)

        # print(float(current_best['fit']))

        # print('Previous best:-', float(self.best['fit']))
        if float(current_best['fit']) > float(self.best['fit']):
            # print(current_best)
            best = current_best
        else:
            best = self.best

        # print('Latest best:-',best['fit'])
        return best

    def random_uniform(self):
        """ random two decimal point eg: 0.00 """
        r = random.uniform(0,1)
        return round(r,2)

    def employee_bee_phase(self, iteration):
        """ employee bee phase with iteration number """
        # emp = self.initial_pop.copy()
        # print('Employee -1')
        # print('Sub Iteration:---', i, emp[i]['candidate])
        source = copy.deepcopy(self.initial_pop)

        r1  = (2 - 2 * (iteration / self.iterations))
        for i in range(self.population_size):

            # run all possible solution
            for j in range(self.dim):
                # dimension of problem eg: x1, x2 (total parameters)
                r4 = self.random_uniform()

                if r4 < 0.5:
                    v = round(source[i]['candidate'][j] + r1 * np.sin(2 * np.pi * self.random_uniform()) * abs(self.random_uniform() * self.best['candidate'][j] - source[i]['candidate'][j]), 10)
                    source[i]['candidate'][j] = v
                else:
                    v = round(source[i]['candidate'][j] + r1 * np.cos(2 * np.pi * self.random_uniform()) * abs(self.random_uniform() * self.best['candidate'][j] - source[i]['candidate'][j]), 10)
                    source[i]['candidate'][j] = v

                if source[i]['candidate'][j] < self.lower_bound:
                    # print('Lower ==================', source[i]['candidate'][j])

                    source[i]['candidate'][j] = self.lower_bound
                elif source[i]['candidate'][j] > self.upper_bound:
                    # print('Upper ==================', source[i]['candidate'][j])

                    source[i]['candidate'][j] = self.upper_bound
                else:
                    pass

            old_source = copy.deepcopy(source[i]['fitness'])
            source[i]['fitness'] = self.fitness(source[i]['candidate'])
            new_source = copy.deepcopy(source[i]['fitness'])
            # if fitness == 0 , solution found
            if source[i]['fitness'] == 0:
                stop = True
            self.values = copy.deepcopy(source)
        # emp[i]['candidate] = new_source

            g = self.greedy_selection(old_source, new_source, source[i]['trail'])
            # print(g[0], g[1], g[2], g[3])
            source[i]['candidate'] = g['candidate']
            source[i]['fit'] = g['fit']
            source[i]['fitness'] = g['fitness']
            source[i]['trail'] = g['trail']

        # self.initial_pop = emp
        self.best = copy.deepcopy(self.best_solution(self.initial_pop))
        return self.initial_pop

    def onlooker_bee_phase(self):
        """ onlooker bee phase """

        # emp = self.employee_bee_phase()
        emp = copy.deepcopy(self.initial_pop.copy())
        # print('Onlooker -1')

        # print('Initial 2', emp)
        sigma_total = sum([ i['fitness'] for i in emp])

        # print(sigma_total)
        rand = random.uniform(0, 1)

        for i in range(self.population_size):
            prob = emp[i]['fitness'] / sigma_total

            if rand < prob:

                random_partner_source = random.choice(range(self.population_size))  # random partner [x1, x2]
                random_choice = random.choice(range(self.dim))  # random dimension 0 or 1

                x_old = emp[i]['candidate'][random_choice]

                xp = emp[random_partner_source]['candidate'][random_choice]

                F = random.uniform(-1, 1)

                x_new = round(x_old + F * (x_old - xp), 4)

                if x_new < self.lower_bound:
                    x_new = self.lower_bound
                elif x_new > self.upper_bound:
                    x_new = self.upper_bound
                else:
                    x_new = x_new

                old_source = emp[i]['candidate'].copy()

                new_source = emp[i]['candidate']


                new_source[random_choice] = x_new


                g = self.greedy_selection(old_source, new_source, emp[i]['trail'])

                emp[i]['candidate'] = g['candidate']
                emp[i]['fit'] = g['fit']
                emp[i]['fitness'] = g['fitness']
                emp[i]['trail'] = g['trail']

        # self.initial_pop = emp
        self.best = copy.deepcopy(self.best_solution(self.initial_pop))
        # print("After onlooker:-", self.best)
        # print([i['trail'] for i in emp])
        return self.initial_pop

    def scout_phase(self):
        """ 3. scout phase """
        # emp = self.onlooker_bee_phase()
        emp = self.initial_pop.copy()
        # print('Scout ')
        # print('Before scout:', self.best)

        change = False
        for s in range(self.population_size):
            trail = emp[s]['trail']

            if trail > self.limit :
                change = True
                SX = list()
                for j in range(self.dim):
                    n = self.lower_bound + random.uniform(0, 1) * (self.upper_bound - self.lower_bound)
                    SX.append(round(n, 4))

                emp[s]['candidate'] = SX
                emp[s]['fit'] = self.function(I=SX)
                emp[s]['fitness'] = self.fitness(self.function(I=SX))
                emp[s]['trail'] = 0
        if change:
            # self.initial_pop = emp
            self.best = copy.deepcopy(self.best_solution(self.initial_pop))
            # print('After scout:', self.best)

            # return self.initial_pop



if __name__ == '__main__':
    obj = ABC(population_size=5, iterations=50, dim=2, lower_bound=-5, upper_bound=5, limit=2)

    obj.initial_population()

    # print(obj.employee_bee_phase())

    for j in range(obj.iterations):
        print('Iteration:-:', j)
        obj.employee_bee_phase(iteration=j)
        obj.onlooker_bee_phase()
        obj.scout_phase()
        print(obj.best)
        print('====================')
    # print(obj.initial_pop)
    # print(json.dumps(obj.best, indent=5))
    # print(obj.best)




# if __name__ == '__main__':
#     obj= obj = ABC(population_size=5, iterations=50, dim=2, lower_bound=-5, upper_bound=5, limit=2)
#     print(obj.function([-5,5]))
#     print(obj.function([-5,4.7783]))