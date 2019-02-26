# generate models for names
# get input as name and activty
# open csv file correspodingly "__name__activity.csv"
# trim the first and last 10 data entries
# create min, max heap based on attention, pop out 20 entries use mean squared error for plane based on x,att,med
# save min_att,max_att,activity to model csv

import numpy as np
import pandas as pd
from pathlib import Path
from keras.layers import Dense
from keras.models import Sequential
name = 'Kabi'
activity = 'rest'
# fix random seed for reproducibility
np.random.seed(7)

# load dataset without header
dataset = np.loadtxt("./records/test_data.csv", delimiter=",")
# with header
# dataset = pd.read_csv('./records/test_data.csv', sep=',', header=None)
# maxdataset = max heap 20 iterations
# mindataset = min heap 20 iterations

# darr = sorted(dataset, key=lambda dataset: dataset[8])
darr = dataset[np.lexsort(([1, -1]*dataset[:, [2]]).T)]


def fun(X, Y):
    model = Sequential()
    model.add(Dense(10, input_dim=8, activation='relu'))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')
    model.summary()
    # Compile model
    model.compile(loss='binary_crossentropy',
                  optimizer='adam', metrics=['mae', 'acc'])

    # Fit the model
    model.fit(X, Y, epochs=150, batch_size=10)

    # evaluate the model
    scores = model.evaluate(X, Y)
    print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

    print("predicting ...")
    # calculate predictions
    predictions = model.predict(X)
    # round predictions
    rounded = [x[0] for x in predictions]
    print(rounded)
    return rounded


# split into input (X) and output (Y) variables
# calculating min attention range
X = darr[1:60, 0:8]
Y = darr[1:60, 8]
max_range = fun(X, Y)
# print(Y)
# create model

# calculating max attention range

X = darr[-60:-10, 0:8]
Y = darr[-60:-10, 8]
min_range = fun(X, Y)

print(min_range, max_range)
# save file as model_name.csv with 3 poperties : min,max,att
header = np.array([["min_attention", "max_attention", "activity"]])
header = np.append(header, [[min_range, max_range, activity]], axis=0)
p = Path('./records/model_'+name+'_'+activity+'.csv')
print('Saving data...')
with p.open('ab') as f:
    np.savetxt(f, header, delimiter=",", fmt='%.3f')
    print('Saved')
