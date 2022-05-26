
#Case-1-Printing an array

from numpy import random
x=random.zipf(a=2,size=(4,3))
pritn(x)

#Zipf's Law: In a collection the nth common 
# term is 1/n times of the most common term. E.g. 5th common word in english has occurs nearly 1/5th times as of the most used word.


#Case-2-Histogram

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x=random.zipf(a=2,size=(3,2))
sns.distplot(x[x<10],kde=False)
plt.show()

# Sample 1000 points but plotting only ones with value < 10 for more meaningful chart.