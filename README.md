User Management CRUD Application

📌 Project Overview

This is a full-stack CRUD application built with Flask (Python) for the backend, MongoDB Atlas for the database, and Vue.js 3 with PrimeVue for the frontend. The application allows users to be created, read, updated, and deleted. The data is imported from a JSON file into the MongoDB collection using a Python script.

🚀 Features

User Import Script: Reads a JSON file and inserts data into MongoDB.

Backend (Flask API): Exposes RESTful CRUD operations.

Frontend (Vue.js + PrimeVue): Displays users and provides an intuitive UI for managing them.

MongoDB Atlas: Cloud-hosted database for easy deployment.

🛠️ Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/JeffersonSilemen/deeper-systems-exam.git
cd deeper-systems-exam

2️⃣ Setup Backend (Flask API)

Install Dependencies

python3 -m venv venv  # Create a virtual environment
source venv/bin/activate  # (On Windows use: venv\Scripts\activate)
pip install -r requirements.txt  # Install required packages

Configure MongoDB Connection

Run the Flask Server

python3 backend/app.py

The API should be running at: http://127.0.0.1:5000

This will insert users into the MongoDB users collection.

3️⃣ Setup Frontend (Vue.js + PrimeVue)

Install Dependencies

cd frontend
npm install

Start the Vue Application

npm run dev

The frontend will be available at http://localhost:5173

🔥 Usage

View Users: The main page lists all users with options to edit or delete them.

Create a User: Click the Create button, fill in the form, and save.

Edit a User: Click the Edit button in the table or on the user page.

Delete a User: Click the Delete button (requires confirmation).

📌 API Endpoints

Method

Endpoint

Description

GET

/users

Get all users

POST

/users

Create a new user

GET

/users/:id

Get a single user by ID

PUT

/users/:id

Update a user

DELETE

/users/:id

Delete a user

📜 Folder Structure

backend: Contains the Flask application and related files.

app.py: Main entry point for the backend.
models.py: Defines data models using Python dataclasses.
routes.py: Implements API endpoints for CRUD operations.
parser.py: Script to import data from udata.json into MongoDB.
config.py: Configuration for MongoDB connection.
frontend: Contains the Vue.js application.

src/: Source code for the frontend.
components/: Vue components for dialogs, pages, and tables.
router.js: Defines application routes.
main.js: Entry point for the Vue application.
style.css: Global styles for the application.
constants: Contains the JSON file (udata.json) with user data to be imported.

requirements.txt: Lists Python dependencies for the backend.

README.md: Documentation for the project.

📌 Notes

Ensure MongoDB Atlas is set up before running the backend.

No .env file is required; the database URL is manually set in app.py.

The frontend and backend must run simultaneously for full functionality.

📬 Contact

For any issues or questions, feel free to create an issue or reach out. 🚀

