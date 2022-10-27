import pandas as pd
import numpy as np
import warnings
from sklearn.model_selection import train_test_split
from sklearn.ensemble import  RandomForestRegressor


warnings.filterwarnings('ignore')

df= pd.read_excel('../DataPreproccesing/ModelData.xlsx')

X=df.drop('expenses',axis=1)
y=df.expenses

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=12)

model_rf= RandomForestRegressor(n_estimators=100)
model_rf.fit(X_train, y_train)
# pred_rf= model_rf.predict(X_test)

pred_rf= model_rf.predict(np.array([19,27.90,0,0,1,0,0,1]).reshape(1, -1))

print(pred_rf[0])