from flask import Flask, jsonify
from dotenv import load_dotenv
from pymongo import MongoClient
import certifi
import os

load_dotenv()

app = Flask(__name__)

MONGO_CLUSTSTER_URL = os.environ.get("MONGO_CLUSTSTER_URL")

client = MongoClient(
    MONGO_CLUSTSTER_URL,
    tls=True,
    tlsCAFile=certifi.where()
)

db = client["water_quality_data"]
robot1 = db["robot1"]


@app.route("/")
def home():
    return "MongoDB Atlas + Flask is working!"


@app.route("/robot1")
def robot_data():

    docs = []

    for doc in robot1.find():
        doc["_id"] = str(doc["_id"])
        docs.append(doc)

    return jsonify(docs)


if __name__ == "__main__":
    app.run(debug=True)