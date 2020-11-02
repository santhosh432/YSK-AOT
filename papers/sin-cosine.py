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
                 lower_bound=None):
        self.populations_size = population_size
        self.max_iterations = max_iterations
        self.upper_bound = upper_bound
        self.lower_bound = lower_bound
        self.values = list()
        self.min_value = None
        self.best_value = None


    def fitness(self, x1 , x2):
        """ objective function for the problem """
        return x1 ** 2 + x2 **2

    def populations(self):
        """ set population """

        pop = [[round(random.uniform(self.lower_bound, self.upper_bound),2),
                round(random.uniform(self.lower_bound, self.upper_bound),2)] for _ in range(6)]
        print('Population :', pop)

        for i in range(self.populations_size):
            fit = self.fitness(pop[i][0], pop[i][1])
            self.values.append({'candidate': pop[i],
                                'fitness': fit})

        self.best_value = sorted(self.values, key = lambda x: x['fitness'])[0]['candidate']





if __name__ == '__main__':
    obj = SinCosine(population_size=6, max_iterations=100, upper_bound=500, lower_bound=-500)
    obj.populations()
    print(obj.values)
    v = obj.values
    b = obj.best_value
    stop = False
    for t in range(1, obj.max_iterations + 1):

        if stop:
            break
        r1 = (2 - 2 * (t / obj.max_iterations))

        for i in range(obj.populations_size):

            for j in range(2):
                r4 = random.uniform(0, 1)
                if r4 < 0.5:
                    v[i]['candidate'][j] = round(v[i]['candidate'][j] + r1 * (np.sin(2 * np.pi * round(random.uniform(0,1), 2)) * abs(random.uniform(0,1) * b[j] - v[i]['candidate'][j])), 2)

                else:
                    v[i]['candidate'][j] = round(v[i]['candidate'][j] + r1 * (np.cos(2 * np.pi * round(random.uniform(0,1), 2)) * abs(random.uniform(0,1) * b[j] - v[i]['candidate'][j])), 2)

                if v[i]['candidate'][j] < obj.lower_bound:
                    print('Lower ==================', v[i]['candidate'][j])

                    v[i]['candidate'][j] = obj.lower_bound
                elif v[i]['candidate'][j] > obj.upper_bound:
                    print('Upper ==================', v[i]['candidate'][j])

                    v[i]['candidate'][j] = obj.upper_bound

            v[i]['fitness'] = obj.fitness(v[i]['candidate'][0], v[i]['candidate'][1])

            if v[i]['fitness'] == 0:
                stop = True

            print(v[i])
        b = sorted(v, key = lambda x: x['fitness'])[0]['candidate']
        print('Best :', b)
    # print('Final', t)
    print(v)
    print(sorted(v, key = lambda x : x['fitness'])[0])
    print('Total Iterations:', t)














