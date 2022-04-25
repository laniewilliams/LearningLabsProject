from django.shortcuts import render

from .models import Topic
# Create your views here.

def index(request): #name of the view is index bc in urls.py we said views.index
    return render(request, 'MainApp/index.html') #rendering a page on your browser using index.html as a template

def topics(request):
    topics = Topic.objects.all() #can't use objects.all if we want to do order by. this will do it in ascending order (this might not be true)

    #we need to move the data to our page by using a dictionary --> referred to as context

    context = {'topics':topics} #the key 'topics' is what you have to refer to in the html. the value is whatever you call it in the view

    return render(request, 'MainApp/topics.html', context) #this gets us info from the DB and rendering the page
