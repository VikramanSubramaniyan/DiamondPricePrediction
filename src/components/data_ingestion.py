import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from src.exception import CustomException
from src.logging import logging
from dataclasses import dataclass

@dataclass

class DataIngestionConfig():
    raw_data_path:str = os.path.join('artifacts','raw.csv')
    train_data_path:str = os.path.join('artifacts','train.csv')
    test_data_path:str = os.path.join('artifacts','test.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    def intiate_data_ingestion(self):
        logging.info("Data Ingestion Started")
        try:
            df=pd.read_csv(os.path.join('notebook/data/','gemstone.csv'))
            logging.info('Dataset read as pandas Dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info('Train test split')

            train_set,test_set = train_test_split(df,test_size=0.30,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False)

            logging.info('Train test split completed')
            logging.info('Data Ingestion Process Completed')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
                )
        except Exception as e:
            logging.info('Exception occured at Data Ingestion stage')
            raise CustomException(e,sys)