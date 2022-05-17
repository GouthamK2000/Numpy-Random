# Poisson Distribution is a Discrete Distribution.

# It estimates how many times an event can happen in a specified time. e.g. If someone eats twice a day what is probability he will eat thrice?

# It has two parameters:

# lam - rate or known number of occurences e.g. 2 for above problem.

# size - The shape of the returned array.

#Case-1 -Basic example

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x=random.poisson(lam=3,size=5)
print(x)        #prints an array of size 5

#Case-2-Visualisation of Poisson's distribution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.poisson(lam=2,size=(3,4)),kde=False,title='vizualisation of Poissons distribution')
plt.show()

#kde=False, when hist=True is not mentioned. When kde=False, it indirectly means hist=True. kde need not be mentioned when hist=False is mentioned.