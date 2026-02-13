from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()

MONGO_USER = os.environ.get("MONGO_USER")
MONGO_PASSWORD = os.environ.get("MONGO_PASSWORD")
MONGO_CLUSTSTER_URL = os.environ.get("MONGO_CLUSTSTER_URL")