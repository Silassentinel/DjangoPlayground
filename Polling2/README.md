
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

