import pandas as pd
from sqlalchemy import create_engine

data_frame = pd.read_csv('pandas/assets/example.csv')

print("Reading CSV file".center(50, '-'))
print(data_frame)

# Starting an engine
sql_engine = create_engine('sqlite:///:memory:')
data_frame.to_sql('pandas_table', sql_engine)

sql_data_frame = pd.read_sql('pandas_table', con=sql_engine)
print("Reading from sql engine".center(50, '-'))
print(sql_data_frame)
