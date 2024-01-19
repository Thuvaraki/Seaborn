import matplotlib.pyplot as plt
import seaborn as sns

tips_df = sns.load_dataset('tips')

sns.lmplot(
    x='total_bill',
    y='tip',
    hue='sex',
    data=tips_df,
    markers=['o', '^'],
    scatter_kws={'s': 100, 'edgecolor': 'w'}
)
# markers=['o', '^']: Use('o') for one gender and ('^') for the other.
# scatter_kws={'s': 100, 'edgecolor': 'w'}: Set the marker size ('s') to 100, and give the markers a white edgecolor.

plt.show()
