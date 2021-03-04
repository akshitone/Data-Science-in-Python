import pandas as pd
import numpy as np
from numpy.random import randn

numbers_2D = randn(5, 4)
X_labels = ['A', 'B', 'C', 'D', 'E']
Y_labels = ['W', 'X', 'Y', 'Z']
data_frame = pd.DataFrame(numbers_2D, X_labels, Y_labels)

print("Data frame".center(50, '-'))
print(data_frame)

print("Boolean data frame".center(50, '-'))
boolean_data_frame = data_frame > 0
print(boolean_data_frame)

print("Data frame with positive values".center(50, '-'))
print(data_frame[boolean_data_frame])

print("W column boolean values".center(50, '-'))
print(data_frame['W'] > 0)

print("W column with positive values".center(50, '-'))
print(data_frame['W'][data_frame['W'] > 0])

# Creating subset of particular condition
print("Z column in W column with positive values".center(50, '-'))
# data_frame[data_frame['W'] > 0]['Z']
positive_data_frame_W = data_frame[data_frame['W'] > 0]
print(positive_data_frame_W['Z'])

# Multiple condition
print("W and Z column with positive values".center(50, '-'))
print(data_frame[(data_frame['W'] > 0) & (data_frame['Z'] > 0)][['W', 'Z']])

print("W and Z column with greater".center(50, '-'))
print(data_frame[data_frame['W'] > data_frame['Z']][['W', 'Z']])

country = ['USA', 'IND', 'AUS', 'ENG', 'CHN']
data_frame['COUNTRY'] = country

print("Updated Data Frame".center(50, '-'))
print(data_frame)

print("Build-in index".center(50, '-'))
print(data_frame.reset_index())

# if you want country as an index permanent use inplace=True
print("Set country as an index".center(50, '-'))
print(data_frame.set_index('COUNTRY'))
