import matplotlib.pyplot as plt
import seaborn as sns

crash_df = sns.load_dataset('car_crashes')

# kde plot
# sns.kdeplot(crash_df['alcohol'])

# pair plot
sns.pairplot(crash_df)
plt.show()