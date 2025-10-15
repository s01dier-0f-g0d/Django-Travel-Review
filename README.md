# 🌍 Travel Review Web App (Django)

A modern **Travel Review and Destination Explorer** built with **Django**.  
Users can browse, search, add, edit, and review travel destinations — each with ratings, cost.  
The app includes smooth animations, responsive design, and a stylish flash message system for feedback.

---

## ✨ Overview

The **Travel Review App** lets users:
- 🏝️ Explore travel destinations  
- ✏️ Create, update, or delete destination reviews  
- 🔍 Search destinations by name, country, rating, or cost  
- 💬 Get instant pop-up messages for all actions  
- 📸 Upload optional images for each destination  

It’s a fully responsive Django CRUD app with a modern UI.

---

## 🧭 Features

| Feature | Description |
|----------|-------------|
| 🏠 **Home Page** | Landing page introducing the app |
| 📋 **Destination List** | View all destinations dynamically |
| 🔍 **Search Bar** | Search by `name`, `country`, `rating`, or `average_cost` |
| ✨ **CRUD Operations** | Create, update, delete destinations easily |
| 💬 **Django Messages** | Animated flash messages for user feedback |
| 📱 **Responsive UI** | Works on desktop and mobile devices |

---

## 🧩 Data Model

### `Destination` Model
Defined in `models.py`

## 🗂️ Views Overview
| Function                          | Purpose                                       |
| --------------------------------- | --------------------------------------------- |
| `home(request)`                   | Renders the homepage                          |
| `display(request)`                | Lists all destinations (with optional search) |
| `create(request)`                 | Handles destination creation                  |
| `update(request, key)`            | Updates a destination by ID                   |
| `deleteDestination(request, key)` | Deletes a destination                         |
| `specific(request, key)`          | Shows details for a single destination        |

## ⚙️ Tech Stack
| Category          | Technology                                 |
| ----------------- | ------------------------------------------ |
| **Backend**       | Django 5+, Python 3.10+                    |
| **Frontend**      | HTML5, CSS3, JavaScript            |
| **Database**      | SQLite (default)                           |
| **Styling**       | Custom CSS (navbar, cards, toast messages) |
| **Notifications** | Django `messages` Framework                |

## ⚡ Setup Instructions

## 1️⃣ Clone the Repository
> git clone https://github.com/s01dier-0f-g0d/Django-Travel-Review.git
> cd Django-Travel-Review

## 2️⃣ Create and Activate a Virtual Environment
> python -m venv venv
> source venv/bin/activate        # macOS/Linux
> venv\Scripts\activate           # Windows

## 3️⃣ Install Dependencies
> pip install django

## 4️⃣ Apply Migrations
> python manage.py makemigrations
> python manage.py migrate

## 5️⃣ Create Superuser (Admin Access)
> python manage.py createsuperuser

## 6️⃣ Run the Development Server
> python manage.py runserver 7001
