import random


def mutation(chromosome):
    chromosome = list(chromosome)
    for bit in range(len(chromosome)):
        randomNum = random.random()
        if randomNum <= 0.01:
            if chromosome[bit] == '0':
                chromosome[bit] = '1'
            elif chromosome[bit] == '1':
                chromosome[bit] = '0'

    chromosome = "".join(chromosome)            
    return chromosome
