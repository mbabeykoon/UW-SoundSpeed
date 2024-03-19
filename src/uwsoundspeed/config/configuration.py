from box.exceptions import BoxValueError
from uwsoundspeed.constants import *
from uwsoundspeed.utils.common import read_yaml, create_directories
from uwsoundspeed.entity.config_entity import (DataIngestionConfig,DataPreprocessingConfig)

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])


    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config

    def get_data_preprocessing_config(self) -> DataPreprocessingConfig:
        config = self.config['data_preprocessing']
        params = self.params['preprocessing']

        create_directories([Path(config['root_dir'])])

        data_preprocessing_config = DataPreprocessingConfig(
            root_dir=Path(config['root_dir']),
            data_path=Path(config['data_path']),
            numerical_features=params['numerical_features'],
            # numerical_transformer=params['numerical_transformer'],
            categorical_features=params['categorical_features'],
            # categorical_transformer=params['categorical_transformer'],
            pca_n_components=params['pca_n_components']
        )

        return data_preprocessing_config