import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

crash_df = sns.load_dataset('car_crashes')

sns.displot(crash_df['not_distracted'],kde=False)
plt.show()