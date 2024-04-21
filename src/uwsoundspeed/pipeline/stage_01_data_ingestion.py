from uwsoundspeed.config.configuration import ConfigurationManager
from uwsoundspeed.components.data_ingestion import DataIngestion
from uwsoundspeed.logging import logger



class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.handle_local_data()
        data_ingestion.extract_zip_file()

if __name__ == '__main__':
    try:
        # Data Ingestion Stage
        STAGE_NAME = "Data Ingestion stage"
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        data_ingestion_obj = DataIngestionPipeline()
        data_ingestion_obj.main()  # Assuming this method orchestrates the data ingestion stage
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

    except Exception as e:
        logger.exception(e)
        raise e