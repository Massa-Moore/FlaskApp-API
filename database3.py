from dotenv import load_dotenv
from pymongo import MongoClient
import certifi
import os
import pandas as pd

df = pd.read_csv("data/BB_WQ.csv")

for _, row in df.iterrows():
    robot1.insert_one(row.to_dict())

print("CSV data inserted into MongoDB")
load_dotenv()

MONGO_USER = os.environ.get("MONGO_USER")
MONGO_PASSWORD = os.environ.get("MONGO_PASSWORD")
MONGO_CLUSTSTER_URL = os.environ.get("MONGO_CLUSTSTER_URL")

client = MongoClient(
    MONGO_CLUSTSTER_URL,
    tls=True,
    tlsCAFile=certifi.where()
)

print("Connected client created")

client.admin.command("ping")
print("Ping successful")

db = client["water_quality_data"]
robot1 = db["robot1"]

obs1 = {
    "temp": 92,
    "salinity": 35,
    "pH": 6.5,
    "oxygen": 7.2,
    "notes": "good"
}

result1 = robot1.insert_one(obs1)
print("Inserted one:", result1.inserted_id)

doc = robot1.find_one()
print("First document:", doc)