from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError
import os
from datetime import datetime

# Load environment variables
load_dotenv()

# Get credentials from .env file
MONGO_USER = os.environ.get("MONGO_USER")
MONGO_PASSWORD = os.environ.get("MONGO_PASSWORD")
MONGO_CLUSTER_URL = os.environ.get("MONGO_CLUSTER_URL")  # Fixed typo

# Construct the full connection string
# Option 1: If MONGO_CLUSTER_URL doesn't include credentials
connection_string = f"mongodb+srv://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_CLUSTER_URL}"

# Option 2: If MONGO_CLUSTER_URL is the complete connection string
# connection_string = MONGO_CLUSTER_URL

try:
    # Create client with timeout settings
    client = MongoClient(
        connection_string,
        serverSelectionTimeoutMS=5000,
        connectTimeoutMS=10000
    )

    # Verify connection
    client.admin.command('ping')
    print("✅ Successfully connected to MongoDB Atlas!")

    # Access database and collection
    db = client["water_quality_data"]
    robot1 = db["robot1"]

    # Insert one observation with timestamp
    obs1 = {
        "temp": 92,
        "salinity": 35,
        "pH": 6.5,
        "oxygen": 7.2,
        "notes": "good",
        "timestamp": datetime.now()  # Add timestamp for tracking
    }

    result1 = robot1.insert_one(obs1)
    print(f"✅ Inserted document with ID: {result1.inserted_id}")

    # Insert multiple observations
    listObs = [
        {"temp": 28, "salinity": 35, "pH": 6.5, "oxygen": 7.2, "notes": "good", "timestamp": datetime.now()},
        {"temp": 30, "salinity": 34, "pH": 6.8, "oxygen": 7.5, "notes": "excellent", "timestamp": datetime.now()},
        {"temp": 29, "salinity": 36, "pH": 6.3, "oxygen": 6.9, "notes": "fair", "timestamp": datetime.now()}
    ]

    result2 = robot1.insert_many(listObs)
    print(f"✅ Inserted {len(result2.inserted_ids)} documents")

    # Query operations
    print("\n📊 QUERY RESULTS:")
    print("-" * 40)

    # Find first document
    doc = robot1.find_one()
    print("First document:", doc)

    # Find hot water (temp > 28)
    print("\n🌡️ Hot water readings (temp > 28):")
    for obs in robot1.find({"temp": {"$gt": 28}}):
        print(f"  - Temp: {obs['temp']}°, pH: {obs['pH']}, Notes: {obs['notes']}")

    # Additional useful queries
    print("\n📈 Statistics:")
    print(f"Total documents: {robot1.count_documents({})}")
    print(
        f"Average temperature: {robot1.aggregate([{'$group': {'_id': None, 'avg_temp': {'$avg': '$temp'}}}]).next()['avg_temp']:.2f}°")

except ConnectionFailure as e:
    print(f"❌ Failed to connect to MongoDB: {e}")
    print("\nTroubleshooting:")
    print("1. Check your .env file has correct credentials")
    print("2. Verify your IP is whitelisted in Atlas")
    print("3. Ensure cluster is running")

except ServerSelectionTimeoutError as e:
    print(f"❌ Connection timeout: {e}")
    print("\nPossible issues:")
    print("1. Network connectivity problems")
    print("2. Incorrect cluster URL")
    print("3. Firewall blocking connection")

except Exception as e:
    print(f"❌ An error occurred: {e}")

finally:
    # Always close the connection
    if 'client' in locals():
        client.close()
        print("\n🔒 Connection closed")
