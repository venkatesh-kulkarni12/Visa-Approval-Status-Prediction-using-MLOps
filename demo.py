# from US_VISA.logger import logging
# from US_VISA.exception import USvisaException
# import sys


# logging.info("Welcome to Our Major-Project")
# logging.info("Zero Handling exception")


# try:
    # a = 2/0
# except Exception as e:
#     raise USvisaException(e, sys)


# import os
# mongo_db_url = os.getenv("MONGODB_URL")
# print(mongo_db_url)


from US_VISA.pipline.training_pipeline import TrainPipeline

obj = TrainPipeline()

obj.run_pipeline()