# 🛍️ Pfact Product Review System – Backend API

A Django REST Framework-based backend for managing products and their reviews, supporting JWT authentication, admin control, and rating aggregation.

> ✅ Completed as part of a technical assignment

---

## 🚀 Features

- 🔐 JWT-based login & registration
- 👥 Role-based permissions (Admin vs Regular user)
- 🛒 Product CRUD for admins
- ✍️ Product reviews by authenticated users
- ⭐ Average rating shown per product
- 🚫 Prevent duplicate reviews per product-user
- 🧪 Postman collection included for testing

---

## 🧱 Tech Stack

- **Backend**: Django 5, Django REST Framework
- **Auth**: JWT via `djangorestframework-simplejwt`
- **Database**: SQLite (for dev)

---

## 📦 API Endpoints

### 🔐 Auth

| Method | Endpoint                     | Access       | Description              |
|--------|------------------------------|--------------|--------------------------|
| POST   | `/api/users/register/`       | Public       | Register a user          |
| POST   | `/api/users/login/`          | Public       | Get JWT tokens           |
| POST   | `/api/users/token/refresh/`  | Public       | Refresh access token     |

---

### 🛒 Product

| Method | Endpoint                           | Access        | Description             |
|--------|------------------------------------|---------------|-------------------------|
| GET    | `/api/products/`                   | Public        | List all products       |
| GET    | `/api/products/<id>/`              | Public        | Product detail          |
| POST   | `/api/products/create/`            | Admin only    | Create product          |
| PUT    | `/api/products/<id>/update/`       | Admin only    | Update product          |
| DELETE | `/api/products/<id>/delete/`       | Admin only    | Delete product          |

---

### ✍️ Reviews

| Method | Endpoint                        | Access        | Description                     |
|--------|----------------------------------|---------------|---------------------------------|
| GET    | `/api/reviews/?product=<id>`    | Public        | List reviews for product        |
| POST   | `/api/reviews/create/`          | Authenticated | Submit a review (1 per user)    |

---

## 🧪 Postman Collection

📁 `PfactReviewSystem.postman_collection.json`  
Includes:
- Register
- Login
- Product browse
- Create review with token

---

## ⚙️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/Pr1ncePS2002/Pfact.git
cd Pfact
```

### 2. Create the virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```
###4. Create a super user and run the server

```bash
python manage.py createsuperuser
python manage.py runserver




