# from uwsoundspeed import logger
# from uwsoundspeed.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
# from uwsoundspeed.pipeline.stage_02_knn_model_train import ConfigurationManager

# STAGE_NAME = "Data Ingestion stage"
# if __name__ == '__main__':
#     try:
#         logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
#         obj = DataIngestionTrainingPipeline()
#         obj.main()
#         logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
#     except Exception as e:
#         logger.exception(e)
#         raise e
    

# STAGE_NAME = "knn model train"
# try:
#     logger.info("*******************")
#     logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    
#     config_manager = ConfigurationManager(config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH)  # Ensure these paths are defined
#     knn_model_train = KNNModelTrain(config_manager)

#     knn_model_train.load_data()
#     knn_model_train.prepare_pipeline()
#     knn_model_train.train_test_split()
#     knn_model_train.train_and_evaluate()
#     knn_model_train.save_model()

#     logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
# except Exception as e:
#     logger.exce
from uwsoundspeed import logger
from uwsoundspeed.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from uwsoundspeed.pipeline.stage_02_knn_model_train import  ConfigurationManager 
from uwsoundspeed.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH # Assuming KNNModelTrain is in the same module

# # Ensure these paths are correctly defined
# CONFIG_FILE_PATH = 'path/to/your/config.yaml' 
# PARAMS_FILE_PATH = 'path/to/your/params.yaml'

if __name__ == '__main__':
    try:
        # Data Ingestion Stage
        STAGE_NAME = "Data Ingestion stage"
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        data_ingestion_obj = DataIngestionTrainingPipeline()
        data_ingestion_obj.main()  # Assuming this method orchestrates the data ingestion stage
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

        # KNN Model Training Stage
        STAGE_NAME = "KNN Model Train"
        logger.info("*******************")
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        config_manager = ConfigurationManager(config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH)
        knn_model_train = KNNModelTrainPipeline(config_manager)
        knn_model_train.load_data()
        knn_model_train.prepare_pipeline()
        knn_model_train.train_test_split()
        knn_model_train.train_and_evaluate()
        knn_model_train.save_model()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

    except Exception as e:
        logger.exception(e)
        raise e
