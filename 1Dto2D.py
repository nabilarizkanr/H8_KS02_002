import numpy as np
#Meningkatkan Dimesi Array Menggunakan :
#np.newaxis 
#Meningkatkan dimensi array sebesar satu dimensi bila digunakan sekali
a = np.array([1, 2, 3, 4, 5, 6])
a.shape
a2 = a[np.newaxis]
print(a2.shape)
print(a2)

row_vector = a[np.newaxis, :]
print(row_vector.shape)
print(row_vector)

col_vector = a[:, np.newaxis]
print(col_vector.shape)
print(col_vector)

#np.expand_dims
#Memperluas array dengan memasukkan axis baru pada posisi yang ditentukan
b = np.expand_dims(a, axis=1)
print(b.shape)

c = np.expand_dims(a, axis = 0)
print(c.shape)