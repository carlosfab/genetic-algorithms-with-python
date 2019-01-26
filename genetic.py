# import the necessary packages
import numpy as np
import time
import statistics
import sys


class Chromossome(object):
    Genes = None
    Fitness = None

    def __init__(self, genes, fitness):
        self.Genes = genes
        self.Fitness = fitness


class Benchmark(object):
    @staticmethod
    def run(function):
        timings = []
        stdout = sys.stdout
        for i in range(100):
            stdout = None
            startTime = time.time()
            function()
            seconds = time.time() - startTime
            sys.stdout = stdout
            timings.append(seconds)
            mean = statistics.mean(timings)

            if i < 10 or i % 10 == 9:
                print("{0} {1:3.2f} {2:3.2f}".format(
                    1 + i, mean,
                    statistics.stdev(timings, mean)
                    if i > 1 else 0
                ))


def _generate_parent(length, geneSet, get_fitness):
    genes = np.random.choice(geneSet, length)
    genes = ''.join(genes)
    fitness = get_fitness(genes)
    return Chromossome(genes, fitness)


def _mutate(parent, geneSet, get_fitness):
    idx = np.random.randint(0, len(parent.Genes))
    childGenes = list(parent.Genes)
    newGene = np.random.choice(geneSet, 1)[0]
    childGenes[idx] = newGene
    genes = ''.join(childGenes)
    fitness = get_fitness(genes)
    return Chromossome(genes, fitness)


def get_best(get_fitness, targetLen, optimalFitness, geneSet, display):
    np.random.seed()
    bestParent = _generate_parent(targetLen, geneSet, get_fitness)
    display(bestParent)

    if bestParent.Fitness >= optimalFitness:
        return bestParent

    while True:
        child = _mutate(bestParent, geneSet, get_fitness)

        if bestParent.Fitness >= child.Fitness:
            continue

        bestParent = child

        display(bestParent)

        if bestParent.Fitness >= optimalFitness:
            return bestParent