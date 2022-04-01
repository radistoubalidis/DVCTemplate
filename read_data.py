import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import os

if os.path.isfile("data/tracks.csv"):
    tracks = pd.read_csv('data/tracks.csv')
    print("Tracks dataset preview")
    print(tracks.head())
years = np.asarray([int(y.split("-")[0]) for y in tracks['release_date']])
tracks['year'] = years

year_list = sorted(list(tracks['year'].unique()))
res = pd.cut(tracks['year'],10,labels=['1921-31','1931-41','1941-51','1951-61','1961-71','1971-81','1981-91','1991-01','2001-11','2011-2020'])
tracks['decade'] = res



dec_dist = dict(tracks['decade'].value_counts())

if os.path.isfile('plots/decade_dist.png'):
    dd = plt.figure()
    plt.bar(x=list(dec_dist.keys()),height=list(dec_dist.values()))
    plt.title("Decade Distribution")
    plt.savefig("plots/decade_dist.png")


tempos = (tracks['tempo'])
tempos = pd.cut(tempos,8,labels=['0-50','51-75','76-100','101-125','126-150','151-175','176-200','201-250'])

tempo_dist = dict(tempos.value_counts())

if os.path.isfile('plots/tempo_dist.png'):
    plt.clf()
    td = plt.figure()
    plt.bar(x=list(tempo_dist.keys()),height=list(tempo_dist.values()))
    plt.title("Tempo Distribution in bpm")
    plt.savefig('./plots/tempo_dist.png')
