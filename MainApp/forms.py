from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    #if you want to create custom fields you would do it here
    class Meta: #using the meta class bc we already have a model defined called forms. we don't have to redefine what type of field we want
        model = Topic
        fields = ['text'] #only need the text field
        labels = {'text':''} #can change this to whatever you want

class EntryForm(forms.ModelForm):
    #if you want to create custom fields you would do it here
    class Meta: #using the meta class bc we already have a model defined called forms. we don't have to redefine what type of field we want
        model = Entry
        fields = ['text'] #only need the text field
        labels = {'text':''} #can change this to whatever you want
        widget = {'text':forms.Textarea(attrs={'cols':80})} #making the text field a text area. This is going to make it look like a big box