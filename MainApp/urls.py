from django.urls import path

from . import views


app_name = 'MainApp'

urlpatterns = [
    path('',views.index, name='index'), #define what view is on the hompage and named the view
    path('topics/',views.topics, name='topics'),
    path('topics/<int:topic_id>/',views.topic, name='topic'), #tell it which topic to load by topic id
    path('new_topic',views.new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>/',views.new_entry, name='new_entry'),
]