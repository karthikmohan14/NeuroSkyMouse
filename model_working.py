from sklearn import linear_model
import pandas as pd
import numpy as np
from pathlib import Path


def fun():
    df = pd.read_csv("./records/test_data.csv", header=0)
    model = linear_model.LinearRegression()
    # print(df[0:1])
    df = df.sort_values('attention')
    # print(df[-2:-3])
    model.fit(df[['delta', 'theta', 'lowAlpha', 'highAlpha', 'lowBeta',
                  'highBeta', 'lowGamma', 'midGamma']], df.attention)
    min = model.predict(
        [[216536, 317380, 95988, 80041, 90055, 19294, 12126, 4934]])
    max = model.predict(
        [[346062, 196531, 259415, 129600, 97253, 77846, 13958, 7854]])
    print(min, max)
    return min, max


min, max = fun()
# save file as model_name.csv with 3 poperties : min,max,att
header = np.array([["min_attention", "max_attention", "activity"]])
name = 'kabi'
activity = 'rest'
header = np.append(header, [[min, max, activity]], axis=0)
p = Path('./records/model_'+name+'_'+activity+'.csv')
print('Saving data...')
with p.open('ab') as f:
    np.savetxt(f, header, delimiter=",", fmt='%s')
    print('Saved')
