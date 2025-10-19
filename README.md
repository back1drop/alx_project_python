# 🎬 Movie Review API

A **RESTful API** built with **Django** and **Django REST Framework (DRF)** that allows users to create, read, update, and delete movie reviews.  
The API supports **JWT authentication**, **permissions**, **filtering**, **searching**, and **pagination** for a complete movie review management experience.

---

## 🚀 Features

### 🎥 Review Management
- Create, read, update, and delete (CRUD) movie reviews.  
- Each review includes:
  - **Movie Title**
  - **Review Content**
  - **Rating (1–5)**
  - **User (owner)**
  - **Created Date**

### 👤 User Management
- Manage users via CRUD operations.
- Each user has a **unique username**, **email**, and **password**.

### 🔐 Authentication
- Uses **JWT (JSON Web Token)** authentication for secure API access.
- Authenticated users can:
  - Create reviews
  - Edit or delete only their own reviews
- Unauthenticated users can only view reviews.


### 🔎 Filtering, Searching, and Sorting
- **Filter** reviews by `movie_title` or `rating`.
- **Search** reviews by title or exact rating.
- **Order** reviews by `rating` or `created_date`.

### 📄 Pagination
- Paginated responses (default: 10 reviews per page) for better performance with large datasets.

---

## 🧠 Tech Stack

| Layer | Technology |
|-------|-------------|
| **Backend Framework** | Django, Django REST Framework |
| **Database** | SQLite (default)  |
| **Authentication** | JWT (via `djangorestframework-simplejwt`) |
| **Filtering** | Django Filter |
| **Pagination** | DRF built-in pagination |
| **Language** | Python 3 |

---

## ⚙️ Installation and Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/movie-review-api.git
cd movie-review-api
