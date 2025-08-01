# Django Tutorial Progress

This repository contains my progress through the Django tutorial from the official Django documentation.

## About
This project is a basic poll application following the [Django Tutorial](https://docs.djangoproject.com/en/5.2/intro/tutorial01/).

## Features
- A public site that lets people view polls and vote in them
- An admin site that lets you add, change, and delete polls
- Testing with Django's testing framework

## Setup
1. Clone the repository
2. Create a virtual environment: `python -m venv .venv`
3. Activate the virtual environment:
   - Windows: `.\.venv\Scripts\activate`
   - Unix/MacOS: `source .venv/bin/activate`
4. Install dependencies: `pip install django`
5. Run migrations: `python manage.py migrate`
6. Run the development server: `python manage.py runserver`
