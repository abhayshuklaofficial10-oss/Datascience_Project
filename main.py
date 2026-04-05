from src.DataScience_Project import logger
from src.DataScience_Project.pipeline.data_ingestion import DataIngestionTrainingPipeline
from src.DataScience_Project.pipeline.data_validation import DataValidationTrainingPipeline
from src.DataScience_Project.pipeline.data_transfromation import DataTransformationTrainingPipeline


STAGE_NAME="Data Ingestion Stage"
try:
        logger.info(f'>>>>>> stage {STAGE_NAME} started <<<<<<') 
        obj= DataIngestionTrainingPipeline()
        obj.initiate_data_ingestion()
        logger.info(f'>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x') 
except Exception as e:
        logger.exception(e)
        raise e  

STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataValidationTrainingPipeline()
   data_ingestion.initiate_data_validation()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Data Transformation stage"
try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
        data_transformation = DataTransformationTrainingPipeline()
        data_transformation.initiate_data_transformation()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")    
except Exception as e:
        logger.exception(e)
        raise e
