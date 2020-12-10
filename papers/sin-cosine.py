"""
author: YSk
Topic: Sin cosine optimization algorithm
"""
import random
import numpy as np

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


    def fitness(self, x1 , x2):
        """ objective function for the problem """
        return x1 ** 2 + x2 **2

    def random_uniform(self):
        """ random two decimal point eg: 0.00 """
        r = random.uniform(0,1)
        return round(r,2)


    def populations(self):
        """ set population """

        # Population : [[3.53, -1.69], [-3.59, 0.34], [-4.29, -1.95], [2.08, -4.75], [0.14, -3.02], [1.39, 4.92]]

        pop = [[round(random.uniform(self.lower_bound, self.upper_bound),2),
                round(random.uniform(self.lower_bound, self.upper_bound),2)] for _ in range(6)]


        # Population : [[5, -5], [2, 3], [-3, 5], [1, 2], [-5, -4], [-4, -4]]
        # pop = [[random.randint(self.lower_bound, self.upper_bound), random.randint(self.lower_bound, self.upper_bound)] for _ in range(6)]

        print('Population :', pop)

        for i in range(self.populations_size):
            fit = self.fitness(pop[i][0], pop[i][1])
            self.values.append({'candidate': pop[i],
                                'fitness': fit})

        self.best_value = sorted(self.values, key = lambda x: x['fitness'])[0]['candidate']

    def run(self):
        """ run process """
        self.populations()
        stop = False
        for t in range(1, self.max_iterations + 1):
            # run over iterations
            print("Iteration number:-", t)
            if stop:
                break
            r1  = (2 - 2 * (t / self.max_iterations))
            for i in range(self.populations_size):

                # run all possible solution
                for j in range(self.dim):
                    # dimension of problem eg: x1, x2 (total parameters)
                    r4 = self.random_uniform()

                    if r4 < 0.5:
                        v = round(self.values[i]['candidate'][j] + r1 * np.sin(2 * np.pi * self.random_uniform()) * abs(self.random_uniform() * self.best_value[j] - self.values[i]['candidate'][j]), 2)
                        self.values[i]['candidate'][j] = v
                    else:
                        v = round(self.values[i]['candidate'][j] + r1 * np.cos(2 * np.pi * self.random_uniform()) * abs(self.random_uniform() * self.best_value[j] - self.values[i]['candidate'][j]), 2)
                        self.values[i]['candidate'][j] = v

                    if self.values[i]['candidate'][j] < self.lower_bound:
                        print('Lower ==================', self.values[i]['candidate'][j])

                        self.values[i]['candidate'][j] = self.lower_bound
                    elif self.values[i]['candidate'][j] > self.upper_bound:
                        print('Upper ==================', self.values[i]['candidate'][j])

                        self.values[i]['candidate'][j] = self.upper_bound
                    else:
                        pass

                self.values[i]['fitness'] = self.fitness(self.values[i]['candidate'][0], self.values[i]['candidate'][1])

                if self.values[i]['fitness'] == 0:
                    stop = True

                print(self.values[i])
            self.best_value = sorted(self.values, key = lambda x: x['fitness'])[0]['candidate']


if __name__ == '__main__':
    obj = SinCosine(population_size=6, max_iterations=100, upper_bound=5, lower_bound=-5, dim=2)
    obj.run()
    print('Best value :', obj.best_value)



# if __name__ == '__main__':
#
#     obj = SinCosine(population_size=6, max_iterations=100, upper_bound=5, lower_bound=-5, dim=2)
#
#     for i in range(10):
#         print(obj.random_uniform())
