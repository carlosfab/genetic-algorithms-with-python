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


def _generate_parent(length, geneSet, get_fitness):
    genes = np.random.choice(geneSet, length)
    fitness = get_fitness(genes)
    return Chromossome(genes, fitness)


def _mutate(parent, geneSet, get_fitness):
    idx = np.random.randint(0, len(parent.Genes))
    childGenes = parent.Genes[:]
    newGene = np.random.choice(geneSet, 1)[0]
    childGenes[idx] = newGene
    fitness = get_fitness(childGenes)

    return Chromossome(childGenes, fitness)


def get_best(get_fitness, targetLen, optimalFitness, geneSet, display):
    np.random.seed()
    bestParent = _generate_parent(targetLen, geneSet, get_fitness)
    # display(bestParent)

    if bestParent.Fitness >= optimalFitness:
        return bestParent

    while True:
        child = _mutate(bestParent, geneSet, get_fitness)

        if bestParent.Fitness >= child.Fitness:
            continue

        bestParent = child

        # display(bestParent)

        if bestParent.Fitness >= optimalFitness:
            return bestParent
