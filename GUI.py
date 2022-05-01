from main import *
import tkinter as tk
from tkinter import *
import ast
from functools import partial
from unittest import mock

window = tk.Tk()

count = 1


def clicked():  # without event because I use `command=` instead of `bind`
    global count
    count = count + 1


# Label for number of items
var = StringVar()
label = Label(window, textvariable=var)
var.set("Number of items:")
label.pack(padx=20, pady=10)

num_of_items = 0


def get_num_of_items():
    global num_of_items
    num_of_items = int(items_num_ent.get())


items_num_ent = tk.Entry(window, width=40)
items_num_ent.pack(padx=20, pady=5)
items_num_ent.pack(pady=10)
# btn = tk.Button(window, height=1, width=20, text="Read num of items", command=get_num_of_items)
# btn.pack(pady=20)

# Label for the maximum weight
var = StringVar()
label = Label(window, textvariable=var)
var.set("Maximum weight:")
label.pack(padx=20, pady=10)

max_weight = 0


def get_max_weight():
    global max_weight
    max_weight = int(max_weight_ent.get())


max_weight_ent = tk.Entry(window, width=40)
max_weight_ent.pack(padx=20, pady=5)
max_weight_ent.pack(pady=10)
# btn = tk.Button(window, height=1, width=20, text="Read max weight", command=get_max_weight)
# btn.pack(pady=20)

# Label for profit entries
var = StringVar()
label = Label(window, textvariable=var)
var.set("Enter weight for item number : %s" % count)

label.pack(pady=10)
weights = []


def get_weight():
    weights.append(ast.literal_eval(weight_ent.get()))
    get_num_of_items()
    get_max_weight()
    get_profit()
    print(num_of_items, max_weight)
    weight_ent.delete(0, tk.END)
    if count - 1 == num_of_items:
        running_solutions()
    var.set("Enter weight for item number: %s" % count)



print(count)
weight_ent = tk.Entry(window, width=40)
weight_ent.pack(padx=20, pady=10)

# Label for weight entries
var_two = StringVar()
label = Label(window, textvariable=var_two)
var_two.set("Enter profit for item number: %s" % count)
label.pack(pady=10)

profits = []


def get_profit():
    clicked()
    profits.append(ast.literal_eval(profits_ent.get()))
    profits_ent.delete(0, tk.END)
    var_two.set("Enter profit for item number: %s" % count)


profits_ent = tk.Entry(window, width=40)
profits_ent.pack(padx=20, pady=10)

btn = tk.Button(window, height=1, width=10, text="Read", command=get_weight)
btn.pack(pady=20)


def running_solutions():
    result_dp = DynamicProgramming(num_of_items, max_weight, weights, profits).solution()
    var_result_dp.set("The solution for dp is: %s"%result_dp)
    result_br = BruteForce(num_of_items, max_weight, weights, profits).solution()
    var_result_br.set("The solution for brute force is: %s"%result_br)
    result_gr = GreedySolution(num_of_items, max_weight, weights, profits).solution()
    var_result_gr.set("The solution for greedy is: %s"%result_gr)

var_result_dp = StringVar()
label = Label(window, textvariable=var_result_dp)
var_result_dp.set("The solution for dp is: ????")
label.pack(padx=20, pady=10)

var_result_br = StringVar()
label = Label(window, textvariable=var_result_br)
var_result_br.set("The solution for brute force is: ????")
label.pack(padx=20, pady=10)

var_result_gr = StringVar()
label = Label(window, textvariable=var_result_gr)
var_result_gr.set("The solution for greedy force is: ????")
label.pack(padx=20, pady=10)

window.title('Knapsack')
window.geometry("350x500+10+10")
window.mainloop()
