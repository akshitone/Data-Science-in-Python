import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

tips = sns.load_dataset('tips')

print("Build-in data from seaborn".center(50, '-'))
print(tips.head(10))

sns.barplot(x='sex', y='total_bill', data=tips)

plt.tight_layout()
plt.show()
