import random 
import math
import matplotlib.pyplot as plt
import copy


# Customization section: 
def objective_function(X):
    x=X[0]
    y=X[1]
    value= x**2 + y
    return value

# Simulated Annealing Algorithm:
initial_solution = [-1, 14]
# prob = [0.593054, 0.29857, 0.504246, 0.376256, 0.942043, 0.496899, 0.093536, 0.093536]
current_solution =  initial_solution 
best_solution = initial_solution

best_fitness = objective_function(best_solution)
initial_temperature = 1
current_temperature = initial_temperature # current temperature

no_attempts = 2 # number of attempts in each level of temperature
record_best_fitness =[]
record_best_fitness.append(best_fitness)
for i in range (10000):

    for j in range(no_attempts):
        if (i!=0 or j!=0):
            current_solution[0] = best_solution [0] + 0.5
            current_solution[1] = best_solution [1] + 0.5
        
        # print(current_solution)
        current_fitness = objective_function(current_solution)
        E = abs(current_fitness - best_fitness)
        # print("current_fitness", current_fitness)

        print('current_temperature: ',current_temperature)
        print('best solution: ', best_solution)
        print('current solution: ', current_solution)
        print('E: ', E)
        print('best fitness: ', best_fitness)
        print('current fitness: ', current_fitness)
        
        # print()
        if current_fitness > best_fitness:                  # get a worse solution

            m = math.exp(E/ current_temperature)
            p = random.random()
            # p = prob.pop(0)
            print("Simulated Annealing value: ", current_fitness)
            print('p:', round(p,2))
            print('m:', round(m,2))
            print()
            if p<m:           # making a decision to accept the worse solution or not if p < m:

                accept = True # this worse solution is accepted
            else: 
                accept = False # this worse solution is not accepted
        
        else: 
            accept = True # accept better solution
            print()    

        if accept == True:
            best_solution = copy.deepcopy(current_solution) # update the best solution
            best_fitness =  objective_function(best_solution)

        record_best_fitness.append(best_fitness) 

    current_temperature = round(0.8 * current_temperature - 1, 2)

plt.plot(record_best_fitness)
plt.show()
