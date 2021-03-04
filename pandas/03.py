import numpy as np
import pandas as pd
from numpy.random import randint, randn


numbers_2D = randn(5, 4)
# numbers_2D = randint(1, 100, 20).reshape(5, 4)
X_labels = ['A', 'B', 'C', 'D', 'E']
Y_labels = ['W', 'X', 'Y', 'Z']
data_frame = pd.DataFrame(numbers_2D, X_labels, Y_labels)

print(data_frame)

# Display column data --> looking like Series
# print(data_frame.W)
print(data_frame['W'])

# Display types
print(type(data_frame), type(data_frame['W']))


print(data_frame[['W', 'Z']])

# Creating new column in data frame
data_frame['NEW'] = data_frame['W'] + data_frame['Z']
print(data_frame)

# Deleting column
print("Drop Y coloumn".center(50, '-'))
print(data_frame.drop('Y', axis=1))
print("Does not affect main dataframe".center(50, '-'))
print(data_frame)

# Deleting permenently use inplace=True
data_frame.drop('NEW', axis=1, inplace=True)
print("Deleting Y column permanently using inplace".center(50, '-'))
print(data_frame)

# Deleting row
print("Drop E row".center(50, '-'))
print(data_frame.drop('E'))


# Display row data --> looking like Series
print("Display row A from data frame".center(50, '-'))
print(data_frame.loc['A'])

print("Display row C using index from data frame".center(50, '-'))
print(data_frame.iloc[2])

# subset of data frames
print("Display A and C row and W and X column".center(50, '-'))
print(data_frame.loc[['A', 'C'], ['W', 'X']])
