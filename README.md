# Sticky Notes Application

A Django-based web application designed to allow users to create, view, update, and delete sticky notes. Built as part of the HyperionDev Software Engineering curriculum to demonstrate Object-Oriented Software Design, Model-View-Template (MVT) architecture, and CRUD operations.

---

## 📁 Project Structure

```text
sticky_notes/
│
├── diagrams/                  # Design & architecture diagrams
│   ├── use_case_diagram.png
│   ├── sequence_diagram.png
│   └── class_diagram.png
│
├── sticky_notes/              # Core Django project configuration folder
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py            # Main project settings
│   ├── urls.py                # Main URL routing
│   └── wsgi.py
│
├── notes/                     # Primary Django application
│   ├── migrations/            # Database migration files
│   ├── templates/             # HTML templates for rendering views
│   │   └── notes/
│   │       ├── base.html
│   │       ├── note_list.html
│   │       ├── note_detail.html
│   │       └── note_form.html
│   ├── static/                # Static files (CSS/styles)
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py               # ModelForm definitions
│   ├── models.py              # Note database models
│   ├── tests.py               # Unit tests
│   ├── urls.py                # App-specific URL routes
│   └── views.py               # View logic for handling CRUD requests
│
├── manage.py                  # Django CLI management utility
├── README.md                  # Project documentation and instructions
└── requirements.txt           # Virtual environment dependencies