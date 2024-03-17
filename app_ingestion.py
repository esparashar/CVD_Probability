from src.logger import logging
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion
from src.components.data_ingestion import DataIngestionConfig
from src.components.data_transformation import DataTransformationConfig,DataTransformation
from src.components.model_tranier import ModelTrainerConfig,ModelTrainer

import sys


if __name__=="__main__":
    logging.info("The execution has started")

    try:
        #data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        #data_ingestion.initiate_data_ingestion()
        
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()

               
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)