import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

crash_df = sns.load_dataset('car_crashes')

# Exclude non-numeric columns from the correlation calculation
numeric_columns = crash_df.select_dtypes(include=[np.number])
crash_mx = numeric_columns.corr()

plt.figure(figsize=(8, 6))
sns.set_context('paper', font_scale=1.4)

# annot=True adds numerical annotations to each cell in the heatmap.
sns.heatmap(crash_mx,annot=True,cmap='Blues')
plt.show()

