import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_dataset('iris')
#  remove the 'species' column and store it in a separate variable (species).
#  We remove the 'species' column because we don't want to include it in the clustering
species = iris.pop('species')

sns.clustermap(iris)

plt.show()