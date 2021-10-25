import numpy as np
from numpy.core.defchararray import array 

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

#Menambahkan elemen ke array dengan np.append()
print(np.append(arr,[1,2]))

#Menghapus Elemen dengan np.delete()
print(np.delete(arr, 1)) #menghapus di posisi satu

#Mengurutkan Elemen dengan np.sort() dapat menentukan axis(dimensi), jensi dan urutan
arrr = np.array([2,1,5,3,7,4,6,8])
print(np.sort(arrr))