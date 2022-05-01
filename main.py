from abc import ABC, abstractmethod
from itertools import chain, combinations
import random


# Class Knapsack will take as input first the capacity of the knapsack
# then the number of the items K and finally the value of each item

# a function to get all subsets of a set
def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


# Getting input from the user and if wrong we let him enter again
def get_input():
    while True:
        try:
            value = int(input())
            break
        except ValueError:
            print("knapsack only accepts integer values please try again")

    return value


class Knapsack:

    def __init__(self, init_max_items, init_max_weight, items_weights, items_profits):
        self.items_weight = items_weights
        self.items_profit = items_profits
        self.max_weight = init_max_weight
        self.max_items = init_max_items

    def __str__(self):
        return f"""The number of items we have is: {str(self.max_items)} and the max_weight of the knapsack is: {str(self.max_weight)} 
and the items have the weights of {self.items_weight} and profit of {self.items_profit}"""

    @abstractmethod
    def solution(self):
        pass


class BruteForce(Knapsack):

    def solution(self):

        max_profit = 0

        for p, w in zip(powerset(self.items_profit), powerset(self.items_weight)):
            if sum(w) > self.max_weight or len(w) > self.max_items:
                continue
            elif sum(p) > max_profit:
                max_profit = sum(p)

        return max_profit


class DynamicProgramming(Knapsack):

    def solution(self):
        table = [[0 for x in range(self.max_weight + 1)] for y in range(self.max_items + 1)]
        i = 0

        while i < self.max_items + 1:
            j = 0

            while j < self.max_weight + 1:
                if i == 0 or j == 0:
                    table[i][j] = 0

                elif self.items_weight[i - 1] <= j:
                    table[i][j] = max(table[i - 1][j],
                                      table[i - 1][j - self.items_weight[i - 1]] + self.items_profit[i - 1])

                else:
                    table[i][j] = table[i - 1][j]

                j += 1
            i += 1
        return table[self.max_items][self.max_weight]


# Greedy solution for fractional Knapsack problem
# It will give optimal solution here but in case of
# 0/1 knapsack problem it won't always give the
# optimal solution
class GreedySolution(Knapsack):

    def solution(self):
        
        if sum(self.items_weight) < self.max_weight:
            return sum(self.items_profit)
        
        weight_to_profit = [(p / w) for w, p in zip(self.items_weight, self.items_profit)]
        sum_of_weight = 0
        max_profit = 0

        while sum_of_weight < self.max_weight:
            index = weight_to_profit.index(max(weight_to_profit))

            if (sum_of_weight + self.items_weight[index]) <= self.max_weight:
                sum_of_weight += self.items_weight[index]
                max_profit += self.items_profit[index]
                weight_to_profit[index] = -1

            else:
                ratio = ((self.max_weight - sum_of_weight) / self.items_weight[index])
                sum_of_weight += ratio * self.items_weight[index]
                max_profit += ratio * self.items_profit[index]
                weight_to_profit[index] = -1

        return max_profit
