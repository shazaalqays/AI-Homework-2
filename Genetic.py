import numpy as np

# wall = 0
# left = 1
# up = 2
# right = 3
# down = 4
# found = 5

# Function to create a population
def generatePop(sizeOfPop):
    pop = []
    # Random generation of population
    for i in range(sizeOfPop):
        # The population will be in range 1 - 4 not incuding 0's
        pop.append(np.random.randint(low = 1, high = 5))
    return pop

def fitness(pop):
    fitness = 0
    for i in range(len(pop)):
        if pop[i] == 3 or pop[i] == 4:
            fitness = fitness + 1
    return fitness

# Geneation of childs or we can say crossover function
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

    # Create child1 by adding the parent1 to parent2
    for i in range(len(parent1)):
        solu = parent1[i]+parent2[i]
        if solu > 4:
            solu = solu // 2
        child1.append(solu)
    childs.append(child1)
    #print(childs)
    # Create child2 by subtracting parent1 from pareent2
    for i in range(len(parent1)):
        solu = parent1[i]-parent2[i]
        if solu < 1:
            solu = solu * -1
        if solu > 4:
            solu = solu //2
        child2.append(solu)
    childs.append(child2)
    # Create child3 by multiplying parent1 by parent2
    for i in range(len(parent1)):
        solu = parent1[i]*parent2[i]
        if solu < 1:
            solu = solu * -1
        if solu > 4:
            solu = solu //4
        child3.append(solu)
    childs.append(child3)
    # Create child4 by dividing parent1 by parent2
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
    # print(childs)
    return childs

def selection(pop):
    max = 0
    x = generateChild(pop)
    for i in x:
        y = fitness(i)
        if y > max:
            max = y
            child = i
    return child

# Function to change the childs genes or we can say Mutation function
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

#
# Genes = [[1,1,0,1,1,0,0,1,1,1,0,1,1,0,1,1,0,1,0,1],
#          [0,1,1,1,1,0,1,1,0,1,1,1,0,0,1,1,1,1,1,0],
#          [1,0,1,0,1,1,1,1,1,0,1,1,1,0,0,0,0,1,1,1],
#          [1,0,1,1,0,1,1,1,1,0,0,1,0,0,1,1,1,1,0,0],
#          [1,0,0,0,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,0],
#          [1,0,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1],
#          [0,1,1,1,1,0,1,1,0,0,0,1,0,0,0,1,1,1,1,1],
#          [0,1,1,1,1,0,1,1,0,1,1,1,0,0,1,1,1,1,1,0],
#          [0,1,1,1,1,0,1,1,0,0,0,1,0,0,0,1,1,1,1,1],
#          [1,1,0,0,1,0,0,1,1,1,1,0,0,1,1,1,0,1,0,0],
#          [1,0,0,0,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,0],
#          [1,1,0,1,1,0,0,1,1,1,0,1,1,0,1,1,0,1,0,1],
#          [1,1,0,0,1,0,0,1,1,1,1,0,0,1,1,1,0,1,0,0],
#          [1,0,1,0,1,1,1,1,1,0,1,1,1,0,0,0,0,1,1,1],
#          [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1],
#          [1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,0,0,0,0],
#          [0,0,0,1,1,1,1,0,0,1,1,0,1,0,1,0,1,1,1,1],
#          [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
#          [1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1],
#          [1,0,0,1,1,1,1,1,1,0,1,1,1,1,1,0,0,1,1,1]]

# Create labyrinth randomly
Genes = np.random.randint(2 , size=(40,40))
# print(Genes)

# Mark the first cell as 1 for starting point
Genes[0][0] = 1

# Mark the last cell as 5 for ending point
Genes[39][39] = 6

print(Genes)

# Give generation number
GenerationNum = 10

# Find the path
p = findPath(Genes, GenerationNum)
# print(p)
