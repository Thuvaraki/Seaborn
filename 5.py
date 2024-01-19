import matplotlib.pyplot as plt
import seaborn as sns

crash_df = sns.load_dataset('car_crashes')

# styling
# sns.set_style('white')
# sns.set_style('whitegrid')
# sns.set_style('darkgrid')
# sns.set_style('dark')
sns.set_style('ticks')

plt.figure(figsize=(8,4))

# adjust the overall appearance of plot
# sns.set_context('poster',font_scale=1.5)
sns.set_context('paper',font_scale=1.5)

sns.jointplot(x='speeding',y='alcohol',data=crash_df,kind='reg')

# sns.despine() function in Seaborn is used to remove or modify the spines of a plot
# left=True: This specifies that the left spine of the plot should be removed.
# bottom=True: This specifies that the bottom spine of the plot should be removed.
sns.despine(left=True, bottom=True)

plt.show()

