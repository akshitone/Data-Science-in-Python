import numpy as np

matrix01 = np.arange(1, 26).reshape(5, 5)

print("5 X 5 matrix:", matrix01)

print("Custom 3 X 4:", matrix01[2:, 1:])

print("Value:", matrix01[3, 4])

print("Custome 3 X 1:", matrix01[:3, 1:2])

print("Custome 1 X 5:", matrix01[-1:, :])

print("Custome 2 X 5:", matrix01[-2:, :])

print("Sum of matrix:", np.std(matrix01))

print("5 X 5 matrix:", matrix01)

print("Sum of matrix:", matrix01.sum(axis=0))
