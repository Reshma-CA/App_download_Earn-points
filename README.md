
# Project Overview

This project is a web application where users can earn points by simulating the download of apps and uploading screenshots to confirm the action. The admin panel allows admins to manage apps by adding new apps with details such as app photo, app name, category, subcategory, and the number of points awarded for downloading the app. Users can view the available apps, upload screenshots as proof of task completion, and track their points and task progress.


## Features

- Admin Panel
- User Interface
- API Integration
- Simulated Functionality

#### 1. Admin Panel

Admins can add new apps by uploading app images, assigning app names, selecting categories and subcategories, and setting the points for each app.

#### 2. User Interface

Users can sign up, log in, view available apps, upload screenshots for completing tasks, and see their accumulated points and completed tasks.

#### 3. API Integration

The application exposes REST API endpoints for user authentication, app retrieval, and task management.

#### 4. Simulated Functionality

The app download and screenshot upload processes are simulated, allowing users to earn points without downloading real apps. Points are automatically awarded once the screenshot is uploaded.

### Backend
Python Django
### Frontend
HTML5, CSS3, JavaScript
### Database
SQL


## Project Setup Instructions


### 1. Create and Activate a Virtual Environment

Navigate into project folder:

```bash
cd company_task


```

Create a virtual environment (name it venv):

```bash
python -m venv venv

```
Activate the virtual environment:
On Windows:

```bash
venv\Scripts\activate


```
### 2. Install the Required Dependencies

After activating the virtual environment, install the necessary dependencies from the requirements.txt file:

```bash
pip install -r requirements.txt

```

### 3. Create the Django Project

If your project is not already set up, create the main Django project. In your case, if you've already created the project, skip this step.

```bash
django-admin startproject project

```
### 4. Create the Django Apps
Create the two apps: userapp and djadminapp

If your project is not already set up, create the main Django project. In your case, if you've already created the project, skip this step.

```bash
python manage.py startapp userapp
python manage.py startapp djadminapp


```

### 5. Apply Migrations

Run the database migrations to apply the models:

```bash
python manage.py migrate
```
### 6. Run the Development Server

Finally, start the development server to run your application:

```bash
python manage.py runserver

```
This project should now be set up and running on http://127.0.0.1:8000/.

## Usage Instructions


### 1. Cloning the Repository

To get started, clone the repository from GitLab:

```bash
git clone -b deployment https://gitlab.com/app_projects_group/company_task.git


```
### 2. Setting Up the Virtual Environment

Navigate into your project directory and set up a virtual environment:

```bash
cd company_task
python -m venv venv



```
Activate the virtual environment:

```bash
venv\Scripts\activate

```
### 3. Installing Dependencies

Install the required packages using requirements.txt:

```bash
pip install -r requirements.txt

```
### 4. Running Migrations

Apply the database migrations to set up your database schema:

```bash
python manage.py migrate

```
### 5. Creating Superuser (Admin)

If you need to access the Django admin panel, create a superuser:

```bash
python manage.py createsuperuser

```
Follow the prompts to enter your admin credentials.
### 6. Running the Development Server

Start the Django development server to run the application locally:

```bash
python manage.py runserver

```
The application will be accessible at http://127.0.0.1:8000/.

## Project Structure


```bash
company_task/
│
├── venv/                 
│
├── userapp/              
│   ├── migrations/        
│   ├── __init__.py        
│   ├── admin.py           
│   ├── apps.py            
│   ├── models.py          
│   ├── serializers.py     
│   ├── tests.py           
│   ├── urls.py            
│   ├── views.py           
│   ├── templates/        
│   │   └── userapp/       
│   │       └── ...        
│   └── static/            
│       └── userapp/       
│           └── ...        
│
├── djadminapp/            
│   ├── migrations/        
│   ├── __init__.py        
│   ├── admin.py           
│   ├── apps.py            
│   ├── models.py           
│   ├── serializers.py     
│   ├── tests.py           
│   ├── urls.py            
│   ├── views.py           
│   ├── templates/         
│   │   └── djadminapp/    
│   │       └── ...        
│   └── static/            
│       └── djadminapp/     
│           └── ...        
│
├── company_task/          
│   ├── __init__.py        
│   ├── asgi.py            
│   ├── settings.py        
│   ├── urls.py            
│   └── wsgi.py           
│
├── manage.py              
│
├── requirements.txt       
│
├── .env                   
├── .gitignore             
└── README.md              

```

## requirements.txt

```bash
asgiref==3.8.1
Django==4.2.15
djangorestframework==3.15.2
pillow==10.4.0
sqlparse==0.5.1
typing-extensions==4.12.2
tzdata==2024.1

```

## Database Schema Overview
### 1. People

Purpose: Stores user information.
Fields: Username (unique), email, password, confirm_password.
### 2. Category

Purpose: Represents categories for organizing apps.
Fields: Name of the category.
### 3. SubCategory

Purpose: Represents subcategories within a category.
Fields: Name, linked to a Category.
### 4. App

Purpose: Represents apps available in the system.
Fields: Name, link, points awarded, associated Category and Subcategory, image.
### 5. UserProfile

Purpose: Tracks additional information for each user.
Fields: Points earned, tasks completed, linked to People.
### 6. Task

Purpose: Manages tasks related to app screenshots.
Fields: Task name, associated App, screenshot image, points awarded, completion status, linked to UserProfile.

