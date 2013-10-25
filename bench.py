from numpy import *
import timeit
import numpy as np

print ("Hello World with NumPy")

def bench(name, params):
	n = 10000
	r = timeit.timeit(name+"("+params+")", setup="from __main__ import "+name, number=n)
	return r * 1000000000.0 / n

# elementwise building of a 10x10 matrix, followed by computation of the sum
# => about 45,000 ns

def buildsum(n): 
	a = np.empty([n,n])
	for i in range(n):
		for j in range(n):
			a[i,j] = i*j
	a = np.sum(a)
	return a

print ("Timing buildsum")
print(bench("buildsum", "10"))


# Multiplication (inner product) of two 20x20 matrices
# => about 0.5 ms

def multiply(n): 
	a = np.empty([n,n])
	b = np.empty([n,n])
	a = np.dot (a,b)
	return a
	
print ("Timing multiply")
print(bench("multiply", "100"))