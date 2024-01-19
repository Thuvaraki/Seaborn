import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

tips_df = sns.load_dataset('tips')
# bar plot
# sns.barplot(x='sex',y='total_bill',data=tips_df,estimator=np.median)

# count plot
# sns.countplot(x='sex',data=tips_df)

# box plot
# sns.boxplot(data=tips_df,x='day',y='total_bill',hue='sex')

# violin plot
# sns.violinplot(data=tips_df,x='day',y='total_bill',hue='sex',split=True)

# strip plot
# sns.stripplot(data=tips_df,x='day',y='total_bill',hue='sex')
# Jitter is applied to prevent overlapping points.
# dodge=True: separates the points for each level of the 'hue' variable.
# It means that points for different 'sex' categories will be displayed separately rather than overlapping.
# sns.stripplot(data=tips_df,x='day',y='total_bill',hue='sex',jitter=True,dodge=True)

# swarm plot
# sns.swarmplot(data=tips_df,x='day',y='total_bill',hue='sex')

plt.show()