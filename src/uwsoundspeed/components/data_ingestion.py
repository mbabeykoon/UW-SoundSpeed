import os
import shutil
import urllib.request as request
import zipfile
from uwsoundspeed import logger
from uwsoundspeed.utils.common import get_size
from pathlib import Path
from uwsoundspeed.entity.config_entity import DataIngestionConfig



class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def handle_local_data(self):    
        if not os.path.exists(self.config.local_data_file):
            shutil.copy(self.config.source_URL, self.config.local_data_file)  # Assuming source_URL is the path to the local file
            logger.info(f"File copied to: {self.config.local_data_file}")
        else:
            logger.info(f"File already exists at destination: {self.config.local_data_file} of size: {get_size(Path(self.config.local_data_file))}")



    # #for data download from internet    # def download_file(self):
    #     if not os.path.exists(self.config.local_data_file):
    #         filename, headers = request.urlretrieve(
    #             url = self.config.source_URL,
    #             filename = self.config.local_data_file
    #         )
    #         logger.info(f"{filename} download! with following info: \n{headers}")
    #     else:
    #         logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")  


    
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)