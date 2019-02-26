from sklearn import linear_model
import pandas as pd
df = pd.read_csv("./records/test_data.csv")
model = linear_model.LinearRegression()
model.fit(df[['delta', 'theta', 'lowAlpha', 'highAlpha', 'lowBeta',
              'highBeta', 'lowGamma', 'midGamma']], df.attention)
print(model.predict([[384978, 26436, 1301, 4682, 5116, 2787, 1523, 734]]))
print(model.predict([[121553, 37611, 7000, 7125, 11140, 5017, 1400, 685]]))
