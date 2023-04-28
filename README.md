# Dreamhome
# DreamHome Rental Project
DreamHome Rental Project is a database management system built using MySQL database for storing rental property data, Django as the backend for handling data and authentication, and React as the frontend for user interaction. The project is designed to provide a user-friendly interface for landlords and tenants to manage rental properties.

## Installation
## Prerequisites
Node.js
Python 3
MySQL
## Backend Installation
Clone the repository to your local machine.
Navigate to the backend directory cd backend.
Create a virtual environment python3 -m venv env and activate it source env/bin/activate.
Install the required packages pip install -r requirements.txt.
Create a MySQL database and update the database settings in backend/dreamhome/settings.py.
Run the migrations python manage.py migrate.
Create a superuser python manage.py createsuperuser.
Start the server python manage.py runserver.
## Frontend Installation
Navigate to the frontend directory cd frontend.
Install the required packages npm install.
Start the server npm start.
## Usage
Backend
Login with your superuser account at http://localhost:8000/admin/.
Add rental properties, tenants, landlords, and other related data from the Django admin dashboard.
Authenticate users and authorize access to data from the backend API.
## Frontend
Navigate to http://localhost:3000/ to view the React frontend.
Login with your superuser account or a tenant account.
View rental properties and details.
Submit rental applications and requests.
Contact landlords for further information.
## Contributing
Contributions are welcome! Please submit a pull request for any improvements or bug fixes.
