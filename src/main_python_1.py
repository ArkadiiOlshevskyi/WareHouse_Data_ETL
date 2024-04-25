import logging
import inspect

from parse_txt_data import parse_data
from warehouse_processor.divided_by_3_rounded import *

from utills.timer import *
from utills.Transaction import *
from utills.move_product import *
from utills.clean_starting_products import *

from log_setup import setup_logging

logger = logging.getLogger(__name__)

log_filename = "WareHouse_Data_ETL\\logs\\log.txt"
data_file = "WareHouse_Data_ETL\\data\\dataset.txt"


@timer
def main(business_days: object,
         data_file: object):
    """
    Main ETL pipeline function.
    :type data_file: object
    :type business_days: object
    :return: None
    """
    function_name = inspect.currentframe().f_code.co_name
    logger.info(f"Main ETL pipeline -> {function_name}")

    setup_logging(log_filename)

    try:
        all_warehouses = parse_data(data_file)
        # print(f"Total WAREHOUSES -> {len(all_warehouses)}")
        all_transactions: list = []
        # print(f"Total TRANSACTIONS -> {len(all_transactions)}")

        for day in range(1, business_days + 1):
            logger.info(f"Processing All WareHouses during the {business_days} business days")
            for warehouse in all_warehouses:

                products_to_remove = []   # list that used to compare and remove processed copies of the products

                print(f"WareHouse Name -> {warehouse.name}")
                # print(f"WareHouse Unit -> {warehouse.unit}")
                # print(f"WareHouse Starting Products-> {warehouse.starting_products}")
                # print(f"WareHouse Products total -> {len(warehouse.starting_products)}")
                # print(f"WareHouse Formula text -> {warehouse.formula.formula_original_text}")
                # print(f"WareHouse Test text -> {warehouse.test.test_formula_text}")

                for product in warehouse.starting_products:

                    processing_product = product
                    processed_product_number = processing_product.last_number
                    print(type(processing_product))
                    print(f"Product Init Number -> {processing_product.initial_number}")
                    print(f"Product LAST Number -> {processing_product.last_number}")


                    print()
                    print(f"=> Processing Product number inside of the {warehouse.name}")

                    shipping_location = warehouse.formula.calculate(processing_product.last_number)
                    print(f"{shipping_location} - 1st Shipping Location "
                          f"-> WareHouse Formula {warehouse.formula.formula_original_text}")
                    before_shipped = divided_by_3_rounded(shipping_location, divider=3)
                    print(f"{before_shipped} - 2nd before Shipped -> Fixed formula")
                    when_shipped = warehouse.test.calculate(before_shipped)
                    print(f"{when_shipped} - 3nd When Shipped -> Sorting Test")

                    new_warehouse_unit = when_shipped.new_warehouse_unit_number
                    print(f"{new_warehouse_unit} - New WareHouse Unit Number -> Sorting Test Results")
                    new_product_number = when_shipped.new_product_number
                    print(f"{new_product_number} - New Product Number -> Sorting Test Results")

                    # Moving processed product to list of all removed from current warehouse products
                    products_to_remove.append(processing_product)
                    print(f"Moved Products -> {products_to_remove}")
                    print(f"Moved Products -> {len(products_to_remove)}")

                    # TODO Change product last number wint new_product number
                    processing_product.update_last_number(new_product_number)
                    print(f'OVERWRITE number of produtct -> {processing_product.last_number}')

                    # TODO move_products from list new to current (Put product to new warehouse)
                    move_product(all_warehouses, processing_product, new_warehouse_unit)

                    # TODO Class transaction + append to all_transactions list
                    print()
                    new_transaction = Transaction(
                        warehouse.unit,
                        warehouse.name,
                        warehouse.formula.formula_original_text,
                        warehouse.unit,
                        new_warehouse_unit,
                        processing_product.initial_number,
                        new_product_number,
                        warehouse.test.test_formula_text,
                        when_shipped.is_divisible,    # TODO Test result object
                        day                           # TODO counter days in iteration
                    )
                    print(f"New Transaction Created:\n{new_transaction}")
                    logger.info(f"New Transaction Created:\n{new_transaction}")
                    all_transactions.append(new_transaction)

                # TODO cleanup products from starting_products in current warehouse
                remove_products(warehouse, products_to_remove)

        # TODO Move Products for wall warehouses for New_arrivals_products to Starting_products
        # TODO print balances for today







        print("Main -> ETL executed")
        logger.info("Main -> ETL executed")

    except Exception as e:
        print(f"Main Error -> {e}")
        logger.error(f"Main Error -> {e}")


if __name__ == '__main__':
    business_days = 10
    main(business_days, data_file)
