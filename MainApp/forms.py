from django import forms

from .models import Topic


class TopicForm(forms.ModelForm):
    #if you want to create custom fields you would do it here
    class Meta: #using the meta class bc we already have a model defined called forms. we don't have to redefine what type of field we want
        model = Topic
        fields = ['text'] #only need the text field
        labels = {'text':''} #can change this to whatever you want