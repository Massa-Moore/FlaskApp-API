from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()

MONGO_USER = os.environ.get("MONGO_USER")
MONGO_PASSWORD = os.environ.get("MONGO_PASSWORD")
MONGO_CLUSTSTER_URL = os.environ.get("MONGO_CLUSTSTER_URL")






client = MongoClient(MONGO_CLUSTSTER_URL)
print(client)

db = client["water_quality_data"]
robot1 = db["robot1"]

obs1 = {"temp": 92,
        "salinity": 35,
        "pH": 6.5,
        "oxygen": 7.2,
        "notes":"good"}
result1 = robot1.insert_one(obs1)

listObs = [{"temp": 92, "salinity": 35,"pH": 6.5,"oxygen": 7.2,"notes":"good"},
           {"temp": 92, "salinity": 35,"pH": 6.5,"oxygen": 7.2,"notes":"good"},
           {"temp": 92, "salinity": 35,"pH": 6.5,"oxygen": 7.2,"notes":"good"}]

result2 = robot1.insert_many(listObs)

# Other methods:

doc = robot1.find_one()
for obs in robot1.find({"temp": {"$gt":28}}):
print("Hot water", obs)