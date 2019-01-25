# import the necessary packages
import string
import numpy as np

# gene set to use for building password guesses
geneSet = [c for c in string.printable]
target = "Hello, World!"


def generate_parent(length):
    genes = np.random.choice(geneSet, length)
    return ''.join(genes)


def get_fitness(guess):
    fitness = sum(1 for expected, actual in zip(target, guess)
                  if expected == actual)
    return fitness
