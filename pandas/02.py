import pandas as pd

series01 = pd.Series([1, 2, 3, 4], ['USA', 'GER', 'IND', 'ENG'])
print(series01)

series02 = pd.Series([1, 2, 5, 4], ['USA', 'NZ', 'IND', 'WI'])
print(series02)
print("Value of USA in series 2:", series02['USA'])

print(series01+series02)
