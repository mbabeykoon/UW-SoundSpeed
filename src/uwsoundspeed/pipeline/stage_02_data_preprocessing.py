from uwsoundspeed.config.configuration import ConfigurationManager
from uwsoundspeed.components.data_preprocessing import DataPreprocessor
from uwsoundspeed.logging import logger





class DataPreprocessorPipeline:
    def __init__(self):
        pass

    def main(self):
   
        config = ConfigurationManager()
        data_preprocessing_config = config.get_data_preprocessing_config()
        data_preprocessor = DataPreprocessor(config=data_preprocessing_config)
        
        # Preprocess the data and apply PCA
        # This method now internally reads the data, applies transformations, and PCA
        X_pca = data_preprocessor.preprocess_and_apply_pca()

        # Save the fitted preprocessor and PCA model for later use
        data_preprocessor.save(subdir_name="preprocessor")

        return X_pca

