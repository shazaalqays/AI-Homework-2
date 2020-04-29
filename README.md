# AI-Homework-2
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
Mark the last cell as 5 for ending point.
```
Genes[99][99] = 5
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
