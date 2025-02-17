# Welcome to StudyBuddy

## 🤖 Introduction

StudyBuddy is a web application that allows you to create and join study rooms with your friends. A sort of a Discord clone. You can chat, share files, and collaborate on projects in real-time. Get started by creating a new room or joining an existing one.

## ⚙️ Tech Stack

    - Python
    - Django

---

## Developer's Build Notes

### 🔋 2024/12/30

#### Setup

- Create GitHub repository from GitHub Desktop `File->New Repository`

- `79b56954a71042910c6d3db931f81367d44e52cc`

In `cmd prompt`:

- Create virtual environment `python -m venv env`

- Activate virtual environment `env\Scripts\activate.bat`

- Install Django `pip install django`

- `django-admin` to see a list of core commands

- Create Django project `django-admin startproject <your-app-name>`

- Change directory into your app name `cd <your-app-name>`

- Open application `python manage.py runserver`

- Check your browser `localhost:8000` and make sure you can see the app running

- Exit server `CTRL C`

#### Create base app

- Create base app `python manage.py startapp base`

- `pip freeze > requirements.txt`

#### Database

### 🔋 2025/01/02

Create admin user `python manage.py createsuperuser`

Add rooms
