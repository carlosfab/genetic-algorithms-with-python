# import the necessary packages
import string
import datetime
import unittest

import genetic

# gene set to use for building password guesses

target = "Hello, World!"


def get_fitness(genes, target):
    fitness = sum(1 for expected, actual in zip(target, genes)
                  if expected == actual)
    return fitness


def display(candidate, startTime):
    timeDiff = datetime.datetime.now() - startTime
    print("{0}\t{1}\t{2}".format(candidate.Genes, candidate.Fitness, timeDiff))


class GuessPasswordTests(unittest.TestCase):
    geneSet = [c for c in string.printable]

    def test_Hello_World(self):
        target = "Hello, World!"
        self.guess_password(target)

    
    def test_For_I_am_fearfully_and_wonrdefully_made(self):
        target = "For I am fearfully and wonderfully made."
        self.guess_password(target)


    def guess_password(self, target):
        startTime = datetime.datetime.now()

        def fnGetFitness(genes):
            return get_fitness(genes, target)

        def fnDisplay(candidate):
            return display(candidate, startTime)

        optimalFitness = len(target)
        best = genetic.get_best(fnGetFitness, len(target), optimalFitness, self.geneSet, fnDisplay)

        self.assertEqual(best.Genes, target)


if __name__ == '__main__':
    unittest.main()