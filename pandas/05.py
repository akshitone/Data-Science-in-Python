import numpy as np
from numpy.random import randn
import pandas as pd
import os

os.system("clear")

outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]

hier_index = list(zip(outside, inside))
print("Zip index:", hier_index)

hier_index = pd.MultiIndex.from_tuples(hier_index)
print(hier_index)

print("Data frame".center(50, '-'))
data_frame = pd.DataFrame(randn(6, 2), hier_index, ['A', 'B'])
print(data_frame)

print("Naming of indecies".center(50, '-'))
data_frame.index.names = ['Group', 'Member']
print(data_frame)

print("Particular value".center(50, '-'))
print(data_frame.loc['G2'].loc[2]['B'])

print("Particular value".center(50, '-'))
print(data_frame.loc[['G1', 'G2']].iloc[[1, 4]])

print("Using cross section".center(50, '-'))
print(data_frame.xs(2, level='Member'))
