# Import the path from django.urls.
from django.urls import path
# Import the views
from . import views

# set the url pattern
urlpatterns = [
    # setting up a path for the index
    # first param empty sets to '/'
    # second param is the view
    # third param is the name of the view
    path('', views.index, name='index'),
]