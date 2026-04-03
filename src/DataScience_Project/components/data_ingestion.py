import os
import urllib.request as request
from src.DataScience_Project import logger
import zipfile
from src.DataScience_Project.entity.config_entity import (DataIngestionConfig)

class DataIngestion:

    def __init__(self, config):
        self.config = config

    # downloading the zip file
    def download_file(self):

        if not os.path.exists(self.config.local_data_file):

            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )

            logger.info(
                f"{filename} downloaded with following info: \n{headers}"
            )

        else:
            logger.info("File already exists")

    # extract the zip file
    def extract_zip_file(self):

        """
        Extract the zip file into the data directory
        """

        unzip_path = self.config.unzip_dir

        os.makedirs(unzip_path, exist_ok=True)

        with zipfile.ZipFile(
            self.config.local_data_file,
            'r'
        ) as zip_ref:

            zip_ref.extractall(unzip_path)