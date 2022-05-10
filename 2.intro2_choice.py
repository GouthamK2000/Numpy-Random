#case-1
from numpy import random
x=random.choice([4,5,6,2,3])  # choice method takes an array as a parameter
print(x)   # a random number from the mentioned array is printed

#case-2

from numpy import random

x=random.choice([5,4,6,3],size=(3,2))
print(x)  # array of the mentioned size is printed with the elements that are mentioned inside the array