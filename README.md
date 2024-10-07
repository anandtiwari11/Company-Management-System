# Company Management System

## Overview
The **Company Management System** is a web application that allows users to manage companies and their employees. Users can create, delete, and perform CRUD (Create, Read, Update, Delete) operations on companies and employees. The backend is developed using Django REST API with ORM, providing a robust and scalable architecture.

## Features
- Create and delete companies
- Perform CRUD operations on employees associated with each company
- Built using Django REST API and ORM
- Flexible and easy to extend

## Technologies Used
- **Backend:** Django, Django REST Framework
- **Database:** PostgreSQL (or your chosen database)
- **Frontend:** (mention the frontend technology you are using, e.g., React, Angular, etc. – if applicable)
- **Version Control:** Git

## Installation
To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/anandtiwari11/Company-Management-System.git
   cd Company-Management-System
   
2. Set up virtual evironment
   python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3.Install the required packages:
  pip install -r requirements.txt
  
4. Set up the databases
  Update the database settings in settings.py.
  Run the migrations: python manage.py migrate

5. Start the development server:
   python manage.py runserver

USAGE:
Creating a Company: (provide endpoint details)
Deleting a Company: (provide endpoint details)
Creating an Employee: (provide endpoint details)
Updating an Employee: (provide endpoint details)
Deleting an Employee: (provide endpoint details)

Future Work:
Implement user authentication and authorization
Host the backend API
Integrate the frontend with the backend
Add more features based on user feedback

Contributing:
Contributions are welcome! Please create a new issue or submit a pull request for any enhancements or bug fixes.
