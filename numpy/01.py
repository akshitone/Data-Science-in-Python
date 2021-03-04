import numpy as np

# 1D List
my_list = [1, 2, 3, 4, 5]
print("1D list:", my_list)

# 2D List
my_second_list = [[1, 2, 3], [4, 5, 6]]
print("2D list:", my_second_list)

# Converting list into 1D Array
numpy_arr = np.array(my_list)
print("1D array:", numpy_arr)

# Converting list into 2D Array
numpy_second_arr = np.array(my_second_list)
print("2D array:", numpy_second_arr)

# Arange array for particular values
print("1D array even values:", np.arange(0, 10, 2))

# Print zeros
print("1D array with zeors:", np.zeros(5))

# Print zeros
print("2D array with zeors:", np.zeros((3, 2)))

# Print ones
print("1D array with zeors:", np.ones(5))

# Print ones
print("2D array with zeors:", np.ones((3, 2)))
