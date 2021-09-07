from django.contrib import admin

# import the created models
from .models import Question, Choice

#register the models to the site
admin.site.register(Question)
admin.site.register(Choice)

