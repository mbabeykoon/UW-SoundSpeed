from uwsoundspeed.config.configuration import ConfigurationManager
from uwsoundspeed.components.knn_model_train import KnnModelTrain
from uwsoundspeed.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from uwsoundspeed import logger

STAGE_NAME = "knn model train"

class KNNModelTrainPipeline:
    def __init__(self):
        pass
    def main(self):
        config_manager = ConfigurationManager(config_filepath=CONFIG_FILE_PATH, params_filepath=PARAMS_FILE_PATH)
        
        # Directly use KnnModelTrain for all operations
        knn_model_train = KnnModelTrain(config_manager)

        
        
        knn_model_train.load_data()
        knn_model_train.prepare_pipeline()
        knn_model_train.train_test_split()
        knn_model_train.train_and_evaluate()
        knn_model_train.save_model()

if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = KNNModelTrainPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e