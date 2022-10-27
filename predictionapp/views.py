from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import numpy as np
import warnings
from sklearn.model_selection import train_test_split
from sklearn.ensemble import  RandomForestRegressor

def home(request):
    return render(request, 'index.html')


def predictValue(age,bmi,childrens,sex,smoke,northwest,southeast,southwest):
    warnings.filterwarnings('ignore')

    # df= pd.read_excel('http://127.0.0.1:8000/media/ModelData.xlsx')
    df= pd.read_excel('https://nandu-insuranceprediction.herokuapp.com/media/ModelData.xlsx')

    X=df.drop('expenses',axis=1)
    y=df.expenses

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=12)

    model_rf= RandomForestRegressor(n_estimators=100)
    model_rf.fit(X_train, y_train)
    # pred_rf= model_rf.predict(X_test)

    pred_rf= model_rf.predict(np.array([age,bmi,childrens,sex,smoke,northwest,southeast,southwest]).reshape(1, -1))

    return pred_rf[0]

def predict(request):
    if request.method == "POST":
        age = int(request.POST['age'])
        bmi = float(request.POST['bmi'])
        childrens = int(request.POST['childrens'])
        sex = int(request.POST['sex'])
        smoke = int(request.POST['smoke'])
        region = int(request.POST['region'])
        northwest = 0 
        southeast = 0 
        southwest = 0
        if region == 1:
            northwest = 1
            southeast = 0
            southwest = 0
        elif region == 2:
            northwest = 0
            southeast = 1
            southwest = 0
        else:
            northwest = 0
            southeast = 0
            southwest = 1   
        print(age,bmi,childrens,sex,smoke,northwest,southeast,southwest)
        pre = predictValue(age,bmi,childrens,sex,smoke,northwest,southeast,southwest)
        return render(request, 'index.html',{'data':pre})
    return render(request, 'index.html')
