import numpy as np 
#Making a NumPy Array using np.array() function
a = np.array([1, 2, 3])
print(a)

#Creating an array filled with 0s :
arr = np.zeros(6)
print(arr)

#array filled with 1s :
first = np.ones(6)
print(first)

#Empty array --> function to initial contents is random depends on the state of the memory
empty = np.empty(6)
print(empty)

#Range of Elements
print(np.arange(4)) #akan mengakses sampai elemen 4
print(np.arange(0,10,2)) #start, stop, step
#dimulai dari elemen 0, stop di 10, kelang 2