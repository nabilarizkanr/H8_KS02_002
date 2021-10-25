import numpy as np
a1 = np.array([[1,1],[2,2]])
a2 = np.array([[3,3],[4,4]])
print(a1)
print(a2)

print(np.vstack((a1,a2)))
print(np.hstack((a1,a2)))

x1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24])
x2 = np.hsplit(x1,4)
x3 = x1.view()
x4 = x1.copy()
print(x1)
print(x2)
print(x3)
print(x4)