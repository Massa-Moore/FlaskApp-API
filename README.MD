Flask MongoDB Atlas Water Quality API

This project demonstrates the development and consumption of a REST API using Flask connected to a MongoDB Atlas cloud database.

The project includes:

A Flask web application demonstrating static and dynamic routing.

A RESTful API that provides water quality sensor data in JSON format.

Integration with MongoDB Atlas for storing and retrieving environmental sensor readings.

👋 About Me

Hi, I’m Massa Moore — a Computer Science student and Air National Guard avionics technician transitioning into IT and cybersecurity. I’m focused on building practical software, networking, and backend development skills while strengthening my understanding of system architecture, APIs, and cloud-connected applications.

🔗 GitHub: https://github.com/Massa-Moore

📌 Project Overview

FlaskApp-API is a backend web application built using Python and Flask that demonstrates RESTful API development and integration with a MongoDB Atlas cloud database.

This project includes:
• A Flask-based REST API
• MongoDB Atlas cloud database integration
• JSON data handling and API responses
• Python scripts for database operations and testing

The application simulates a water quality monitoring system, storing environmental sensor readings and returning them through API routes.

🚀 Features

• Health check endpoint (/)
• Retrieve all water quality records (/robot1)
• MongoDB Atlas cloud database integration
• JSON responses with formatted output
• Secure database credentials using .env variables
• Cloud-based data storage and retrieval

🧠 How It Works

The Flask application runs a local server.

The API connects securely to MongoDB Atlas using PyMongo.

Sensor data is inserted into a MongoDB collection.

Flask API routes query the database.

The API returns JSON responses that can be viewed in the browser or consumed by other applications.

This demonstrates real-world backend fundamentals including database integration, REST API design, and client-server communication.

🛠 Technologies Used

• Python
• Flask
• MongoDB Atlas
• PyMongo
• python-dotenv
• certifi
• JSON
• Git & GitHub

📁 Project Structure

Flask-App/
│
├── FlaskApp3.py # Flask API application
├── database3.py # MongoDB connection & testing script
├── .env # Environment variables (not committed)
├── requirements.txt # Project dependencies
└── README.md # Project documentation

▶️ How to Run the Project Locally
1️⃣ Clone the Repository
git clone https://github.com/Massa-Moore/FlaskApp-API.git
cd FlaskApp-API
2️⃣ Create & Activate Virtual Environment
python -m venv .venv
source .venv/bin/activate    # macOS/Linux
.venv\Scripts\activate       # Windows
3️⃣ Install Dependencies
pip install flask pymongo python-dotenv certifi
4️⃣ Configure Environment Variables

Create a .env file in the project root:

MONGO_CLUSTSTER_URL=your_mongodb_atlas_connection_string
5️⃣ Run the Flask API
python FlaskApp3.py

The API will start at:

http://127.0.0.1:5000
📡 Available API Endpoints
Method	Endpoint	Description
GET	/	API health check
GET	/robot1	Retrieve all water quality records
🎯 Learning Outcomes

This project strengthened my understanding of:

• REST API architecture
• Backend routing with Flask
• Cloud database integration (MongoDB Atlas)
• Environment variable security practices
• JSON serialization and API responses
• Building backend services using Python