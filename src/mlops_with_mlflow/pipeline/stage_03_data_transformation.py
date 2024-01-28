from src.mlops_with_mlflow.config.configuration import ConfigurationManager
from src.mlops_with_mlflow.components.data_transformation import DataTranformation
from src.mlops_with_mlflow import logger
from pathlib import Path

STAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]
                
            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTranformation(config=data_transformation_config)
                data_transformation.train_test_splitting()
                
            else:
                raise Exception("Provided data schema is not valid")
            
        except Exception as e:
            print(e)
            
if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<\n\nx===============================x")
    except Exception as e:
        logger.exception(e)
        raise e