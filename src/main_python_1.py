import logging
import inspect
from parse_txt_data import parse_data
from log_setup import setup_logging

# Setting up the logger
logger = logging.getLogger(__name__)

# Relative paths for data and log file
log_filename = "Arkadii_Assignment_HT\\logs\\log.txt"
data_file = "Arkadii_Assignment_HT\\data\\dataset.txt"
# D:\0_tech\1_ARK_DS\heatTransformers_assignment\Arkadii_Assignment_HT\data\dataset.txt


def main():
    """
    Main ETL pipeline function.
    :return: None
    """
    function_name = inspect.currentframe().f_code.co_name
    logger.info(f"Main ETL pipeline -> {function_name}")

    # Setup logging for each run
    setup_logging(log_filename)

    try:
        all_warehouses = parse_data(data_file)
        print(all_warehouses)

        print("Main -> ETL executed")
        logger.info("Main -> ETL executed")

    except Exception as e:
        print(f"Main Error -> {e}")
        logger.error(f"Main Error -> {e}")


if __name__ == '__main__':
    main()
