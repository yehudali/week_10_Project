# week_10_Project
Week 10 Project: Contact Manager API with Docker Compose

# week_10_Project
Week 10 Project: Contact Manager API with Docker Compose


Project Overview:
is Contact Manager API - a REST API service that allows users to manage a contact list. The application will do the following: - - - -
Store contacts in a MySQL database
Provide HTTP endpoints for CRUD (create, read, update, delete) operations
Run in Docker containers using Docker Compose
Persist data using Docker storage
Technology Stack: - - - -
Python 3.11+
FastAPI (web framework)
MySQL 8.0 (database)
Docker and Docker Compose


the endpoint:
get /contacts  -> Get all contacts 
POST /contacts  -> Create new contact 
PUT /contacts/{id}  -> Update existing contact 
DELETE /contacts/{id}  -> Delete contact 


Installation instructions:
PULL the project to your local computer
Create a .env file in the main project folder and set it:
DB_NAME=contacts_db
DB_PASSWORD=your_password
DB_USER=root
DB_HOST=db

In the project folder, run in the terminal: docker compose up -d
The server will be available at:http://localhost:8000
Run tests at: http://localhost:8000/docs
