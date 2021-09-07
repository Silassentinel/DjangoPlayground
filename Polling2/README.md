
# This is a playground repo for exploring Django

## steps for polling site

-- cd into your projectsFolder( where you'll want the project to be located)

1. make sure pipenv is installed
    1. create virtual env by (pipenv shell)
    2. install django INSIDE the pipenv not globally *facepalm* by (pipenv install django)

2. Create Django Project: 
    1. django-admin startproject \<projectName>
    2. cd into the project folder
    3. run server by (python manage.py runserver)
    *bash will give you info about missing migrations (python manage.py migrate)* 

3. Create app within the project
    1. python manage.py startapp \<appName>


4. Create a Model in new app (in models.py):
    1. Class name: \<className>
        1. Fields:
        2. define string method (def \<fieldName> (self): return self.\<fieldName>)

5. Create a second Model in new app (in models.py):
    1. Class name: \<className>
        1. Fields:
        2. define string method (def \<fieldName> (self): return self.\<fieldName>)

6. Make a migration:
    1. python manage.py makemigrations \<appName>

7. Migrate models to the DB to create tables
    1. Add in Project folder's settings.py file:
    @ installed apps: '\<appName>.apps.\<AppName>Config'
    2. python manage.py makemigrations \<appName>

8. Add data to DB:
    1. python manage.py shell
    2. from \<appName>.models import \<className>, \<className>
    3. from django.utils import timezone
    4. \<className>.objects.create(\<fieldName>=\<value>, \<fieldName>=\<value>, ...)
    || (q = \<ClassName>(\<fieldName>="\<value>", \<fieldName>="\<value>", ...) then q.save()

9.  Add admin/superuser
    1. python manage.py createsuperuser
    2. Enter username, password, email

10. Start server ()
    1. python manage.py runserver
    2. open browser to localhost:8000
    3. login with admin user + pw
    

EXTRA
----

add in polls/admin.py:

    1. A new class \<ClassName>Inline(admin.TabluarInline):
        1. Set the model to \<className>
        2. Set the number of wanted fields to \<numberOfFields>
    2. Another class \<ClassName>Admin(admin.ModelAdmin):
        1. Add the fieldsets to control the layout of the 'add' and 'change pages':
        (Tuple (name,field_option))
            1. (None, {'fields',['\<Model.attribute>']}) 
                1.(none will take the default) 
                2. (fields points to each entry and it will take the default => ['\<Model.attribute>'])
            2. ('Date information', {'fields',['pub_date'],'classes',['collapse']}), 
                1. (Date information will be the name of the fieldset,)
                2. pub_date as collmn name (Date Published)
                3. Classes with option collapse (collapse will collapse the fieldset)
        2. list_display: the order of  the fields to be displayed
        3. list_filter: the fields to be used for filtering
        4. search_fields: the fields to be used for searching
    3. Change the site header 
        1. (admin.site.site_header = '\<header>')
    4. Change the site title
        1. (admin.site.site_title = '\<title>')
    5. Change the index page title
        1. (admin.site.index_title = '\<title>')
    
### Creating views:
In \<appName>/ views.py:
1. Index:
    1. First Route
        1. import the models
        2. define the index which takes a request and returns a rendered template
    2. add new file in \<appName>/urls.py:
        1. Import path from django.urls
        2. Import the views
        3. Name the app: 
            1. app_name = '\<appName>'
        4. set the UrlPattern
            1. First param is empty which resolves to /
            2. Second param is the view
            3. Third param is the name of the view
    3. Add the new URL to the PROJECT UrlPattern
        2. in Urls.py:
            1. Add include from django.urls
            2. Add the path to the new URL
                1. Same as 2.4.1 -> 2.4.3
    4. Add a new template folder
        1. Add a new folder in the templates folder called \<appName>
        2. Add a new file in the new folder called \<appName>_index.html
    5. Add the template dir to the PROJECTS settings.py
        1. import os
        2. Add the new template dir to the TEMPLATES setting:
            1. Dirs: [os.path.join(BASE_DIR, 'templates')]
    6. Add a baseTemplate to the folder templates named base.html
        1. The file will hold the baseSkeleton + Head and links etc
        2. Added blocks to the baseSkeleton for more flexibility:
            1. title
            2. content
    7. in \<appName>/index.html:
        1. Add some bootstrap btn with an A ref which links to the questions via the ID
        click the button goes to polls/1
        2. Add the second bootstrap btn with an A ref which links to the questions via the ID

2. Questions (add in \<appName>/views.py):
    1. Second Route
        1. add to index:
            1. latest_question_list = Question.objects.order_by('-pub_date')[:5]
        2. Add context and pass context to the render function
    2. in \<appName>/index.html:
        1. Add a page heading
        2. check if there are questions
            1. if yes loop through the questions
            2. if no display a message

3. in \<appName>/view.py:
    1. Define a new render method detail
        1. Try to get the question 
        2. If no question display a 404 page
        3. Return a rendered template
    2. in \<appName>/urls.py:
        1. add a new Path to the urlpatterns
            1. Path('\<int:question_id>', views.detail, name='detail')

4. in \<appName>/view.py:
    1. Add a new method called results:
        1. check db for the question or return 404
        2. return a rendered template
    2. in \<appName>/urls.py:
        1. add a new Path to the urlpatterns
            1. Path('results/<int:question_id>', views.results, name='results')

5. Add new HTML FILES
    3. Add new HTML file: detail.html
        1. Extend base.html
        2. Name the title via title block
        3. Add a new block called content
            1. A back btn to the polls
            2. If there is an error display the error
            3. Add CsRF token to avoid forged requests
            4. Loop through all the choices of a question display them in a form with radio btns and labels
            5. Add a submit btn
    9. Add new HTML file: results.html
        1. Extend base.html
        2. Name the title via title block
        3. Add a new block called content
            1. Header with the question
            2. Unordered list with choices
            3. Loop through all the choices an show then as list items
            4. Add a back btn to the polls 
            5. Add a btn vote again
    10. Add new HTML file: vote.html
        1. Extend base.html
        2. Name the title via title block
        3. Add a new block called content

6. In \<appName>/views.py:
    1. Add a new method called vote:
        1. Get the question or return 404
        2. Try to get the choice pk = request.POST['choice']
        3. If no choice is made
            1. Create an error message
            2. Redirect to the details page with the error message
        4. Else Save the vote
7. in \<appName>/urls.py:
    1. Add a new Path to the urlpatterns
        1. Path('<int:question_id>/vote', views.vote, name='vote')

### creating a nav bar via partials

1. add new folder in templates called partials
   1. Add a new file in the partials folder called _navbar.html
   2. Add a bootstrap navbar to the file
        1. Href '/'
        2. Text 'Home'
2. Add the new navbar to the base.html

### create landing page

!! make sure you are in project directory !!

1. run in terminal python manage.py startapp pages
2. create a view in pages/views.py:
    1. return index.html from pages app folder
3. create a pages/urls.py file
    1. Add 1 path to the urlpatterns
        1. Path('', views.index, name='index')
4. Add the new url to the project urls.py
    1. Path('', include('pages.urls'))
5. Add a folder to Templates called pages
    1. Add a new file in the pages folder called index.html
        1. Name the page via the title block
        2. Add a new block called content
            1. Add a card with a welcome message
            2. Add a btn with a link to the polls