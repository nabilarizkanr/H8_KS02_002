import numpy as np
a1 = np.array([[11,12,13,14], [15,16,17,18], [19,20,21,22], [23,24,25,26], [27,28,29,30]])

print(a1)
print(a1[a1>=13])
a2 = (a1>=10)
print(a1[a2])
print(a1[a1%2==1])
print(a1[a1%2==0])

a3 = np.array([1,2,3,4,5,6,7,8,9,10])
aa = a3[5:7]
print(aa)