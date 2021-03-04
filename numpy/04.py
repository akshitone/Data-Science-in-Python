import numpy as np

arr_2d = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
print("2d array:", arr_2d)

print("1st column:", arr_2d[0])
print("2nd row:", arr_2d[:, 1])

# print first 2 column and last 2 row
print("Custom row and column", arr_2d[:2, 1:])

arr = np.arange(1, 11)
bool_arr = arr > 5
print("Main array:", arr)
print("Boolean array:", bool_arr)
print("Array of boolean:", arr[bool_arr])

print("Shortcut boolean array:", arr[arr > 5])

# List comprehension
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst = [i for i in lst if i > 5]
print("List:", lst)

my_2d = np.arange(50).reshape(5, 10)
print("5 X 10 array:", my_2d)

print("Custom array:", my_2d[1:3, 3:5])
