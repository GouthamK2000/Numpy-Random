#case-1-  random.randint(upper limit) -> gives us any number from 0 to upper limit

from numpy import random  #numpy allows us to have random module, to deal with random numbers
x=random.randint(100)  # upper limit from zero.
print(x)               #prints random numbers from 0 to 100


#case-2- random.rand -> gives us any float value from 0 to 1. NO need any arguments

from numpy import random
x=random.rand()
print(x)

#case-3-  gives us an array of the mentioned value size, if a parameter is passed inside random.rand function.

from numpy import random
x=random.rand(5)
print(x)
   
   #EX-2
   from numpy import random
   x=random.rand(5,3)   # forms a specific size. Either 1-D/2-D.
   print(x)


#case-4 -size(value) -> gives us the arrays of required size

from numpy import random
x=random.randint(5,size=(4,2))  # forms tha array of specific size from the upper mentioned.
print(x)


#conclusion : random.randint and random.rand arr 2 functions to print random integers/float. No parameter is needed in place of rand.
#Any parameter inside rand() function directly size is mentioned,but inside random.randint, apart from mentioning the upper value, size() parameter must be mentioned for a specific size.