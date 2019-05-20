#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression



data = pd.read_csv('scripts/mtcars.csv')
#print(data.head(6))
x=data.drop(['model', 'vs', 'am', 'carb', 'mpg'], axis=1)
y=data.iloc[:,1]
model_mpg = LinearRegression().fit(x, y)
# print('Intercept: \n', model_mpg.intercept_)
# print('Coefficients: \n', model_mpg.coef_)

col_imp = ["cyl", "disp", "hp", "drat", "wt", "qsec", "gear"]



def predict(dict_values, col_imp=x.columns):
    x = np.array([float(dict_values[col]) for col in col_imp])
    x = x.reshape(1,-1)
    y_pred = float(model_mpg.predict(x)[0])
    return y_pred
