# Logistic Distribution is used to describe growth.

# Used extensively in machine learning in logistic regression, neural networks etc.

# It has three parameters:

# loc - mean, where the peak is. Default 0.

# scale - standard deviation, the flatness of distribution. Default 1.

# size - The shape of the returned array.

#Case-1-Printing an array

from tokenize import PlainToken
from numpy import random
x=random.logistic(loc=2,scale=3,size=(2,3))
print(x)

#Case-2 - plotting logistic function

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.logistic(loc=1,scale=2,size=(2,3)),hist=False)
plt.show()