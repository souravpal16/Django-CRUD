# Django-CRUD

<img src="imgg/postgresqlimg.png" width="400" height="400"> | <img src="https://static.djangoproject.com/img/logos/django-logo-positive.png" width="500" height="400"> 
## Description:
This project is based on Django and emphasizes the use of CRUD using postgresql. Its allows the user to make pizza based on the sizes and toppings available in the database.
The user can add other sizes of pizza and toppings available to make the pizza. The options available to make a pizza is totally dependent on the toppings available in the 
database. All the pizzas made by the user can be viewed at a place and if need be, the user can delete and edit the pizzas made. Specific pizzas made by the user can 
be filtered based on size and type of pizza.

## Various Endpoints:
The endpoints are relative to the domain name. For development purposes, '127.0.0.1:8000' was used locally.
1. 'admin/' : This takes the user to the admin page which comes built-in with Django.
2. '' : This is the homepage with name = "index". 
3. 'create/' : Here the user can create a new pizza based on the toppings, size available in the database. The type of pizza can be either 'Regular' or 'Square'
4. 'AllPizza/ : Here the user can see all the pizzas made by him/her. The pizzas viewed can be filterd based on the type of pizza or/and size of pizza. The pizzas
                can also be edited or deleted.
5. 'Delete/<int:pk>' : if the user chooses to delete a pizza, then the user is redirected here. Using pk value, the object is deleted from the database.
6. 'Edit/<int:pk>' : if the user chooses to edit any pizza, then the user is redirected here and can choose the desired options. 
7. 'NoPizza/<int:pk> : if the user wants to see all the pizzas but haven't created any, then the user is redirected to this page. 
8. 'Layout/' : Here, the user can add more toppings or sizes to the database. If a topping or any particular size is not available in the database then the user cannot 
               cannot create a pizza with that.
               
## How To Use:
1. You should have postgresql installed.
2. Open PgAdmin 4 and make a database named Pizza.
3. in the settings the DATABASES dictionary has a default key which needs to be configured according to postgresql installed in your PC like my default key has the following value:
'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Pizza',
        'USER': 'postgres',
        'PASSWORD': 'testing4916',
        'HOST': 'localhost',
        'PORT': '',
    }
4. Open psql which is postgresql command shell and enter the details.
5. Installing everything from the requirements.txt
6. On your command prompt, navigate to the folder where manage.py is located.
7. run python manage.py migrate, then python manage.py makemigrations, then python manage.py migrate to migrate your database and to be on the safe side.
8. Then run python manage.py runserver --insecure and open 127.0.0.1:8000 on your browser. --insecure because DEBUG is set to False in settings.py
