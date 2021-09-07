from django.contrib import admin

# import the created models
from .models import Question, Choice

# Change the header of the admin panel
admin.site.site_header = 'Polls Administration'

# Change the page title
admin.site.site_title = 'Polls Administration area'

# Change the page index title
admin.site.index_title = 'Welcome to the poll admin area'

#register the models to the site
# #do not use this make a tablu and nest according to the model
# admin.site.register(Question)
# admin.site.register(Choice)

# tabluar display
class ChoiceInline(admin.TabularInline):
    # the model to be displayed
    model = Choice
    # the number of extra choices to display
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # the fields to display an array of fields
    # as colums in the admin panel overview
    fieldsets = [
        # None will take the default
        #fields points to each entry and question_text is the name of the attribute/prop of the class
        (None,               {'fields': ['question_text']}),
        # second column:
        # date information: 
        # with the pubdate (date published as colum title)
        # and Classes with the option collapse
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    # the fields to display
    inlines = [ChoiceInline]
    # the order of the fields
    list_display = ('question_text', 'pub_date')
    # the filter options
    list_filter = ['pub_date']
    # the search options
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
