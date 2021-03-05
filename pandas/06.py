import numpy as np
import pandas as pd

dic = {'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]}

data_frame = pd.DataFrame(dic)
print("Dictionary to Data frame".center(50, '-'))
print(data_frame)

print("Omitted rows where data missing".center(50, '-'))
print(data_frame.dropna())

print("Omitted columns where data missing".center(50, '-'))
print(data_frame.dropna(axis=1))

print("atleast 2 columns are not null".center(50, '-'))
print(data_frame.dropna(thresh=2))

print("fill value where null".center(50, '-'))
print(data_frame.fillna(value='FILL'))

print("fill value in column".center(50, '-'))
print(data_frame['A'].fillna(value=data_frame['A'].mean()))
