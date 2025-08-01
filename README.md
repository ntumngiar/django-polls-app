# Django Polls App

This repository contains a complete Django poll application following the official Django tutorial.

## About
This project is a basic poll application following the [Django Tutorial](https://docs.djangoproject.com/en/5.2/intro/tutorial01/).

## Features
- A public site that lets people view polls and vote in them
- An admin site that lets you add, change, and delete polls
- Testing with Django's testing framework

## Setup
1. Clone the repository: `git clone https://github.com/ntumngiar/django-polls-app.git`
2. Navigate to the project: `cd django-polls-app/djangotutorial`
3. Create a virtual environment: `python -m venv .venv`
4. Activate the virtual environment:
   - Windows: `.\.venv\Scripts\activate`
   - Unix/MacOS: `source .venv/bin/activate`
5. Install dependencies: `pip install django`
6. Run migrations: `python manage.py migrate`
7. Create a superuser: `python manage.py createsuperuser`
8. Run the development server: `python manage.py runserver`
9. Visit http://127.0.0.1:8000/polls/ to see the polls
10. Visit http://127.0.0.1:8000/admin/ to access the admin interface
