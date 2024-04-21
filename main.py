
from uwsoundspeed.logging import logger
from uwsoundspeed.pipeline.stage_01_data_ingestion import DataIngestionPipeline
# from uwsoundspeed.pipeline.stage_02_data_preprocessing import DataPreprocessorPipeline
from uwsoundspeed.pipeline.stage_03_knn_model_train import  KNNModelTrainPipeline
from uwsoundspeed.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH 

# # Ensure these paths are correctly defined
# CONFIG_FILE_PATH = 'path/to/your/config.yaml' 
# PARAMS_FILE_PATH = 'path/to/your/params.yaml'

if __name__ == '__main__':

    try:
        # Data Ingestion Stage
        STAGE_NAME = "Data Ingestion stage"
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        data_ingestion_obj = DataIngestionPipeline()
        data_ingestion_obj.main()  # Assuming this method orchestrates the data ingestion stage
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

        # Data Preprocessing Stage
        # STAGE_NAME = "Data Preprocessing stage"
        # logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        # data_preprocessing_obj = DataPreprocessorPipeline()
        # data_preprocessing_obj.main()  # Assuming this method orchestrates the data ingestion stage
        # logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

        # KNN Model Training Stage
        STAGE_NAME = "KNN Model Train"
        logger.info("*******************")
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        knn_model_obj = KNNModelTrainPipeline()
        knn_model_obj.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

    except Exception as e:
        logger.exception(e)
        raise e
