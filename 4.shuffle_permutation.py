#case-1 - shuffle()

from numpy import random
import numpy as np

arr=np.array([7,5,6,3,5])
random.shuffle(arr)                           #random.shuffle('arrayname'), shuffles/changes the original array.
print(arr)                    


#case-2 -permutation()
 from numpy import random
 import numpy as np

 arr=np.array([5,3,6,2,5,2])
 print(random.permutation(arr))              #randm.permutation('arrayname'), does not change the original array.
 