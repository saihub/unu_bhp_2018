import pandas as pd
import matplotlib.pylab as plt
from datetime import datetime
import numpy as np
pd.set_option('display.max_columns', 51)
font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 32}
plt.rc('font', **font)

def normalize_for_plot(v):
    v_mean=np.mean(v)
    v = v - v_mean
    v_min, v_max = min(v), max(v)
    v = v / max([abs(v_min), abs(v_max)])
    return v
def plot_features(df, start_time, end_time, features, normalized=True):
    '''
    plot the feautres for EDA in different time range
    Feature is suggested to normalize for feature comparison
    '''
    plt.figure(figsize = (15,8))
    time_range = (df["Time"] < end_time)&(df["Time"] > start_time)
    x = df.loc[time_range,["Time"]].values
    for feature in features:
        y = df.loc[time_range, [feature]].values
        if normalized:
            y = normalize_for_plot(y)
        plt.plot(x, y, label = feature)
    plt.legend(features)
    plt.show()