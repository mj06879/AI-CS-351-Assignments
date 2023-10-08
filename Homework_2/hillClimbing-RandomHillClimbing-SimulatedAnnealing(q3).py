import random
import time
import math
from matplotlib import pyplot as plt

def generateRandomCoordinate():
    x = random.uniform(-2, 2)
    y = random.uniform(-1, 3)
    return [x,y]

def fitnessEvaluation(coordinate):
    x = coordinate[0]
    y = coordinate[1]
    fitness = 100*(x**2 - y**2) + (1-x)**2
    return fitness

def getNeighbours(coordinate):
    x = coordinate[0]
    y = coordinate[1]
    stepSize = 0.1
    neighbours = []

    if (x+stepSize <= 2):
        neighbours.append([x+stepSize, y])
    if (x-stepSize >= -2):
        neighbours.append([x-stepSize, y])
    if (y+stepSize <= 3):
        neighbours.append([x, y+stepSize])
    if (y-stepSize >= -1):
        neighbours.append([x, y-stepSize])

    return neighbours


def getRandomNeighbour(coordinate):
    x = random.uniform(-2, 2)
    y = random.uniform(-1, 3)
    while [x,y] == coordinate:
        x = random.uniform(-2, 2)
        y = random.uniform(-1, 3)

    return [x, y]


def hillClimbing(currentPoint, iterations):
    bestFitness = fitnessEvaluation(currentPoint)
    fitnesses = []

    for iteration in range(iterations):
        neighbours = getNeighbours(currentPoint)
        for neighbour in neighbours:
            neighbourFitness = fitnessEvaluation(neighbour)
            if neighbourFitness > bestFitness:
                currentPoint = neighbour
                bestFitness = neighbourFitness
        
        fitnesses.append(bestFitness)

    return fitnesses



def randomHillClimbing(currentPoint, iterations):
    bestFitness = fitnessEvaluation(currentPoint)
    fitnesses = []

    for iteration in range(iterations):
        neighbour = getRandomNeighbour(currentPoint)
        neighbourFitness = fitnessEvaluation(neighbour)
        if neighbourFitness > bestFitness:
            currentPoint = neighbour
            bestFitness = neighbourFitness

        fitnesses.append(bestFitness)

    return fitnesses



def simulatedAnnealing(currentPoint, iterations):
    fitness = fitnessEvaluation(currentPoint)
    initialTemperature = 100
    fitnesses = []
    temperatures = []
    probabilites = []

    for iteration in range(iterations):
        temperature = initialTemperature/float(iteration+1)
        neighbour = getRandomNeighbour(currentPoint)
        neighbourFitness = fitnessEvaluation(neighbour)
        delta = neighbourFitness - fitness
        if delta > 0:
            currentPoint = neighbour
            fitness = neighbourFitness
            probabilites.append(0)
        else:
            m = math.exp(delta/temperature)
            p = random.random()
            probabilites.append(m)
            if p < m:
                currentPoint = neighbour
                fitness = neighbourFitness
        
        fitnesses.append(fitness)
        temperatures.append(temperature)
        
    return fitnesses, temperatures, probabilites


