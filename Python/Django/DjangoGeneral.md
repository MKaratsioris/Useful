## Documentation
https://docs.djangoproject.com/en/5.0/

## Install

```bash
python3 -m pip install Django
```

Check that installation was success

```bash
pip freeze | grep 'Django'
```

or

```bash
django-admin
```

## Project

#### Start
Navigate into the directory you want to save the project and then run the following command
```bash
django-admin startproject <project-name>
```

#### Admin User

```bash
python3 manage.py migrate
python3 manage.py createsuperuser
```
If you want to add a product from the Database to the admin page, then inside app-name/admin.py add:
```python
from django.contrib import admin
from .models import <product-name>

admin.site.register(<product-name>)
```


#### Launch local dev server
A convenient way to preview your project.

From the project root directory run the following command
```bash
python3 manage.py runserver
```
Stop the server by pressing Ctrl+C.

#### Apps
Django projects embrace a modular structure. So a Django project often consists of multiple modules that make up the project. Those modules are not called modules, though, but apps, and you then do store your actual application code in those apps. So you don't really work in this main project sub-folder, which was created for you, but instead, to add different features to your entire project, you would add multiple apps that hold those features.

To create a new app, run the following command (stop the server first...)
```bash
python3 manage.py startapp <app-name>
```

#### Structure
- project-name/urls.py: All the routes of the webapp.
- app-name/view: Views are responsible for processing requests and creating responses. They can be either a Function or a Class.
- app-name/templates/app-name/template-name.html: this is considered as good practice because, under the hood, Django merges all the `templates/` folders into one. This way, including the app-name as a folder inside each templates folder, we avoid possible future confusion. Remember to include the app-name in the `INSTALLED_APPS` list variable inside project-name/settings.py. This way, it is guaranteed that Django will search for the templates folder in each application that is included in the list.
- app-name/static/app-name/: same as for the `templates/` folder. In this folder we can save images, css files, etc.
- app-name/models.py: Here we can create classes that will represent a table in the database.
- app-name/migrations/: Here we can create migrations or instructions for Django to create or update the database. We always have to create the migrations by running the following command
    ```bash
    python3 manage.py makemigrations
    ```
    and then run the migrations by running the following command
    ```bash
    python3 manage.py migrate
    ```

#### Database
To interact with the database through cmd run the following command
```bash
python3 manage.py shell
```

## Quick Start Steps
- Create project
    ```bash
    django-admin startproject <project-name>
    ```
- Create app
    ```bash
    python3 manage.py startapp <app-name>
    ```
    and add it in the projest settings file `<project-name>/<project-name>/settings.py`, in the list INSTALLED_APPS:
    ```python
    ...
    INSTALLED_APPS = [
        '<app-name>',
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
    ]
    ...
    ```
- Create the following folders:
    
    -> `<project-name>/<app-name>/templates/<app-name>` for html files
    
    -> `<project-name>/<app-name>/static/<app-name>` for all static files like css, images, videos, etc.
- Create a `urls.py` file in the folder `<project-name>/<app-name>/` with the following script:

    ```python
    from django.urls import path

    from . import views

    urlpatterns = [
        path("", views.<app-name>, name="<app-name>"), # http://127.0.0.1:8000/<app-name>/ : This is the landing page of the app
    ]
    ```
- Add, in the file `<project-name>/<project-name>/urls.py`, inside the urlpatterns list the following path: 

    ->  `path("<app-name>/", include("<app-name>.urls"))`
    the resulting file should look something like this:
    ```python
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path("admin/", admin.site.urls),
        path("<app-name>/", include("<app-name>.urls")),
    ]
    ```
- After creating the html files, run the development server:
    ```bash
    python3 manage.py runserver
    ```
- If you will need to use a database:

    - First create your schema in the `<project-name>/<app-name>/models.py`, i.e.:
    ```python
    from django.db import models
    from django.core.validators import MinValueValidator, MaxValueValidator

    class Review(models.Model):
        name = models.CharField(max_length=100)
        email = models.EmailField(max_length=100)
        review = models.TextField(max_length=200)
        rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    ```
    - Run the following commands every time you make a change in the models:
    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```
    - Import the models in the file `<project-name>/<app-name>/views.py`.