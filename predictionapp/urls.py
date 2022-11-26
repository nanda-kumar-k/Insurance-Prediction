from django.urls import path
from . import views

app_name = 'predictionapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('predict', views.predict, name='predict'),
    path('apipredict/<str:age>/<str:bmi>/<str:children>/<str:sex>/<str:smoke>/<str:region>', views.ApiPrediction, name='apipredict'),
]