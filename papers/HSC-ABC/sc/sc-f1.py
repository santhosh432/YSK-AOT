#!/usr/bin/env python3
try:
    from sin_cosine import SinCosine
except:
    from .sin_cosine import SinCosine


class F1(SinCosine):
    """ F1 from paper """
    def fitness(self, p=list()):
        """ objective function for the problem
            input:
                p : list of elements with all dimension [x1, x2, x3, .... xn]

            output:
                squares of all elements

        """
        return sum([i * i for i in p])

if __name__ == '__main__':
    obj = F1(population_size=6, max_iterations=100, upper_bound=100, lower_bound=-100, dim=10)
    obj.run()
    print('Best value :', obj.best_value)