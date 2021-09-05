# AI labyrinth of N * N
In a labyrinth of N * N, we have to finde the shortest path combining starting point which is the upper left  and end point the lower right, using genetic algorithm.
# Getting started
In order to work with labyrinthwe will use numpy library to work with matrices.
## Prerequisites
First of all, we need to install the package mentioned before  which is numby.
# Generate labyrinth
As mentioned before creating the labyrinth will be done by using numpy library. The labyrinth consist of two values 0 and 1. In `main` function write the part of code bellow.
```
Genes = np.random.randint(2 , size=(100,100))
```
Mark the first cell as 1 for starting point.
```
Genes[0][0] = 1
```
Mark the last cell as 6 for ending point.
```
Genes[99][99] = 6
```
# Finding the path
As declared before we will be using Genetic algorithm in order to find the path between starting point and end point. 
## Genetic algorithm
A genetic algorithm is a search heuristic that is inspired by Charles Darwin’s theory of natural evolution. This algorithm reflects the process of natural selection where the fittest individuals are selected for reproduction in order to produce offspring of the next generation.
Five phases are considered in a genetic algorithm.
* Initial population
* Fitness function
* Selection
* Crossover
* Mutation
### Pseudocode
START
Generate the initial population
Compute fitness
REPEAT
    Selection
    Crossover
    Mutation
    Compute fitness
UNTIL population has converged
STOP
### Initialize population
The process begins with a set of individuals, each individual is a solution to the problem we want to solve. "An individual is characterized by a set of variables known as Genes. Genes are joined into a string to form a Chromosome (solution)."
So we define a function which creates our population as follow in function `generatePop`.
```
def generatePop(sizeOfPop):
    pop = []
    # Random generation of population
    for i in range(sizeOfPop):
        # The population will be in range 1 - 4 not incuding 0's
        pop.append(np.random.randint(low = 1, high = 5))
    return pop
```
The population consist of 4 different values which represent our moves. 1 to move left, 2 to move up, 3 to move right and 4 to move down.
### Fitness function
In this function we assume that up from starting point down to ending point obly childs or chromosomes who has more right and down moves have higher fitness score. see the function `fitness`.
```
def fitness(pop):
    fitness = 0
    for i in range(len(pop)):
        if pop[i] == 3 or pop[i] == 4:
            fitness = fitness + 1
    return fitness
```
### Selection function
In this function we will select the chromosome which has higher fitness score to continue with. See fonction `selection`.
```
def selection(pop):
    max = 0
    x = generateChild(pop)
    for i in x:
        y = fitness(i)
        if y > max:
            max = y
            child = i
    return child
```
### Crossover function
In this part we will generate parents and their children by making some mathematical operations. In our case we create 2 parents and 4 children at each iteration and add them to the list childs. See function `generateChild`
```
def generateChild(pop):
    # As many childs we have as the result is better
    childs = []
    child1 = []
    child2 = []
    child3 = []
    child4 = []
    # Prepare parents first
    length = len(pop)
    middle_index = length//2
    parent1 = pop[:middle_index]
    parent2 = pop[middle_index:]
```
Create child1 by adding the parent1 to parent2
```
    for i in range(len(parent1)):
        solu = parent1[i]+parent2[i]
        if solu > 4:
            solu = solu //2
        child1.append(solu)
    childs.append(child1)
````
Create child2 by subtracting parent1 from pareent2
```
    for i in range(len(parent1)):
        solu = parent1[i]-parent2[i]
        if solu < 1:
            solu = solu * -1
        if solu > 4:
            solu = solu //2
        child2.append(solu)
    childs.append(child2)
```
Create child3 by multiplying parent1 by parent2
```
    for i in range(len(parent1)):
        solu = parent1[i]*parent2[i]
        if solu < 1:
            solu = solu * -1
        if solu > 4:
            solu = solu //4
        child3.append(solu)
    childs.append(child3)
```
Create child4 by dividing parent1 by parent2
```
    for i in range(len(parent1)):
        solu = parent1[i]//parent2[i]
        if solu < 1:
            solu = solu * -1
            if solu > 4:
                solu = solu//4
        if solu > 4:
            solu = solu //4
        child4.append(solu)
    childs.append(child4)
    return childs
```
### Mutation function
Here in mutation function we select a gene randomly and change its value. See function below.
```
def updatingChild(childs):
    x = np.array(childs)
    # Randomly change genes of child1
    mask = np.random.randint(1,2,size=x.shape).astype(np.bool)
    r = np.random.rand(*x.shape)*np.max(x)
    x[mask] = r[mask]
    for i in x:
        if i == 0:
            i = np.random.randint(low = 1, high=5)
    return x
```
### Find path function
Lastly, in `findpath` function we will call all the functions created before and try to find the path.
```
def findPath(Genes, GenerationNum):

    # Start with generation 0
    for k in range(GenerationNum):
        print("Generation: ", k)
        path = []
        start1 = 0
        start2 = 0

        # Generate Population
        x = generatePop(10000)

        # Calculate fitness
        y = fitness(x)

        # Selection function
        p = selection(x)

        # Update childs or mutate child
        z = updatingChild(p)

        # For each child in Updated childs set
        for i in z:
            # Start with labyrinth if the cell equal 1
            if Genes[start1][start2] == 1:
                # if the gene was 0 then no move
                if i == 0:
                    print("no move" , i)
                    # return
                # if gene equal 1 then move left
                elif i == 1:
                    # i = i+1
                    start2 = start2-1
                    # add the cell to the path
                    path.append(Genes[start1][start2])
                    print("left ", i)
                # if gene equal 2 then move up
                elif i == 2:
                    # i = i+1
                    start1 = start1-1
                    # add the cell to the path
                    path.append(Genes[start1][start2])
                    print("up ", i)
                # if gene equal 3 then move right
                elif i == 3:
                    # i = i+1
                    start2 = start2+1
                    # add the cell to the path
                    path.append(Genes[start1][start2])
                    print("right", i)
                # if gene equal 4 then move down
                elif i == 4:
                    # i = i+1
                    start1 =start1+1
                    # add the cell to the path
                    path.append(Genes[start1][start2])
                    print("down ", i)
            # if cell is 5 then we found the goal
            elif Genes[start1][start2] == 6:
                print(path)
                return path
            # if cell is 0 then there is a wall
            elif Genes[start1][start2] == 0:
                s = start1
                start1 = start2
                start2  = s
                # print("wall")
    return print("No path")
```
# Conclusion
Genetic algorithm is a fast and optimal solution for such a problem.
# Prepared by
Chaza Alkis
