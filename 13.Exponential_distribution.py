# Exponential Distribution
# Exponential distribution is used for describing time till next event e.g. failure/success etc.

# It has two parameters:

# scale - inverse of rate ( see lam in poisson distribution ) defaults to 1.0.

# size - The shape of the returned array.

#Case-1-Basic exponential distribution

from numpy import random
x=random.exponential(scale=2,size=(4,5))
print(x)                             #Prints an array


#Case-2-Basic plot

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.exponential(scale=4,size=(4,5,5)),hist=False)
plt.show()                        # shows a plot, without histogram.