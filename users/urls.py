from django.urls import path, include




app_name = 'users'


urlpatterns = [
    path('',include('django.contrib.auth.urls')), #don't have to create a view because django has a default view. we do have to create a template

]