```bash
-- People Table
CREATE TABLE people (
    id SERIAL PRIMARY KEY,
    username VARCHAR(200) UNIQUE NOT NULL,
    email VARCHAR(200) NOT NULL,
    password VARCHAR(200) NOT NULL,
    confirm_password VARCHAR(200) NOT NULL
);

-- Category Table
CREATE TABLE category (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- SubCategory Table
CREATE TABLE subcategory (
    id SERIAL PRIMARY KEY,
    category_id INTEGER REFERENCES category(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL
);

-- App Table
CREATE TABLE app (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    app_link VARCHAR(255) NOT NULL,
    points INTEGER NOT NULL,
    category_id INTEGER REFERENCES category(id) ON DELETE CASCADE,
    sub_category_id INTEGER REFERENCES subcategory(id) ON DELETE CASCADE,
    app_image VARCHAR(255) -- Adjust depending on your storage solution
);

-- UserProfile Table
CREATE TABLE user_profile (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES people(id) ON DELETE CASCADE,
    user_points INTEGER DEFAULT 0,
    tasks_completed INTEGER DEFAULT 0
);

-- Task Table
CREATE TABLE task (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    app_id INTEGER REFERENCES app(id) ON DELETE CASCADE,
    screenshot VARCHAR(255), -- Adjust depending on your storage solution
    points_awarded INTEGER DEFAULT 0,
    completed BOOLEAN DEFAULT FALSE,
    user_profile_id INTEGER REFERENCES user_profile(id) ON DELETE CASCADE
);


```


## API Endpoints
### Admin API

```bash
Categories: GET /api/categories/
SubCategories: GET /api/subcategories/?category_id=<id>
Admin Apps: GET /api/admin_dash/, POST /api/admin_dash/
```

### User API

```bash
Available Apps: GET /api/home/
```

## Usage Instructions
### Admin Side

Access the admin dashboard to manage apps and assign points.
User Side

Users can view available apps, upload screenshots, and track their points and completed tasks.

### Project Screen record link
link: https://youtu.be/xm1aVwBTGd8

### Project hosted link

link: http://3.25.137.55:8000/


### Problem Set I - Regex

```bash
import re

# Sample text
text = '{"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"}]}'

# Regular expression to find numbers after "id": or "code":
pattern = r'(?<=id":)\d+|(?<=code":)\d+'

# Find all matches
matches = re.findall(pattern, text)

# Convert matches to integers
numbers = [int(match) for match in matches]

print(numbers)
```

### Answer

```bash
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 648, 649, 650, 651, 652, 653, 3, 153]

```

## Problem Set 3

### Choice of System: Celery with Redis
Reason for Choice:

Reliability: Celery is a powerful, flexible, and reliable distributed task queue system that can handle periodic tasks efficiently. It integrates well with Django and can be used with various brokers, including Redis, RabbitMQ, and others. Redis is a popular choice as it is fast and easy to configure.

Scalability: Celery supports distributed task processing, meaning you can scale it horizontally by adding more worker nodes as the load increases. This makes it suitable for high-volume and production environments where tasks need to be executed reliably and promptly.

Task Scheduling: Celery supports periodic tasks via Celery Beat, which can schedule tasks to run at specified intervals, such as every 24 hours. This feature makes it suitable for tasks like downloading ISINs at regular intervals.

Flexibility: Celery supports complex workflows and task dependencies, which is advantageous if your task scheduling needs become more complex in the future.

Potential Problems and Recommendations:

Complexity: Setting up Celery with Redis or another broker can be complex, especially for beginners. It requires additional configuration and monitoring.

Resource Management: Redis or other brokers require additional resources and maintenance. You need to ensure that the broker is reliable and scalable.

Task Failures: Handling failed tasks and retries can add complexity. You need to implement proper error handling and monitoring.

Recommendations for Production:

Monitoring and Management: Use monitoring tools like Flower to keep an eye on your Celery workers and tasks.

Fault Tolerance: Implement retries and error handling to ensure that tasks are not lost in case of failures.

Scaling: For large-scale applications, consider using a more robust message broker like RabbitMQ if Redis does not meet your needs.

### B. Using Flask vs. Django

####  Use of Flask:

Simple Applications: Flask is ideal for small to medium-sized applications or microservices where you need minimalistic and flexible web framework features without the overhead of a full-stack framework.

Fine-Grained Control: If you want more control over the components and architecture of your application, Flask allows you to choose and integrate only the components you need, giving you more flexibility.

Learning and Prototyping: Flask’s simplicity makes it an excellent choice for learning web development or quickly prototyping an application.

API-Only Applications: Flask is well-suited for building RESTful APIs where you don’t need a full-featured web framework.

####  Use of  Django:

Full-Featured Applications: Django is suitable for larger applications where you need built-in features like authentication, ORM, and admin interfaces. It follows the "batteries-included" philosophy, providing many built-in functionalities.

Rapid Development: Django's extensive features and built-in tools make it easier to develop complex applications quickly. The Django admin interface, for example, can save a lot of development time.

Scalability and Maintainability: Django’s architecture is designed to handle complex applications and is more suitable for large-scale projects where scalability and maintainability are critical.

Conventions and Structure: If you prefer a framework with a defined structure and conventions, Django provides a robust and opinionated way of building web applications, which can lead to more organized and maintainable code.
