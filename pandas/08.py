import pandas as pd

left = pd.DataFrame({
    'KEY1': ['K0', 'K0', 'K1', 'K2'],
    'KEY2': ['K0', 'K1', 'K0', 'K1'],
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3']
})

right = pd.DataFrame({
    'KEY1': ['K0', 'K1', 'K1', 'K2'],
    'KEY2': ['K0', 'K0', 'K0', 'K0'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']
})

print("INNER JOIN".center(50, '-'))
print(pd.merge(left, right, on=['KEY1', 'KEY2']))

print("OUTER JOIN".center(50, '-'))
print(pd.merge(left, right, on=['KEY1', 'KEY2'], how='outer'))

print("RIGHT JOIN".center(50, '-'))
print(pd.merge(left, right, on=['KEY1', 'KEY2'], how='right'))

print("LEFT JOIN".center(50, '-'))
print(pd.merge(left, right, on=['KEY1', 'KEY2'], how='left'))
