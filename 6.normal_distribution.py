#case-1
from numpy import random
x=random.normal(size=(2,3))
print(x)

#case-2 
# random.normal has 3 parameters.

from numpy import random
x=random.normal(loc=1,scale=2,size=(2,3))
print(x)


# loc - (Mean) where the peak of the bell exists.

# scale - (Standard Deviation) how flat the graph distribution should be.

# size - The shape of the returned array.

