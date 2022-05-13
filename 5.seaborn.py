#case-1

import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot([0, 1, 2, 3, 4, 5])
plt.show()   # prints the normal graph, having barplot underneath the graphs



#seaborn uses matplotlib to visualise data from the underneath.
#case-2 - using hist=false
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot([0, 1, 2, 3, 4, 5],hist=False) #by using this, barplot is not present in the graph

plt.show() 


