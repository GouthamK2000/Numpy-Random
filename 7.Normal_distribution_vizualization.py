from tracemalloc import Snapshot
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


sns.distplot(random.normal(size=1000),hist=False)   #draws a bell curve.

plt.show()