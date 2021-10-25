import numpy as np
ex = np.array([1,2,3,4,5,6,7,8,9,10])

ex2 = np.expand_dims(ex, axis=1)
print(ex2.shape)

ex3 = np.expand_dims(ex, axis=0)
print(ex3.shape)

ex4 = ex[np.newaxis]
print(ex4.shape)

ex5 = ex[:, np.newaxis]
print(ex5.shape)

