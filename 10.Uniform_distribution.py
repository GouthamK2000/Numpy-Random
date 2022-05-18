# Uniform Distribution
# Used to describe probability where every event has equal chances of occuring.

# E.g. Generation of random numbers.

# It has three parameters:

# a - lower bound - default 0 .0.

# b - upper bound - default 1.0.

# size - The shape of the returned array.

#Case-1 ,random.uniform

from random import random
from tracemalloc import Snapshot
x=random.uniform(size=(8,7))
print(x)                                   #prints an array of size 8,7.

#NOTe- here a and b are default values.YOu must never specify them inside the unifrom function.


from random import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.uniform(size=4,2),hist=False)
plt.show()