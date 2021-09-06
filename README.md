# Internship_project

To run project first you need to create a virtual environment:

  >> python3 -m venv [VenvName]
 
Then you need to install all packages:

  >> pip install -r requirements.txt
  
Then you should create your database and set all changes:

  >> python manage.py makemigration
  >> python manage.py migrate
  
  
  
To Create some data you need have a User as admin permission:

  >> python manage.py createsuperuser
  
Then go to localhost:8000/admin and create your data.

To run project:

  >> python manage.py runserver
