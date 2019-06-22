#!/usr/bin/python3
import numpy as np

x=input("Enter the dimensions of array (for eg. 3x2 or 6x7): ")

#creating array with random integer values

a=np.random.randint(50,size=(int(x[0]),int(x[2])))

#here '50' the 1st arg. depicts the random valuse tht will be generated, will be less then 50

print(a)

b=np.random.rand(int(x[0]),int(x[2]))

#this will create an array of the given shape and populate it with random samples from a uniform distribution over [0, 1)

print(b)

#np.savetxt(x+"array",a,delimiter=',')

f=open(x+"array",'w+')
f.write(str(a))
f.write("\n\n")
f.write(str(b))
 
