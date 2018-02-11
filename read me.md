Launch Project 
    $ dajngo-admin startproject projectname
Start App

Create first view to test app
	1. Write:
			from dajngo.http import HttpResponse

			def index(request):
				return HttpResponse("Say Something")

	2. Link view in url:
		#Create a 'urls.py' file in app dir and enter:
				from django.urls import path
				from . import views

				urlpatterns = [
    				path('', views.index, name='index'),

				]
	3. Link app to project in project 'urls.py':
			from django.contrib import admin
			from django.urls import include, path

			urlpatterns = [
    			path('blog/', include('blog.urls')),
    			path('admin/', admin.site.urls),
    
			

			]

Activate Database:
	$ python manage.py migrate

Create Models:
	1. Create database models in models.py file in app dir
	2. To use the models created, activate it in <settings.py> in project dir by adding 'app_name.apps.App_nameConfig', to installed apps
	3. To create migrations for those changes:
           $ python manage.py makemigrations
	

	4. Run migrations :
           $ python manage.py sqlmigrate app_name 0001
	5. To apply those changes to database, run:
    		$ python manage.py migrate

    	NB: Always repeate 3 when you make changes to models.

Create Admin User:
	1. Run:
		$ python manage.py createsuperuser
	2. Enter username for admin
	3. Enter email
	4. Enter password
	5. Open admin.py in app dir, add: 
		 from . import models

		 admin.site.register(models.classname)
	   to make app modify app in admin inter face

Write Views, open views.py in app dir to edit:
	1. Import models using:
		from .models import classname
	2. Create your view
	3. Add views into urlpatterns in urls.py in app dir
	4. Write raise 404 error




