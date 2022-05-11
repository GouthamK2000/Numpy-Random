from numpy import random

x=random.choice([4,5,6,3],p=[0.5,0.3,0.1,0.1],size=(4,5))
print(x)

#choice() method allows us to mention the probability. Outputs necessarily need not conatoin the values in that probability, but while choosing each value, output will be in that provbility.
# no. of element sinside the choice and that inside p should be equal.
#values inside p must be 0>=x<=1, usually we say in 0.x range. 
#sum of all values inside p must equal to 1.