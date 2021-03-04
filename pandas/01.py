import numpy as np
import pandas as pd

labels = ['a', 'b', 'c']
numbers = [10, 20, 30]
arr = np.array(numbers)
dic = {'a': 10, 'b': 20, 'c': 30}

print(type(labels), type(numbers), type(arr), type(dic))

# panda01 = pd.Series(data=numbers)
panda01 = pd.Series(numbers)
print(panda01)

# panda02 = pd.Series(data=numbers, index=labels)
panda02 = pd.Series(numbers, labels)
print(panda02)

panda03 = pd.Series(arr)
print(panda03)

# Make automatic from dic to index and data
panda04 = pd.Series(dic)
print(panda04)

# you can store build-in fuction also
panda05 = pd.Series([sum, print, len])
print(panda05)
