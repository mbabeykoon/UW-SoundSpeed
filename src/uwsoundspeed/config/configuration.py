from box.exceptions import BoxValueError
from uwsoundspeed.constants import *
from uwsoundspeed.utils.common import read_yaml, create_directories
from uwsoundspeed.entity.config_entity import (DataIngestionConfig,PrepareBaseModelConfig,PreprocessingConfig,PCAConfig,ModelConfig,GridSearchConfig,TrainTestSplitConfig) #Dat
from uwsoundspeed.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from uwsoundspeed.utils.common import read_yaml, create_directories


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
    


    def get_preprocessing_config(self) -> PreprocessingConfig:
        config = self.params.preprocessing 
        return PreprocessingConfig(
            numerical_features=config.numerical_features,
            numerical_transformer=config.numerical_transformer,
            categorical_features=config.categorical_features,
            categorical_transformer=config.categorical_transformer

           
        )
    
    
    def get_pca_config(self) -> PCAConfig:
        pca= self.params.preprocessing
        return PCAConfig(n_components=pca.pca_n_components)

    def get_model_config(self) -> ModelConfig:
        model = self.params.model
        return ModelConfig(KNeighborsRegressor=model['KNeighborsRegressor'])

    def get_grid_search_config(self) -> GridSearchConfig:
        grid_search = self.params.grid_search
        return GridSearchConfig(cv=grid_search['cv'], scoring=grid_search['scoring'])

    def get_train_test_split_config(self) -> TrainTestSplitConfig:
        split_config = self.params.train_test_split
        return TrainTestSplitConfig(test_size=split_config['test_size'], random_state=split_config['random_state'])
    

    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
    # Assuming 'prepare_knn_model' contains all necessary configuration paths and settings
        config = self.config['prepare_knn_model']
        
        # Create necessary directories specified in the configuration
        create_directories([Path(config['root_dir'])])

        # Construct and return the PrepareBaseModelConfig object with appropriate paths and settings
        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(config['root_dir']),
            data_file_path=Path(config['data_file_path']),
            preprocessing=self.get_preprocessing_config(),
            pca=self.get_pca_config(),
            model=self.get_model_config(),
            grid_search=self.get_grid_search_config(),
            train_test_split=self.get_train_test_split_config(),
            knn_model_path=Path(config['knn_model_path'])
        )

        return prepare_base_model_config
    

    

