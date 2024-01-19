import matplotlib.pyplot as plt
import seaborn as sns

tips_df = sns.load_dataset('tips')

#  creates subplots based on 'time' and 'smoker' without using hue
# tips_fg = sns.FacetGrid(tips_df,col='time',row='smoker')
# tips_fg.map(plt.hist, 'total_bill',bins=8)
# tips_fg.map(plt.scatter, 'total_bill','tip')


# creates subplots based on 'time', incorporates hue with 'smoker' for color differentiation, and specifies specific height and aspect ratio.
tips_fg = sns.FacetGrid(tips_df,col='time',hue='smoker',height=4,aspect=1.3,col_order=['Dinner','Lunch'],palette='Set1')
tips_fg.map(plt.scatter, 'total_bill','tip',edgecolor='w')


plt.show()