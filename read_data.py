import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

tracks = pd.read_csv('data/tracks.csv')
years = np.asarray([int(y.split("-")[0]) for y in tracks['release_date']])
tracks['year'] = years

year_list = sorted(list(tracks['year'].unique()))
res = pd.cut(tracks['year'],10,labels=['1921-31','1931-41','1941-51','1951-61','1961-71','1971-81','1981-91','1991-01','2001-11','2011-2020'])
tracks['decade'] = res

count = dict(tracks['decade'].value_counts())
plt.bar(x=list(count.keys()),height=list(count.values()))
plt.savefig("./plots/decade_dist.png")