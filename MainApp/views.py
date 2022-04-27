from django.shortcuts import render, redirect
from .forms import TopicForm

from .models import Topic
# Create your views here.

def index(request): #name of the view is index bc in urls.py we said views.index
    return render(request, 'MainApp/index.html') #rendering a page on your browser using index.html as a template

def topics(request):
    topics = Topic.objects.all() #can't use objects.all if we want to do order by. this will do it in ascending order (this might not be true)

    #we need to move the data to our page by using a dictionary --> referred to as context

    context = {'topics':topics} #the key 'topics' is what you have to refer to in the html. the value is whatever you call it in the view

    return render(request, 'MainApp/topics.html', context) #this gets us info from the DB and rendering the page

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id) #need to use get to get a singular topic.

    entries = topic.entry_set.all()

    context = {'topic':topic, 'entries':entries} #passes information from the view to use in the template

    return render(request, 'MainApp/topic.html', context) #MainApp/topic.html this is just saying to use the topic file for the template

def new_topic(request):
    if request.method != 'POST': #this means that it's a get request, because it's not a post
        form = TopicForm() #an instance of the form we created in the forms.py file

    else:
        form = TopicForm(data=request.POST) #data is coming in from request.POST

        if form.is_valid():
            new_topic = form.save() #will directly save it to the database

            return redirect('MainApp:topics')

    context = {'form': form}
    return render(request, 'MainApp/new_topic.html', context)