# import the necessary packages
import numpy as np


def _generate_parent(length, geneSet):
    genes = np.random.choice(geneSet, length)
    return ''.join(genes)


def _mutate(parent, geneSet):
    idx = np.random.randint(0, len(parent))
    childGenes = list(parent)
    newGene = np.random.choice(geneSet, 1)[0]
    childGenes[idx] = newGene
    return ''.join(childGenes)


def get_best(get_fitness, targetLen, optimalFitness, geneSet, display):
    np.random.seed()
    bestParent = _generate_parent(targetLen, geneSet)
    bestFitness = get_fitness(bestParent)
    display(bestParent)

    if bestFitness >= optimalFitness:
        return bestParent

    while True:
        child = _mutate(bestParent, geneSet)
        childFitness = get_fitness(child)

        if bestFitness >= childFitness:
            continue

        bestParent = child
        bestFitness = childFitness

        display(bestParent)

        if bestFitness >= optimalFitness:
            return bestParent