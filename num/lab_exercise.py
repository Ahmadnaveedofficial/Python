import numpy as np

a = np.array([1, 2, 3, 4])
print(a)


# b = np.array([[1, 2],
#               [3, 4]])
# print(b)




print(a.shape)  # size
print(a.ndim)   # dimension
print(a.size)   # total elements


np.zeros((2,2))   # all 0
np.ones((3,3))    # all 1
np.eye(3)         # identity matrix