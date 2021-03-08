import pandas as pd

eCom_data_frame = pd.read_csv('pandas/assets/Ecommerce Purchases.csv')
print(eCom_data_frame.head())

print("Columns".center(50, '-'))
print(len(eCom_data_frame.columns))

print("Rows".center(50, '-'))
print(len(eCom_data_frame.index))

print("Average purchase price".center(50, '-'))
print(eCom_data_frame['Purchase Price'].mean())

print("Highest purchase price".center(50, '-'))
print(eCom_data_frame['Purchase Price'].max())

print("Lowest purchase price".center(50, '-'))
print(eCom_data_frame['Purchase Price'].min())

print("English Language people".center(50, '-'))
print(sum(eCom_data_frame['Language'] == 'en'))
# print(eCom_data_frame[eCom_data_frame['Language'] == 'en']['Language'].count())

print("Lawyer people".center(50, '-'))
print(sum(eCom_data_frame['Job'] == 'Lawyer'))

print("Am and PM people".center(50, '-'))
print(eCom_data_frame['AM or PM'].value_counts())
# print(eCom_data_frame.groupby('AM or PM')['AM or PM'].count())

print("Top 5 common job title".center(50, '-'))
print(eCom_data_frame['Job'].value_counts().head(5))

print("90 WT purchase price".center(50, '-'))
print(eCom_data_frame[eCom_data_frame['Lot'] == '90 WT']['Purchase Price'])

print("American express and 95 above".center(50, '-'))
print(len(eCom_data_frame[(eCom_data_frame['CC Provider'] == 'American Express') &
                          (eCom_data_frame['Purchase Price'] > 95)]))


print("Expire in 2025".center(50, '-'))


def exp_date(date):
    _, year = date.split('/')
    if year == "25":
        return True
    return False


print(sum(eCom_data_frame['CC Exp Date'].apply(lambda x: exp_date(x))))
# print(sum(eCom_data_frame['CC Exp Date'].apply(lambda x: x[3:]=='25')))


print("Top 5 Email Provider".center(50, '-'))
print(eCom_data_frame['Email'].apply(
    lambda email: email.split('@')[1]).value_counts().head(5))
