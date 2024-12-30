# Developer's Build Notes

## 2024/12/30

### Setup

Create GitHub repository from GitHub Desktop `File->New Repository`
`79b56954a71042910c6d3db931f81367d44e52cc`
In `cmd prompt`:
Activate virtual environment `python -m venv venv`, then `venv\Scripts\activate.bat`
Install Django `pip install django`
`django-admin` to see a list of core commands
Create Django project `django-admin startproject <your-app-name>`
Change directory into your app name `cd <your-app-name>`
Open application `python manage.py runserver`
Check your browser `localhost:8000` and make sure you can see the app running
Exit server `CTRL C`
