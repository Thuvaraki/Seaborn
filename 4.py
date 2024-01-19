import matplotlib.pyplot as plt
import seaborn as sns


tips_df = sns.load_dataset('tips')

# pair plot
sns.pairplot(tips_df,palette='Blues',hue='sex')

# rug plot
sns.rugplot(tips_df['tip'])

plt.show()