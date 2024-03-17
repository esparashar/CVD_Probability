from src.logger import logging
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion
from src.components.data_ingestion import DataIngestionConfig
from src.components.data_transformation import DataTransformationConfig,DataTransformation
from src.components.model_tranier import ModelTrainerConfig,ModelTrainer

import sys


if __name__=="__main__":
    logging.info("The execution has started")

    #data_ingestion_config=DataIngestionConfig()
    data_ingestion=DataIngestion()
    train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()
        
    data_transformation=DataTransformation()
    data_transformation.initiate_data_transormation(train_data_path,test_data_path)
        

               
  