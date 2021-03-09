import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')

print("Build-in data from seaborn".center(50, '-'))
print(tips.head(10))

sns.boxplot(x='day', y='total_bill', data=tips,
            hue='smoker', palette='coolwarm')

plt.tight_layout()
plt.show()
