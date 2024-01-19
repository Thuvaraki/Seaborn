import matplotlib.pyplot as plt
import seaborn as sns

crash_df = sns.load_dataset('car_crashes')

# scatter plot
# sns.jointplot(x='speeding',y='alcohol',data=crash_df,kind='reg')

# kde - kernal density estimation
# sns.jointplot(x='speeding',y='alcohol',data=crash_df,kind='kde')

# Hexagon distribution
sns.jointplot(x='speeding',y='alcohol',data=crash_df,kind='hex')

plt.show()