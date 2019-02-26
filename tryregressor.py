from sklearn import datasets, linear_model
from sklearn.model_selection import cross_val_score, KFold
from keras.models import Sequential
from sklearn.metrics import accuracy_score
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
import numpy
seed = 1

dataset = numpy.loadtxt("./records/test_data.csv", delimiter=",")

# split into input (X) and output (Y) variables
X = dataset[:, 0:8]
Y = dataset[:, 8]


def baseline_model():
    model = Sequential()
    model.add(Dense(8, input_dim=8, activation='linear'))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model


estimator = KerasRegressor(build_fn=baseline_model,
                           nb_epoch=10, batch_size=20, verbose=False)
kfold = KFold(n_splits=10, random_state=seed)
results = cross_val_score(estimator, X, Y, cv=kfold)
print("Results: %.2f (%.2f) MSE" % (results.mean(), results.std()))

X_test = dataset[50, 0:8]
Y_test = dataset[50, 8]

estimator.fit(X, Y)
prediction = estimator.predict(X_test)
# accuracy_score(Y, prediction)
