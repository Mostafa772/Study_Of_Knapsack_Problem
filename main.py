from abc import ABC, abstractmethod  
from itertools import chain, combinations
# Class Knapsack that will take as input first the capacity of the knapsack 
# then the number of the items K and finally the value of each item 

# a function to get all subsets of a set
def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


class Knapsack:

  def __init__(self, init_size, init_num_of_items):
    self.items = []
    self.size = init_size
    self.num = init_num_of_items
    
    for i in range(init_num_of_items):
      self.items.append(int(input()))


  def __str__(self):
    return f"The number of items we have is: {str(self.num)} and the size of the knapsack is: {str(self.size)} and the items have the values {self.items}" 
  
  @abstractmethod
  def solution(self):
    pass


class BruteForce(Knapsack):
  def solution(self):
    max_amount = 0 
    for choice in powerset(self.items):
       if len(choice) > self.size:
         continue
       elif sum(choice) > max_amount:
            max_amount = sum(choice)
       else :
         continue     

    return max_amount
      #  print(len(choice), choice) 


# first_test = Knapsack(1, 2)
# print(first_test)

example = BruteForce(1, 3)
print(str(example.solution()))