def graphMaker():

    fitness10HC = []
    fitness100HC = []
    fitness500HC = []

    fitness10RHC = []
    fitness100RHC = []
    fitness500RHC = []

    fitness10SA = []
    fitness100SA = []
    fitness500SA = []

    temp10SA = []
    temp100SA = []
    temp500SA = []

    prob10SA = []
    prob100SA = []
    prob500SA = []


    for i in range(10):
        currentPoint = generateRandomCoordinate()

        tenIterationsHC = hillClimbing(currentPoint, 10)
        hundredIterationsHC = hillClimbing(currentPoint, 100)
        fiveHundredIterationsHC = hillClimbing(currentPoint, 500)

        tenIterationsRHC = randomHillClimbing(currentPoint, 10)
        hundredIterationsRHC = randomHillClimbing(currentPoint, 100)
        fiveHundredIterationsRHC = randomHillClimbing(currentPoint, 500)

        result10 = simulatedAnnealing(currentPoint, 10)
        tenIterationsSA = result10[0]
        tenIterationsSATemp = result10[1]
        tenIterationsSAProb = result10[2]

        result100 = simulatedAnnealing(currentPoint, 100)
        hundredIterationsSA = result100[0]
        hundredIterationsSATemp = result100[1]
        hundredIterationsSAProb = result100[2]

        result500 = simulatedAnnealing(currentPoint, 500)
        fiveHundredIterationsSA = result500[0]
        fiveHundredIterationsSATemp = result500[1]
        fiveHundredIterationsSAProb = result500[2]


        fitness10HC.append(tenIterationsHC)
        fitness100HC.append(hundredIterationsHC)
        fitness500HC.append(fiveHundredIterationsHC)

        fitness10RHC.append(tenIterationsRHC)
        fitness100RHC.append(hundredIterationsRHC)
        fitness500RHC.append(fiveHundredIterationsRHC)

        fitness10SA.append(tenIterationsSA)
        fitness100SA.append(hundredIterationsSA)
        fitness500SA.append(fiveHundredIterationsSA)

        temp10SA.append(tenIterationsSATemp)
        temp100SA.append(hundredIterationsSATemp)
        temp500SA.append(fiveHundredIterationsSATemp)

        prob10SA.append(tenIterationsSAProb)
        prob100SA.append(hundredIterationsSAProb)
        prob500SA.append(fiveHundredIterationsSAProb)


    avg10HC = [sum(x)/10 for x in zip(*fitness10HC)]
    avg100HC = [sum(x)/10 for x in zip(*fitness100HC)]
    avg500HC = [sum(x)/10 for x in zip(*fitness500HC)]
    avg10RHC = [sum(x)/10 for x in zip(*fitness10RHC)]
    avg100RHC = [sum(x)/10 for x in zip(*fitness100RHC)]
    avg500RHC = [sum(x)/10 for x in zip(*fitness500RHC)]
    avg10SA = [sum(x)/10 for x in zip(*fitness10SA)]
    avg100SA = [sum(x)/10 for x in zip(*fitness100SA)]
    avg500SA = [sum(x)/10 for x in zip(*fitness500SA)]

    avg10SATemp = [sum(x)/10 for x in zip(*temp10SA)]
    avg100SATemp = [sum(x)/10 for x in zip(*temp100SA)]
    avg500SATemp = [sum(x)/10 for x in zip(*temp500SA)]

    avg10SAProb = [sum(x)/10 for x in zip(*prob10SA)]
    avg100SAProb = [sum(x)/10 for x in zip(*prob100SA)]
    avg500SAProb = [sum(x)/10 for x in zip(*prob500SA)]


    plt.plot(list(range(1,11)), avg10HC, label = "Hill Climbing")
    plt.plot(list(range(1,11)), avg10RHC, label = "Random Hill Climbing")
    plt.plot(list(range(1,11)), avg10SA, label = "Simulated Annealing")
    plt.title("Comparison of Fitness Convergence for 10 iterations")
    plt.xlabel("Iterations")
    plt.ylabel("Fitness Value")
    plt.legend()
    plt.grid()
    plt.show()

    plt.plot(list(range(1,101)), avg100HC, label = "Hill Climbing")
    plt.plot(list(range(1,101)), avg100RHC, label = "Random Hill Climbing")
    plt.plot(list(range(1,101)), avg100SA, label = "Simulated Annealing")
    plt.title("Comparison of Fitness Convergence for 100 iterations")
    plt.xlabel("Iterations")
    plt.ylabel("Fitness Value")
    plt.legend()
    plt.grid()
    plt.show()

    plt.plot(list(range(1,501)), avg500HC, label = "Hill Climbing")
    plt.plot(list(range(1,501)), avg500RHC, label = "Random Hill Climbing")
    plt.plot(list(range(1,501)), avg500SA, label = "Simulated Annealing")
    plt.title("Comparison of Fitness Convergence for 500 iterations")
    plt.xlabel("Iterations")
    plt.ylabel("Fitness Value")
    plt.legend()
    plt.grid()
    plt.show()

    plt.plot(list(range(1,11)), avg10SATemp, label = "Temperature")
    plt.title("Temperature Decay for 10 iterations")
    plt.xlabel("Iterations")
    plt.ylabel("Temperature Value")
    plt.legend()
    plt.grid()
    plt.show()

    plt.plot(list(range(1,101)), avg100SATemp, label = "Temperature")
    plt.title("Temperature Decay for 100 iterations")
    plt.xlabel("Iterations")
    plt.ylabel("Temperature Value")
    plt.legend()
    plt.grid()
    plt.show()

    plt.plot(list(range(1,501)), avg500SATemp, label = "Temperature")
    plt.title("Temperature Decay for 500 iterations")
    plt.xlabel("Iterations")
    plt.ylabel("Temperature Value")
    plt.legend()
    plt.grid()
    plt.show()

    plt.plot(list(range(1,11)), avg10SAProb, label = "Probability of Selecting a Bad State")
    plt.title("Probability Decay for 10 iterations")
    plt.xlabel("Iterations")
    plt.ylabel("Probability Value")
    plt.legend()
    plt.grid()
    plt.show()

    plt.plot(list(range(1,101)), avg100SAProb, label = "Probability of Selecting a Bad State")
    plt.title("Probability Decay for 100 iterations")
    plt.xlabel("Iterations")
    plt.ylabel("Probability Value")
    plt.legend()
    plt.grid()
    plt.show()

    plt.plot(list(range(1,501)), avg500SAProb, label = "Probability of Selecting a Bad State")
    plt.title("Probability Decay for 500 iterations")
    plt.xlabel("Iterations")
    plt.ylabel("Probability Value")
    plt.legend()
    plt.grid()
    plt.show()




graphMaker()

