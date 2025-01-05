from pymongo import MongoClient
from datetime import datetime
import uuid
import os 
import os
from dotenv import load_dotenv

load_dotenv()




def save_to_db(trends, ip_address):
    # Connect to MongoDB
    client = MongoClient(os.getenv("MONGO_URI"))
    db = client.twitter_trends
    collection = db.trends

    # Create record
    record = {
        "_id": str(uuid.uuid4()),
        "nameoftrend1": trends[0],
        "nameoftrend2": trends[1],
        "nameoftrend3": trends[2],
        "nameoftrend4": trends[3],
        "date_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "ip_address": ip_address,
    }

    # Save to DB
    collection.insert_one(record)
    return record
