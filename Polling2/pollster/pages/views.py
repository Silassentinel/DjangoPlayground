from django.shortcuts import render

# define a method which will render a static lading page
def index(request):
    return render(request, 'pages/index.html') 
