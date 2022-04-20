from django.contrib import admin

# Register your models here.

from .models import Topic, Entry #have to import it before you register it

admin.site.register(Topic)
admin.site.register(Entry)