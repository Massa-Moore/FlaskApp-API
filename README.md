# FlaskApp-API
This project demonstrates the development and consumption of a REST API using Flask. The project includes: 1)A basic Flask web application demonstrating static and dynamic routing. 2)A RESTful API that provides campus data in JSON format. 3)A Python client script that sends HTTP requests to the API and processes responses.

👋 About Me

Hi, I’m Massa Moore — a Computer Science student and Air National Guard avionics technician transitioning into IT and cybersecurity. I’m focused on building practical software, networking, and backend development skills while strengthening my understanding of system architecture and API design.

🔗 GitHub: https://github.com/Massa-Moore

⸻

📌 Project Overview

FlaskApp-API is a backend web application built using Python and Flask that demonstrates RESTful API development and API consumption.

This project includes:
	•	A Flask-based REST API
	•	JSON data handling
	•	Proper HTTP status codes
	•	A Python client script that consumes the API

It simulates a campus information service and demonstrates how backend systems communicate using HTTP.

⸻

🚀 Features
	•	Health check endpoint (/api/health)
	•	Retrieve all campus records (/api/items)
	•	Retrieve a specific campus by ID (/api/items/<id>)
	•	JSON responses with status codes (200, 404)
	•	Basic error handling
	•	Separate client script for API testing

⸻

🧠 How It Works
	1.	The Flask application runs a local server on port 5001.
	2.	Campus data is stored in an in-memory list (simulating a database).
	3.	API routes process HTTP requests and return JSON responses.
	4.	The client.py script sends requests using the requests library.
	5.	The API responds with data or appropriate error messages.

This demonstrates real-world backend fundamentals including routing, request handling, and client-server communication.

⸻

🛠 Technologies Used
	•	Python
	•	Flask
	•	Requests
	•	JSON
	•	Git & GitHub

⸻

📁 Project Structure

FlaskApp-API/
│
├── app.py          # Flask API application
├── client.py       # Python script that consumes the API
├── requirements.txt
└── README.md


⸻

▶️ How to Run the Project Locally

1️⃣ Clone the Repository

git clone https://github.com/Massa-Moore/FlaskApp-API.git
cd FlaskApp-API


⸻

2️⃣ Create & Activate Virtual Environment

python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows


⸻

3️⃣ Install Dependencies

pip install -r requirements.txt


⸻

4️⃣ Run the API

python app.py

API runs at:

http://127.0.0.1:5001


⸻

5️⃣ Run the Client Script (New Terminal)

python client.py


⸻

📡 Available API Endpoints

Method	Endpoint	Description
GET	/api/health	API health check
GET	/api/items	Retrieve all campuses
GET	/api/items/<id>	Retrieve campus by ID


⸻

🎯 Learning Outcomes

This project strengthened my understanding of:
	•	REST API architecture
	•	Backend routing with Flask
	•	HTTP methods and status codes
	•	JSON serialization
	•	API integration using Python

