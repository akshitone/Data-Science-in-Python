import pandas as pd

data_frame = pd.read_csv('pandas/example.csv')

print("Reading CSV file".center(50, '-'))
print(data_frame)

data_frame.to_excel('pandas/output.xlsx',
                    sheet_name='csv_to_excel', index=None)

print("Creating and Reading excel file".center(50, '-'))
print(pd.read_excel('pandas/output.xlsx'))
