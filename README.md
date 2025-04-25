# 📚 Library Management API

This is a RESTful API for a Library Management System built using Django Rest Framework. It supports user registration, login with JWT, role-based permissions for librarians, and book borrowing features.

---

## 🚀 Features

- User Registration & JWT Login
- Custom User Model with Roles (User & Librarian)
- Librarian-only permissions to Add/Update/Delete Books
- Borrow and Return Books
- Book availability tracking
- Search & Order Books by title, author, and genre
- Pagination Support
- Token Authentication using JWT

---

## 🔧 Tech Stack

- Python 3.x
- Django
- Django Rest Framework (DRF)
- SimpleJWT
- SQLite (default, can be swapped with PostgreSQL)

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/library-api.git
   cd library-api

2. **Create and activate virtual environment**
    ```bash
   python -m venv env source env/bin/activate

3. **Install dependencies**
4. ```bash
   pip install -r requirements.txt
   
5. **Apply migrations**
    ```bash
   python manage.py makemigrations
   python manage.py migrate

6. Run the server
   ```bash
   python manage.py runserver
