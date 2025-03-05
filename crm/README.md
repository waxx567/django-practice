# Customer Relationship Management (CRM) Application

A user-friendly CRM project for comprehensive customer data control featuring full create, read, update, and delete (CRUD) capablities, event management and flash message notifications through an easy-to-operate UI.

## 🛠️ Tech Stack

- `Django`
- `HTML`
- `JavaScript`
- `CSS`
- `Python`
- `Bootstrap`
- `Crispy Forms`
- `Font Awesome`

## ⚙️ Installation Guide

Follow these steps to install and set up the CRM app:

### 1. Set Up a Virtual Environment

1. Open **Anaconda Prompt** and navigate to your desired project folder.
2. Create a virtual environment:
   ```sh
   conda create --name vEnv python=3.12
   ```
3. Activate the virtual environment:
   ```sh
   conda activate vEnv
   ```

### 2. Install Django

```sh
pip install django
```

Confirm installed packages:
```sh
pip list
```

### 3. Create Django Project & Application

1. Start a new Django project:
   ```sh
   django-admin startproject crm
   ```
2. Navigate into the project directory:
   ```sh
   cd crm
   ```
3. Run the server to verify installation:
   ```sh
   py manage.py runserver
   ```
4. Open [localhost:8000](http://127.0.0.1:8000) in your browser.
5. Stop the server with `Ctrl + C`.
6. Create a new Django app:
   ```sh
   django-admin startapp webapp
   ```

### 4. Configure Django Settings

Update `settings.py` as per the [GitHub reference](https://github.com/waxx567/django-practice/tree/main/crm) using commit `f107ed50e679f0091b16ebfe9659f514c3c6aa97`.

### 5. Migrate Django Database & Create Superuser

```sh
py manage.py migrate
```

Create a superuser:
```sh
py manage.py createsuperuser
```

Run the server again:
```sh
py manage.py runserver
```

### 6. Install Crispy Forms

To use Django Crispy Forms, install the specific version:
```sh
pip install django-crispy-forms==1.14.0
```

Confirm packages in the virtual environment:
```sh
pip list
```

### 7. Freeze Requirements

To save the package dependencies, run:
```sh
pip freeze > requirements.txt
```

## 🏁 Running the Application

1. Start the Django development server:
   ```sh
   py manage.py runserver
   ```
2. Open [localhost:8000](http://127.0.0.1:8000) in your browser.

## 🔑 User Login

Create your own account and explore the app to your heart's content!

---
If you have any feedback, suggestions or advice, [email](feedback@fivefiftyfive.io) me. Let's chat!
