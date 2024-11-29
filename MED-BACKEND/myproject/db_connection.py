from pymongo import MongoClient
from django.conf import settings

# Initialize MongoDB connection using the URI from settings
client = MongoClient(settings.MONGODB_URI)
db = client[settings.MONGODB_DB_NAME]
