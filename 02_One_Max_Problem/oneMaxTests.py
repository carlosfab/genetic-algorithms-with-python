# import the necessary packages
import unittest
import datetime

import genetic


def get_fitness(genes):
    return genes.sum()


def display(candidate, startTime):
    timeDiff = datetime.datetime.now() - startTime
    print("{0}...{1}\t{2:3.2f}\t{3}".format(
        ''.join(map(str, candidate.Genes[:5])),
        ''.join(map(str, candidate.Genes[-5:])),
        candidate.Fitness,
        timeDiff
    ))


class OneMaxTests(unittest.TestCase):
    geneSet = [0, 1]
    startTime = datetime.datetime.now()

    def test_10(self):
        length = 100
        self.optimise_one_max(length)

    def optimise_one_max(self, length):
        optimalFitness = length

        def fnGetFitness(genes):
            return get_fitness(genes)

        def fnDisplay(candidate):
            return display(candidate, self.startTime)

        best = genetic.get_best(fnGetFitness, length, optimalFitness,
                                self.geneSet, fnDisplay)

        self.assertEqual(length, best.Fitness)


if __name__ == '__main__':
    unittest.main()
