from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model): #inheriting all the properties of the models class
    text = models.CharField(max_length=200) #name of the topic
    date_added = models.DateTimeField(auto_now_add=True) #we don't have to explicitly say the date, it will automatically display the current date
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self): #allows us to return actual information
        return self.text #if you said print(Topic) it would now give you the name of the topic


class Entry(models.Model): #have to associate entries with topic
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) #many entries to one topic, entry is a foreign key to topic
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta: #used to define to define the plural name
        verbose_name_plural = 'entries'

        
    def __str__(self):
        return f'{self.text[:50]}...' #show a ... after 50 characters 

