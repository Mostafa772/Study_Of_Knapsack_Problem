from abc import ABC, abstractmethod  
from itertools import chain, combinations

# Class Knapsack will take as input first the capacity of the knapsack 
# then the number of the items K and finally the value of each item 

# a function to get all subsets of a set
def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

class Knapsack:

  def __init__(self, init_max_items, init_max_weight):
    self.items_prophet = []
    self.items_weight = []
    self.max_weight = init_max_weight
    self.max_items = init_max_items
    
    print("please enter the weight for each of the " + str(self.max_items) + "th item")
    for i in range(self.max_items):
      self.items_weight.append(int(input()))

    print("please enter the prophet for each of the " + str(self.max_items) + "th item")
    for i in range(self.max_items):
      self.items_prophet.append(int(input()))

  def __str__(self):
    return f"""The number of items we have is: {str(self.max_items)} and the max_weight of the knapsack is: {str(self.max_weight)} 
and the items have the weigths of {self.items_weight} and prophet of {self.items_prophet}"""  
  
  @abstractmethod
  def solution(self):
    pass


class BruteForce(Knapsack):

  def solution(self):
    max_amount = 0

    for p, w in zip(powerset(self.items_prophet), powerset(self.items_weight)):
      #print(p, " || ",w)
      if sum(w) > self.max_weight or len(w) > self.max_items:
        continue
      elif sum(p) > max_amount:
        max_amount = sum(p)

    return max_amount
      #  print(len(choice), choice) 


# first_test = Knapsack(1, 2)
# print(first_test)

class DynamicProgramming(Knapsack):
  def solution(self):
    
    table = [[0 for x in range(self.max_weight + 1)] for y in range(self.max_items + 1)]
    # print(table)
    i = 0
    while i < self.max_items + 1:
      j = 0
      while j < self.max_weight + 1:
        if i == 0 or j == 0:
          table[i][j] = 0
        elif self.items_weight[i - 1] <= j:
          table[i][j] = max(table[i - 1][j], table[i - 1][j - self.items_weight[i - 1]] + self.items_prophet[i - 1]) 
        else:
          table[i][j] = table[i - 1][j]
        
        j += 1
      i += 1
    # print(table)
    return(table[self.max_items][self.max_weight])



# example = BruteForce(4, 8)
example_two = DynamicProgramming(4, 8)
print("we are here: " + str(example_two.solution())) 
#print("we are here: " + str(example.solution())) 
print(example_two)
