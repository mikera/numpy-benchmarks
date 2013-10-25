from numpy import *
import timeit
import numpy as np

print ("Hello World with NumPy")

def buildsum(n): 
	a = np.arange(n*n)
	a = a.reshape([n,n])
	a = np.sinh(a)
	return a

print ("Timing buildsum")
print(timeit.timeit("buildsum(30)", setup="from __main__ import buildsum"))