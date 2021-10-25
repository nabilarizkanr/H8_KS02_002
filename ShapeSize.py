import numpy as np 

array_ex = np.array([[[0,1,2,3],
                      [4,5,6,7]],
                      
                      [[0,1,2,3],
                       [4,5,6,7]],
                       
                       [[0,1,2,3],
                        [4,5,6,7]]])
print(array_ex)
# ndarray.ndim() --> jumlah axes 
print(array_ex.ndim)

# ndarray.size() --> jumlah total elemen array
print(array_ex.size)

# ndarray.shape() --> tuple int yang menunjukkan jumlah
#elemen yang disimpan di sepanjang setiap dimensi array.
#contoh : memiliki larik 2D, 2 baris dan 2 kolom maka bentuk larik (2,3)
print(array_ex.shape)