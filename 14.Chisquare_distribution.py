# Chi Square Distribution
# Chi Square distribution is used as a basis to verify the hypothesis.

# It has two parameters:

# df - (degree of freedom).

# size - The shape of the returned array.


#Case-1-chisquare basic

from numpy import random

x=random.chisquare(df=3,size=(4,3))
print(x)                                        #Prints random array


#Case-2 Plotting Chisquare for Visualisation

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.chisquare(df=5,size=(2,3)),hist=False)
plt.show()                                     #Prints graph.