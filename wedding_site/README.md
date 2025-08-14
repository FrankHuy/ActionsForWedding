# Wedding Site Project

This project is a wedding event management system built using Django framework. It allows users to manage wedding events with functionalities for creating, updating, deleting, and viewing events. The project supports two types of users: regular users and event administrators.

## Features

- User registration and login
- Event management (CRUD operations)
- Simple and elegant user interface
- Built with Django and SQLite

## Project Structure

```
wedding_site
├── manage.py
├── README.md
├── requirements.txt
├── wedding_site
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── events
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── templates
│       └── events
│           ├── event_list.html
│           ├── event_detail.html
│           ├── event_form.html
│           └── event_confirm_delete.html
├── users
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── templates
│       └── registration
│           ├── login.html
│           └── signup.html
└── static
    └── css
        └── style.css
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd wedding_site
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Run migrations:
   ```
   python manage.py migrate
   ```

4. Create a superuser (for admin access):
   ```
   python manage.py createsuperuser
   ```

5. Start the development server:
   ```
   python manage.py runserver
   ```

## Usage

- Access the application at `http://127.0.0.1:8000/`
- Admin panel can be accessed at `http://127.0.0.1:8000/admin/`

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.