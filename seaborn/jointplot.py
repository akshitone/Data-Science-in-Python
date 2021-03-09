import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')

print("Build-in data from seaborn".center(50, '-'))
print(tips.head(10))

# use kind to various designs in graph like reg, hex
sns.jointplot(x='total_bill', y='tip', data=tips)

plt.tight_layout()
plt.show()
