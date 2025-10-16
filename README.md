# 🎓 Educa - Django Learning Management System

A modern, dockerized Learning Management System (LMS) built with Django, featuring real-time chat, course management, and scalable architecture.

![Django](https://img.shields.io/badge/Django-5.1-green)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)
![WebSockets](https://img.shields.io/badge/WebSockets-Enabled-orange)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)

## 🚀 Features

### 📚 Course Management
- **Subjects & Categories**: Organize courses by subjects
- **Course Creation**: Build comprehensive courses with modules
- **Module System**: Structured learning with sequential modules
- **Rich Content**: Support for text, video, images, and files

### 💬 Real-time Communication
- **Module Chat**: Real-time chat within each course module
- **WebSocket Support**: Instant messaging using Django Channels
- **Live Discussions**: Interactive learning experience

### 🏗️ Modern Architecture
- **Dockerized**: Easy deployment with Docker Compose
- **Production Ready**: Nginx, Gunicorn, and Daphne setup
- **Scalable**: PostgreSQL database with Redis caching
- **SSL Secure**: HTTPS encryption with custom certificates

## 🛠️ Tech Stack

**Backend:**
- Django 4.2+ (Python)
- Django Channels (WebSockets)
- PostgreSQL (Database)
- Redis (Caching & Channels layer)

**Servers:**
- Gunicorn (WSGI HTTP Server)
- Daphne (ASGI Server for WebSockets)
- Nginx (Reverse Proxy & Static Files)

**Infrastructure:**
- Docker & Docker Compose
- Custom SSL Certificates
- Multi-container architecture

## 📦 Quick Start

### Prerequisites
- Docker & Docker Compose
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Priyansh-A/educa.git
   cd educa
2. **Build in Docker**
   ```bash
   docker-compose up --build
3. **Add the domain in config/ngnix/default.conf to your hosts or make a custom host**
4. **Create Superuser for admin privilages**
   ```bash
   docker-compose exec web python manage.py createsuperuser
6. **Various urls you can visit**

# 🌐 Available URLs

## 📍 Public Pages (No Login Required)
- `/` - Homepage with all courses list
- `/course/subject/<subject>/` - Courses filtered by subject
- `/course/<slug>/` - Course detail page  
- `/accounts/login/` - User login page
- `/students/register/` - Student registration page

## 👨‍🏫 Instructor Pages (Requires Instructor Privileges)
- `/course/mine/` - List courses created by current instructor
- `/course/create/` - Create a new course
- `/course/<pk>/edit/` - Edit existing course
- `/course/<pk>/delete/` - Delete course
- `/course/<pk>/module/` - Manage course modules
- `/course/module/<module_id>/content/<model_name>/create/` - Add content to module
- `/course/module/<module_id>/content/<model_name>/<id>/` - Edit existing content
- `/course/content/<id>/delete/` - Delete content
- `/course/module/<module_id>/` - View all contents in a module
- `/course/module/order/` - Reorder modules (AJAX)
- `/course/content/order/` - Reorder content within modules (AJAX)

## 🎓 Student Pages (Requires Student Login)
- `/students/courses/` - Student's enrolled courses dashboard
- `/students/enroll-course/` - Course enrollment endpoint
- `/students/course/<pk>/` - Student course detail view
- `/students/course/<pk>/<module_id>/` - Specific module in student course view
- `/chat/room/<course_id>/` - Course chat room

## 🔐 Admin & Authentication
- `/admin/` - Django admin interface
- `/accounts/login/` - User login page
- `/accounts/logged_out/` - Logout confirmation page
