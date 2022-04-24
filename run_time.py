from main import *
import time
import numpy as np
from unittest import mock
import matplotlib.pyplot as plt


def fill_weights_rand(items_num):
    w = []

    for x in range(1, items_num + 1):
        z = random.random()
        while round(z * 10) == 0:
            z = random.random()
        w.append(round(z * 10))
    return w


def fill_profits_rand(items_num):
    p = []
    for x in range(1, items_num + 1):

        z = random.random()
        while round(z * 10) == 0:
            z = random.random()

        p.append(round(z * 10))
    return p


def draw_graph(run_time_brute, run_time_dp, run_time_greedy):

    y_points = np.array([run_time_greedy, run_time_dp, run_time_brute])

    list_of_markers = ["greedy", "dp", "brute force"]

    plt.xlabel("Solving Algorithm", fontsize=14)
    plt.ylabel("Running Time", fontsize=14)
    plt.plot(list_of_markers, y_points, marker='o')
    plt.show()


run_avg_br = 0
run_avg_dp = 0
run_avg_gr = 0


@mock.patch('main.input', create=True)
def calculate_time(mocked_input):
    functions = [BruteForce, DynamicProgramming, GreedySolution]
    counter = 0
    time_sum = 0
    time_sum_dp = 0
    time_sum_gr = 0
    for sol in functions:

        for x in range(1, 21):

            counter += 1
            items = round(random.random() * 10) + 3
            max_weight = round(random.random() * 10)

            z = random.random()
            sol_one = BruteForce(items, max_weight)
            sol_two = DynamicProgramming(items, max_weight)
            sol_three = GreedySolution(items, max_weight)
            sol_one.items_weight = fill_profits_rand(items)
            sol_one.items_profit = fill_weights_rand(items)

            sol_two.items_weight = fill_profits_rand(items)
            sol_two.items_profit = fill_weights_rand(items)

            sol_three.items_weight = fill_profits_rand(items)
            sol_three.items_profit = fill_weights_rand(items)

            start_time = time.monotonic() * 1000
            sol_one.solution()
            end_time = time.monotonic() * 1000
            time_sum += end_time - start_time

            start_time = time.monotonic() * 1000
            sol_two.solution()
            end_time = time.monotonic() * 1000
            time_sum_dp += end_time - start_time

            start_time = time.monotonic() * 1000
            sol_three.solution()
            end_time = time.monotonic() * 1000
            time_sum_gr += end_time - start_time

    print(time_sum/60, time_sum_dp / 60, time_sum_gr/60)
    draw_graph(time_sum/60, time_sum_dp/60, time_sum_gr/60)


calculate_time()
