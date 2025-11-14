import sys

from US_VISA.exception import USvisaException
from US_VISA.logger import logging

import os
from US_VISA.constants import DATABASE_NAME, MONGODB_URL_KEY
import pymongo
import certifi

import urllib.parse

username = "venki"
password = "vishwa"

encoded_username = urllib.parse.quote_plus(username)
encoded_password = urllib.parse.quote_plus(password)


ca = certifi.where()

class MongoDBClient:
    """
    Class Name :   export_data_into_feature_store
    Description :   This method exports the dataframe from mongodb feature store as dataframe 
    
    Output      :   connection to mongodb database
    On Failure  :   raises an exception
    """
    client = None

    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = f"mongodb+srv://{encoded_username}:{encoded_password}@cluster0.egtkrm9.mongodb.net/?appName=Cluster0"
                if mongo_db_url is None:
                    raise Exception(f"Environment key: {MONGODB_URL_KEY} is not set.")
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info("MongoDB connection succesfull")
        except Exception as e:
            raise USvisaException(e,sys)