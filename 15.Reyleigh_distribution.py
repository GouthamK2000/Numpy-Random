# Rayleigh distribution is used in signal processing.

# It has two parameters:

# scale - (standard deviation) decides how flat the distribution will be default 1.0).

# size - The shape of the returned array.

#Case-1 -Rayleigh distribution

from numpy import random

x=random.rayleigh(scale=2,size=(2,3))
from(x)


#Case-2 -Visualization of Rayleigh Distribution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.rayleigh(size=1000),hist=False)
plt.show()