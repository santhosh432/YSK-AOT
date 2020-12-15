#!/usr/bin/env python3
try:
    from sin_cosine import SinCosine
except:
    from .sin_cosine import SinCosine


class F2(SinCosine):
    """ F2 from paper """
    def fitness(self, p=list()):
        """ objective function for the problem
            input:
                p : list of elements with all dimension [x1, x2, x3, .... xn]

            output:
                squares of all elements * multiply with index

        """
        j = 0
        for i in range(len(p)):
            j = j + ((i + 1) * p[i] * p[i])
        return j

if __name__ == '__main__':
    obj = F2(population_size=6, max_iterations=100, upper_bound=10, lower_bound=-10, dim=10)
    obj.run()
    print('Best value :', obj.best_value)