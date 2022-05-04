from django.shortcuts import render, redirect
from .forms import TopicForm, EntryForm

from .models import Topic, Entry
from django.contrib.auth.decorators import login_required
from django.http import Http404
# Create your views here.

def index(request): #name of the view is index bc in urls.py we said views.index
    return render(request, 'MainApp/index.html') #rendering a page on your browser using index.html as a template

@login_required
def topics(request):
    topics = Topic.objects.filter(owner=request.user).order_by("-date_added")#can't use objects.all if we want to do order by. this will do it in ascending order (this might not be true)

    #we need to move the data to our page by using a dictionary --> referred to as context

    context = {'topics':topics} #the key 'topics' is what you have to refer to in the html. the value is whatever you call it in the view

    return render(request, 'MainApp/topics.html', context) #this gets us info from the DB and rendering the page

@login_required
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id) #need to use get to get a singular topic.

    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.all()

    context = {'topic':topic, 'entries':entries} #passes information from the view to use in the template

    return render(request, 'MainApp/topic.html', context) #MainApp/topic.html this is just saying to use the topic file for the template

@login_required
def new_topic(request):
    if request.method != 'POST': #this means that it's a get request, because it's not a post
        form = TopicForm() #an instance of the form we created in the forms.py file

    else:
        form = TopicForm(data=request.POST) #data is coming in from request.POST

        if form.is_valid():
            new_topic = form.save() #will directly save it to the database
            new_topic.owner = request.user
            new_topic.save()
            return redirect('MainApp:topics')

    context = {'form': form}
    return render(request, 'MainApp/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id) #need to use get to get a singular topic.

    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)

        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic #here we are assigning the topic attribute before we save it to the database
            new_entry.save()
            return redirect ('MainApp:topic', topic_id=topic_id) #we need to give it the specific topic page to load
    

    context = {'form':form, 'topic':topic} #passes information from the view to use in the template

    return render(request, 'MainApp/new_entry.html', context) # this is just saying to use the entry html file for the template

@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic #use the variable entry that's storing the object

    if request.method != 'POST':
        form = EntryForm(instance=entry) #loading the specific form from the database
    
    else:
        form = EntryForm(instance=entry, data=request.POST) #when we're saving, we want it to save to the same object with the new information


        if form.is_valid():
            form.save()
            return redirect('MainApp:topic',topic_id=topic.id)
    
    context = {'form':form, 'topic':topic, 'entry':entry}
    return render(request, 'MainApp/edit_entry.html', context)
            

