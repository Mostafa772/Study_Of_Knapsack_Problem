from main import *
import time
import numpy as np
from unittest import mock
import matplotlib.pyplot as plt

def fill_weights_rand(items_num):
    w = []

    for x in range(1, items_num + 1):
        z = random.random()
        while round(z * 100) == 0:
            z = random.random()
        w.append(round(z * 100))
    return w


def fill_profits_rand(items_num):
    p = []
    for x in range(1, items_num + 1):

        z = random.random()
        while round(z * 100) == 0:
            z = random.random()

        p.append(round(z * 100))
    return p


def calculate_time(sol):
    random.seed(10)
    running_time = []
    knapsack_size = [x for x in range(1,26)]
    for x in knapsack_size:
        items = round(x)
        max_weight = round(random.random() * 10)

        z = random.random()
        items_weight = fill_profits_rand(items)
        items_profit = fill_weights_rand(items)
        sol_one = sol(items, max_weight, items_weight, items_profit)
        start_time = time.monotonic()
        answer = sol_one.solution()
        end_time = time.monotonic()
        print("Starting time: %s Finishing time: %s Running time %s  Size: %s The answer: %s"%
              (start_time, end_time, end_time - start_time, x, answer))
        running_time.append(end_time - start_time)
    print("\n************************************************************************************\n")
    return running_time


knapsack_size = [x for x in range(1, 26)]
algorithm = ["Brute Force", "Dynamic Programming", "Greedy Solution"]

run_time_sols = []
for solution in [BruteForce, DynamicProgramming, GreedySolution]:
    run_time_sols.append(calculate_time(solution))
for item, algo in zip(run_time_sols, algorithm):
    plt.plot(knapsack_size, item, label=algo)

x1,x2,y1,y2 = plt.axis()
plt.axis((x1,x2,0,0.001))

plt.xlabel('input size')
plt.ylabel('time in seconds')
plt.legend()
plt.rcParams["figure.figsize"] = (10, 6)

plt.show()
