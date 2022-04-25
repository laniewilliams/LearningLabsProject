from django.urls import path

from . import views


app_name = 'MainApp'

urlpatterns = [
    path('',views.index, name='index'), #define what view is on the hompage and named the view
    path('topics',views.topics, name='topics'),
]