import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')

print("Build-in data from seaborn".center(50, '-'))
print(tips.head(10))

sns.distplot(tips['total_bill'], bins=30)

plt.tight_layout()
plt.show()
