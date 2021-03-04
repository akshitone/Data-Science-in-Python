import numpy as np

que01 = np.zeros(10)
print("array of 10 zeros:", que01)

que02 = np.ones(10)
print("array of 10 ones:", que02)

que03 = np.ones(10)*5
print("array of 10 fives:", que03)

que04 = np.arange(10, 51)
print("integer from 10 to 50:", que04)

que04 = np.arange(10, 51, 2)
print("even integer from 10 to 50:", que04)

que05 = np.arange(9).reshape(3, 3)
print("3 X 3 matrix:", que05)

que06 = np.eye(3)
print("3 X 3 matrix:", que06)

que07 = np.random.rand(1)
print("random number:", que07)

que08 = np.random.randn(25).reshape(5, 5)
print("5 X 5 random number:", que08)

# que09 = np.arange(0.01, 1.01, 0.01).reshape(10, 10)
que09 = np.arange(1, 101).reshape(10, 10)/100
print("0.01 to 1.:", que09)

que10 = np.linspace(0, 1, 20).reshape(4, 5)
print("20 linearly spaced between 0 and 1:", que10)
