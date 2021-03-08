import pandas as pd

salary_data_frame = pd.read_csv('pandas/assets/Salaries.csv')

print("Salary data frame".center(50, '-'))
print(salary_data_frame.head())

print("Salary data frame info".center(50, '-'))
print(salary_data_frame.info())

print("Average BasePay".center(50, '-'))
print(salary_data_frame['BasePay'].mean())

print("Highest amount of OvertimePay".center(50, '-'))
print(salary_data_frame['OvertimePay'].max())

print("Job title of JOSEPH DRISCOLL".center(50, '-'))
print(salary_data_frame
      [salary_data_frame['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle'])

print("including benefits of JOSEPH DRISCOLL".center(50, '-'))
print(salary_data_frame
      [salary_data_frame['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits'])

print("Highest paid employee with benefits".center(50, '-'))
print(salary_data_frame
      [salary_data_frame['TotalPayBenefits'] == salary_data_frame['TotalPayBenefits'].max()]['EmployeeName'])

# print(salary_data_frame.loc[salary_data_frame['TotalPayBenefits'].idxmax()])

print("Lowest paid employee with benefits".center(50, '-'))
print(salary_data_frame
      [salary_data_frame['TotalPayBenefits'] == salary_data_frame['TotalPayBenefits'].min()]['EmployeeName'])

print("Average Salary of per year".center(50, '-'))
groupBy_salaryData = salary_data_frame.groupby('Year')
print(groupBy_salaryData.mean()['BasePay'])

print("Total Unique job title".center(50, '-'))
print(salary_data_frame['JobTitle'].nunique())

print("Top 5 common jobs".center(50, '-'))
print(salary_data_frame['JobTitle'].value_counts().head())

print("Job titles represented by one in 2013".center(50, '-'))
print(sum(salary_data_frame[salary_data_frame['Year']
                            == 2013]['JobTitle'].value_counts() == 1))

print("Job titles with word Chief".center(50, '-'))


def check_chief(title):
    if 'chief' in title.lower().split():
        return True
    return False


print(sum(salary_data_frame['JobTitle'].apply(
    lambda x: check_chief(x))))
