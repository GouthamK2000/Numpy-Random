# Binomial Distribution
# Binomial Distribution is a Discrete Distribution.

# It describes the outcome of binary scenarios, e.g. toss of a coin, it will either be head or tails.

# It has three parameters:

# n - number of trials.

# p - probability of occurence of each trial (e.g. for toss of a coin 0.5 each).

# size - The shape of the returned array.



#Case-1- prints an array of specified size, within

from numpy import random
x=random.binomial(n=200,p=0.5,size=5)
print(x)

#Case-2 - prints a histogram

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)

plt.show()


#Case-3 - Differnece between binomial and normal distriibution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')

plt.show()