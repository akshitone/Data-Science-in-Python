import numpy as np

# go 1st value to 2nd value with 3rd value of partition
print("Linspace array:", np.round(np.linspace(0, 5, 20), 2))

# array of random numbers
print("2D array of random numbers:", np.random.rand(3, 3))

# random number for particular range
randNumber = np.random.randint(1, 100, 10)
print("Array of random numbers:", randNumber)

print("Index and Maximum number in array:",
      randNumber.argmax(), randNumber.max())

print("Index and Minimum number in array:",
      randNumber.argmin(), randNumber.min())

# Reshape 1D array to length of particular dimention
zeroTo25 = np.arange(25)
reShape25 = zeroTo25.reshape(5, 5)
print("5D array:", reShape25)

print("Shape of array:", zeroTo25.shape)
print("Shape of array:", reShape25.shape)
