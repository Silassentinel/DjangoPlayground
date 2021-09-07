# Import the path from django.urls.
from django.urls import path
# Import the views
from . import views

# name the app
app_name = 'polls'
# set the url pattern
urlpatterns = [
    # setting up a path for the index
    # first param empty sets to '/'
    # second param is the view
    # third param is the name of the view
    path('', views.index, name='index'),
    # first is the url parameter
    # second is the view
    # thrid is the name
    path('<int:question_id>/', views.detail, name='detail'),
    # first is the url parameter
    # second is the view
    # third is the name
    path('<int:question_id>/results/', views.results, name='results'),
    # first is the url parameter
    # second is the view
    # third is the name
    path('<int:question_id>/vote/', views.vote, name='vote'),
]