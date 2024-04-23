import logging
import inspect

from parse_txt_data import parse_data
from warehouse_processor.divided_by_3_rounded import *
from log_setup import setup_logging

logger = logging.getLogger(__name__)

log_filename = "WareHouse_Data_ETL\\logs\\log.txt"
data_file = "WareHouse_Data_ETL\\data\\dataset.txt"


def main(business_days, data_file):
    """
    Main ETL pipeline function.
    :return: None
    """
    function_name = inspect.currentframe().f_code.co_name
    logger.info(f"Main ETL pipeline -> {function_name}")

    setup_logging(log_filename)

    try:
        all_warehouses = parse_data(data_file)
        # print(f"Total warehouses -> {len(all_warehouses)}")

        for day in range(1, business_days + 1):
            logger.info(f"Processing All WareHouses during the {business_days} business days")
            for warehouse in all_warehouses:
                print(f"WareHouse Name -> {warehouse.name}")
                print(f"WareHouse Unit -> {warehouse.unit}")
                print(f"WareHouse Starting Products-> {warehouse.starting_products}")
                print(f"WareHouse Products total -> {len(warehouse.starting_products)}")
                print(f"WareHouse Formula text -> {warehouse.formula.formula_original_text}")
                print(f"WareHouse Test text -> {warehouse.test.test_formula_text}")

                for product in warehouse.starting_products:
                    print(f"Product Init Number -> {product.initial_number}")
                    print(f"Product LAST Number -> {product.last_number}")
                    processed_product = product
                    processed_product_number = product.last_number
                    print(type(processed_product))

                    shipping_location = warehouse.formula.calculate(product.initial_number)
                    print(f"{shipping_location} - 1st Shipping Location -> WareHouse Formula")

                    before_shipped = divided_by_3_rounded(shipping_location, divider=3)
                    print(f"{before_shipped} - 2nd before Shipped -> Fixed formula")

                    when_shipped = warehouse.test.calculate(before_shipped)
                    print(f"{when_shipped} - 3nd When Shipped -> Sorting Test")








        print("Main -> ETL executed")
        logger.info("Main -> ETL executed")

    except Exception as e:
        print(f"Main Error -> {e}")
        logger.error(f"Main Error -> {e}")


if __name__ == '__main__':
    business_days = 1

    main(business_days, data_file)
