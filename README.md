# Study_Of_Knapsack_Problem

## Introduction
Imagine yourself going on a trip looking for a treasure so, after a tiring journey, you found the long-sought wealth.
Unfortunately, you weren't well prepared for such a great discovery as this treasure is full of different precious items and 
you hand only a knapsack that fits K kilograms, putting you in such a situation where you have to pick every item carefully
to get back with your back having the maximum value.

Knapsack problems are usually sub-problems of more complex combinatorial optimization problems, and most of them require
the selection of a subset of some given items resulting in the maximization of a profit sum, with the total assigned
weight not exceeding the capacity of the knapsack(s). All knapsack problems are classified as being NP-hard,
meaning that their optimal solutions cannot be obtained by the application of polynomial time algorithms.

## Applications
The knapsack problems have a variety of real life applications including
financial modeling, production and inventory management systems, stratified sampling,
design of queuing network models in manufacturing, and control of traffic overload in
telecommunication systems. Other areas of applications include yield management for
airlines, hotels and rental agencies, college admissions, quality adaptation and
admission control for interactive multimedia systems, cargo loading etc.

## Algorithms

### Brute Force

Complexity Analysis: 

Time Complexity: O(2^n). 
As there are redundant subproblems.
Auxiliary Space :O(1). 
As no extra data structure has been used for storing values.


### Dynamic Programming
Complexity Analysis: 

## Greedy 
This solution works perfectly for fractional Knapsack problem whereas It won't always give
the optimal solution in the case of 0/1 Knapsack problem. The idea is to find the object with 
heighest profit to weight ratio and put in the bag and if the bag doesn't fit the whole object 
put part of it such that it fits, so we will be looking for the maximal p/w value N times
in the worst case using binary search to do this will require Log(N) each time so we will have:
Time complixity: O(NLog(N)) 
Where N is the length of the array. 

Time Complexity: O(N*W). 
where ‘N’ is the number of weight element and ‘W’ is capacity. As for every weight element we traverse through all weight capacities 1<=w<=W.
Auxiliary Space: O(N*W). 
The use of 2-D array of size ‘N*W’.
