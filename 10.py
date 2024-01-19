import matplotlib.pyplot as plt
import seaborn as sns

iris = sns.load_dataset('iris')
iris_g = sns.PairGrid(iris,hue='species')
iris_g.map(plt.scatter)

plt.show()