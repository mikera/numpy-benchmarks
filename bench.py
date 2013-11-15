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
	a = np.zeros([n,n])
	for i in range(n):
		for j in range(n):
			a[i,j] = i*j
	a = np.sum(a)
	return a

print ("Timing buildsum")
print(bench("buildsum", "10"))


# Multiplication (inner product) of two 100x100 matrices
# => about 0.86 ms

def multiply(n): 
	a = np.ones([n,n])
	a.fill (0.5)
	b = np.ones([n,n])
	b.fill (0.5)
	a = np.dot (a,b)
	return a
	
for x in [2,3,4,5,6,7,8,10,13,16,20,25,32,40,50,64,80,101,128,161,203,256,322,406,512,645,812,1024]:
	# print ("Timing multiply 100x100")
	print(str(x) + "\t"+ str(bench("multiply", str(x))))


# Multiplication (inner product) of two 10x10 matrices
# => about 6,400 ns

print ("Timing multiply 10x10")
print (bench("multiply", "10"))