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



    # in case if data need to download from url
    # def download_file(self):
    #     try:
    #         if not self.config.local_data_file.exists():
    #             filename, headers = request.urlretrieve(
    #                 url=self.config.source_URL,
    #                 filename=str(self.config.local_data_file)
    #             )
    #             logger.info(f"{filename} downloaded with following info: \n{headers}")
    #         else:
    #             logger.info(f"File already exists at: {self.config.local_data_file}")
    #     except Exception as e:
    #         logger.error(f"Failed to download file due to {e}")
    #         raise 


    
    def extract_zip_file(self):
        try:
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(self.config.unzip_dir)
            logger.info(f"Extracted zip file to {self.config.unzip_dir}")
        except Exception as e:
            logger.error(f"Failed to extract zip file due to {e}")
            raise