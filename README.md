# Django Web Development

A practical Django project demonstrating **forms, validation, ModelForms, static and media files, ORM relationships, and user authentication**.

## Features

* Django `Form` with custom validation
* `ModelForm` with database integration
* Student registration
* Student profile image upload
* Static files and custom CSS
* Student–Course `ManyToManyField` relationship
* ORM queries using:

  * `filter()`
  * `exclude()`
  * `order_by()`
  * `annotate()`
  * `aggregate()`
* User registration
* Login and logout
* Protected student registration using `@login_required`
* Dynamic logged-in username
* CSRF protection

## Tech Stack

* **Python**
* **Django 6.1**
* **SQLite**
* **HTML / CSS**
* **Git & GitHub**

## Project Structure

```text
django-web-development/
├── config/
├── students/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── forms.py
│   ├── models.py
│   └── views.py
├── media/
├── static/
├── manage.py
└── requirements.txt
```

## Setup

Clone the repository:

```bash
git clone <repository-url>
cd django-web-dev
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```
#### Linux
```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Apply migrations:

```bash
python manage.py migrate
```

Create a superuser:

```bash
python manage.py createsuperuser
```

Run the development server:

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## Purpose

This project was developed as part of **Week 14 Django Web Development practical coursework**, with the goal of implementing core Django features in a single integrated application.
