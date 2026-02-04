import numpy as np

my_list = [1,2,3]
new_list = [1,3,5,7,9]

my_matrix = [[1,2,3],[4,5,6],[7,8,9]]



arr = np.array(my_list)
arr_2 = np.array(new_list)

arr_3 = np.array(my_matrix)

print(arr)
print(arr_2)
print(arr_3)

#zeros Built in method in NumPy

print(np.zeros((3,3)))

#arange 

print(np.arange(0,10))
