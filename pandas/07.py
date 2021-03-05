import numpy as np
import pandas as pd

data = {
    'Company': ['GGL', 'GGL', 'AMZ', 'AMZ', 'FCB', 'FCB'],
    'Person': ['Akshit', 'Viral', 'Suru', 'Rajan', 'Tushar', 'Ashwini'],
    'Sales': [200, 120, 340, 124, 243, 350]
}

data_frame = pd.DataFrame(data)
print("Dictionary to Data frame".center(50, '-'))
print(data_frame)

# Creating group by object and then perform aggregrate func
group_by_company = data_frame.groupby('Company')

print("Sum of sales by company".center(50, '-'))
print(group_by_company.sum())

print("Max of sales of company".center(50, '-'))
print(group_by_company.sum().max())

print("Sales of Amazon".center(50, '-'))
print(group_by_company.sum().loc['AMZ'])

print("All information about company".center(50, '-'))
print(group_by_company.describe())
