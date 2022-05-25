
#Case-1 - Pareto distribution- prints arrays

from numpy import random
x=random.pareto(a=2,size=(2,3))
print(x)

#Case-2- Pareto distribution,  histrogram

from  numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.pareto(a=3,size=(5,2)),kde=False)
plt.show()