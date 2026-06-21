import os
from pathlib import Path
from dotenv import load_dotenv
import pandas as pd
from pymongo import MongoClient

load_dotenv(Path(__file__).parent.parent / ".env")

# Connect directly to the already-running tunnel
from urllib.parse import quote_plus
user = os.getenv("MONGO_USER")
password = quote_plus(os.getenv("MONGO_PASSWORD"))
auth_db = os.getenv("MONGO_DB")
mongo_client = MongoClient(f"mongodb://{user}:{password}@localhost:27017/{auth_db}")

db = mongo_client[os.getenv("MONGO_DB")]
collection = db[os.getenv("MONGO_COLLECTION")]

records = list(
    collection.find(
        {"datetime": {"$gte": "2025-07-17T00:00:00Z", "$lt": "2025-07-18T00:00:00Z"}},
        {"_id": 0},
    )
)
df = pd.DataFrame(records)

print(df.dtypes)
print(df.head(3))

mongo_client.close()
