from django.urls import path 
from . import views

app_name = 'news'


urlpatterns = [
    path('',views.news, name = 'news'),
    path('news/', views.predict_chances, name='submit_prediction'),
]