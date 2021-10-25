import numpy as np 

a = np.arange(6) #mengakses sampe elemen 6 
print(a)

#np.reshape()
#memberikan bentuk baru tanpa mengubah datanya contoh a(1,6)
#akan diubah menjadi a(3,2)
b = a.reshape(3,2)
print(b)

c = a .reshape(6,1)
print(c)