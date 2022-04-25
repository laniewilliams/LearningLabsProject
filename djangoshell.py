import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","learning_log.settings")

import django
django.setup()

from MainApp.models import Topic #from the models file we're importing Topic

topics = Topic.objects.all() #getting all the Topic objects (chess and rock climbing)

for t in topics: #going through each one and printing out t.id and t
    print(t.id,' ',t) #just said t because of the string method in models.py. in Class Topic we used the string method to return text

t = Topic.objects.get(id=1) #returning just the chess object. greater than (gt), greater than or equal to (gte), less than (lt)

#t is an object and has attributes. It has the text attribute and the date_added attribute.

print(t.text)
print(t.date_added)

entries = t.entry_set.all() #because entry is a foreign key to the topic, you get all the corresponding objects related to that specific topic

for e in entries:
    print(e) #can just say e instead of e.text because of the string method