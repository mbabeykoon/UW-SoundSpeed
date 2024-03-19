# # from uwsoundspeed.config.configuration import ConfigurationManager
# # from uwsoundspeed.components.prepare_base_model import PrepareBaseModel
# # from uwsoundspeed import logger

# # STAGE_NAME = "knn model train"

# # class KNNModelTrain:
# #     def __init__(self):
# #         pass
# #     def main(self):
# #         config_manager = ConfigurationManager(config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH)  # Ensure CONFIG_FILE_PATH and PARAMS_FILE_PATH are correctly defined
# #         prepare_data = KnnModelTrain(config_manager)  # Passing config_manager correctly

# #         prepare_data.load_data()
# #         prepare_data.prepare_pipeline()
# #         prepare_data.train_test_split()
# #         prepare_data.train_and_evaluate()
# #         prepare_data.save_model()

# #     if __name__ == '__main__':
# #         try:
# #             logger.info(f"*******************")
# #             logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
# #             obj = PrepareBaseModelTrainingPipeline()
# #             obj.main()
# #             logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
# #         except Exception as e:
# #             logger.exception(e)
# #             raise e
# from uwsoundspeed.config.configuration import ConfigurationManager
# from uwsoundspeed.components.knn_model_train import KnnModelTrain
# from uwsoundspeed.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH

# # from uwsoundspeed.components.knn_model_train import PrepareBaseModel  # Ensure this import is correct
# from uwsoundspeed import logger

# STAGE_NAME = "knn model train"

# class KNNModelTrain:
#     def __init__(self, config_manager):
#         self.config_manager = config_manager  # Store the configuration manager
#         # Assuming PrepareBaseModel is the correct class you intend to use for operations
#         # self.prepare_base_model = KnnModelTrain(config_manager.get_prepare_base_model_config())
#         # knn_model_train = KnnModelTrain(config_manager)
#         prepare_data = KnnModelTrain(config_manager)
    
#     def load_data(self):
#         self.prepare_data.load_data()
    
#     def prepare_pipeline(self):
#         self.prepare_data.prepare_pipeline()
    
#     def train_test_split(self):
#         self.prepare_data.train_test_split()
    
#     def train_and_evaluate(self):
#         self.prepare_data.train_and_evaluate()
    
#     def save_model(self):
#         self.prepare_data.save_model()  # Ensure you have this method in PrepareBaseModel

# if __name__ == '__main__':
#     try:
#         logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
#         config_manager = ConfigurationManager(config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH)  # Ensure these paths are defined
#         knn_model_train = KNNModelTrain(config_manager)

#         knn_model_train.load_data()
#         knn_model_train.prepare_pipeline()
#         knn_model_train.train_test_split()
#         knn_model_train.train_and_evaluate()
#         knn_model_train.save_model()

#         logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
#     except Exception as e:
#         logger.exception(e)
#         raise e

# # def main():
# #     try:
# #         logger.info("*******************")
# #         logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        
# #         config_manager = ConfigurationManager(config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH)  # Ensure these paths are defined
# #         knn_model_train = KNNModelTrain(config_manager)

# #         knn_model_train.load_data()
# #         knn_model_train.prepare_pipeline()
# #         knn_model_train.train_test_split()
# #         knn_model_train.train_and_evaluate()
# #         knn_model_train.save_model()

# #         logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
# #     except Exception as e:
# #         logger.exception(f"Failed during stage {STAGE_NAME} due to: {e}")
# #         raise e

# # if __name__ == '__main__':
# #     main()
from uwsoundspeed.config.configuration import ConfigurationManager
from uwsoundspeed.components.knn_model_train import KnnModelTrain  # Corrected import
from uwsoundspeed.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from uwsoundspeed import logger

from uwsoundspeed.utils.common import get_size, load_from_pkl
from uwsoundspeed.entity.config_entity import (DataIngestionConfig,PrepareBaseModelConfig,PreprocessingConfig)

STAGE_NAME = "KNN Model Train"

if __name__ == '__main__':
    try:
        logger.info("*******************")
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        config_manager = ConfigurationManager(config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH)
        
        # Directly use KnnModelTrain for all operations
        knn_model_train = KnnModelTrain(config_manager)
        
        knn_model_train.load_data()
        knn_model_train.prepare_pipeline()
        knn_model_train.train_test_split()
        knn_model_train.train_and_evaluate()
        knn_model_train.save_model()

        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
