import matplotlib.pyplot as plt
import seaborn as sns

flights = sns.load_dataset('flights')
# pivot table
pivot_flights = flights.pivot_table(index='month',columns='year',values='passengers')

sns.heatmap(pivot_flights,cmap='Blues',linecolor='white',linewidth = 1)
plt.show()