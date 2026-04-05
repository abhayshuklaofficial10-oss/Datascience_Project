from src.DataScience_Project.config.configuration import ConfigurationManager
from src.DataScience_Project.components.data_transformation import DataTransformation
from src.DataScience_Project import logger
from pathlib import Path

STAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]   # FIXED: removed quotes

            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_spliting()
            else:
                raise Exception("Data validation failed. Cannot proceed with data transformation.")

        except Exception as e:   # FIXED: indentation corrected
            logger.error(f"Error occurred while reading status file: {e}")
            raise e