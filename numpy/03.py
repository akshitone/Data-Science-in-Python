import numpy as np

arr = np.arange(0, 11)
print("Array:", arr)

# Array index
print("Array from 1 to 4:", arr[1:5])
print("Array in decending order with even numbers:", arr[::-2])


# Slice of array
arr_that_slice = np.arange(0, 11)
slice_of_arr = arr_that_slice[0:5]

print("Array:", arr_that_slice)
print("Slice of array:", slice_of_arr)

# Slice of array is also affect the main array
# Slicing the array is not copied the array, it's just view the array
slice_of_arr[:] = 20
print("Main array:", arr_that_slice)
print("Slice array:", slice_of_arr)

# Copy array
copy_arr = arr.copy()
print("Main array:", arr)
print("Copied array:", copy_arr)

copy_arr[:] = 10
print("Main array:", arr)
print("Copied array:", copy_arr)
