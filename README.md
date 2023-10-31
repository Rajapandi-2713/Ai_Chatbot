# Smart College Chatbot

Our project is a chatbot system designed to assist students in accessing their internal and semester marks, study materials based on 
their department, and personal details using their register number.

# Steps to run a application :

# Step 1 :

Download & Install a python 3.10 or later versions using a below link and set a environment variables.

https://www.python.org/downloads/

Download a mysql and install it. follow the guidelines in a youtube link

https://youtu.be/eq-e_n7lm2M

# Step 2 :

Go to command prompt and run the following commands one by one.

pip install Django
pip install mysql-connector-python
pip install mysqlclient

# Step 3 :

Open a mysql and run the below command for create a database.

create database academic_details;

# Step 4:

Go to chatbot folder and open a settings.py file.

Change a user name and password in the database to your username and password of mysql.

DATABASES = {

'default': {

'ENGINE': 'django.db.backends.mysql',

'NAME': 'academic_details',

'USER':'root', ----> replace with ur username

'PASSWORD':'root', ----> replace with your password 
} }

# Step 5 :

Open a command prompt and go to manage.py location. run the below commands one by one.

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

copy the url like this shown in ur command prompt & paste in ur browser.

http://127.0.0.1:8000/

Now we successfully run a web application.
