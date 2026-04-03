from src.DataScience_Project import logger
from src.DataScience_Project.pipeline.data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME="Data Ingestion Stage"


try:
        logger.info(f'>>>>>> stage {STAGE_NAME} started <<<<<<') 
        obj= DataIngestionTrainingPipeline()
        obj.initiate_data_ingestion()
        logger.info(f'>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x') 
except Exception as e:
        logger.exception(e)
        raise e  
