# import the necessary packages
import numpy as np
import unittest

import genetic


def get_fitness(genes):
    return genes.sum()


#TODO
def display(candidate, startTime):
    return None


class OneMaxTests(unittest.TestCase):
    geneSet = [0, 1]

    def test_10(self):
        length = 10
        self.optimise_one_max(length)

    #TODO
    def optimise_one_max(self, length):
        optimalFitness = length

        best = genetic.get_best(get_fitness, length, optimalFitness,
                         self.geneSet, display)
        self.assertEqual(length, best.Fitness)


if __name__ == '__main__':
    unittest.main()
