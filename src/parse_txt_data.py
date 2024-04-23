import os
import inspect
import logging
from typing import List

from data_deserializer.WareHouse import *
from data_deserializer.SortingTest import *
from data_deserializer.Formula import *
from src.data_deserializer import WareHouse

logger = logging.getLogger(__name__)


def parse_data(data_filename: str) -> List[WareHouse]:
    """
    Parses a data file to create a list of Warehouse objects.

    Args:
        data_filename (str): The path to the data file.

    Returns:
        List[WareHouse]: A list of WareHouse objects populated with their respective products and conditions.

    Raises:
        Exception: If there is an issue reading the file or parsing its content.
    """
    function_name = inspect.currentframe().f_code.co_name
    logging.info(f"Parsing data from .txt file...->{function_name}")

    script_dir = os.path.dirname(__file__)
    project_root = os.path.abspath(os.path.join(script_dir, os.pardir, os.pardir))
    full_path = os.path.join(project_root, data_filename)

    if not os.path.exists(full_path):
        error_msg = f"File not found: {full_path}"
        logger.error(error_msg)
        raise FileNotFoundError(error_msg)

    all_warehouses: list[WareHouse] = []

    try:
        with open(full_path, 'r') as data_file:
            lines = data_file.readlines()
            idx = 0
            while idx < len(lines):
                if lines[idx].startswith("Warehouse Unit"):
                    unit = int(lines[idx].split(":")[1].strip())

                    warehouse_name = lines[idx].split(":")[0].strip() + ":"

                    products_line = lines[idx + 1]
                    products = [int(p.strip()) for p in products_line.split(":")[1].strip().split(",")]
                    product_objs = [Product(initial_number=num, last_number=num) for num in products]

                    formula_original_str = lines[idx + 2].split(":")[1].strip()
                    formula = Formula(formula_original_str, formula_original_str)

                    test_formula_text = lines[idx + 3].split(":")[1]
                    if_true_str = lines[idx + 4]
                    if_false_str = lines[idx + 5]
                    test = SortingTest(test_formula_text, if_true_str, if_false_str)

                    new_warehouse = WareHouse(unit,
                                              warehouse_name,
                                              product_objs,
                                              [],
                                              formula,
                                              test)

                    all_warehouses.append(new_warehouse)
                    idx += 6  # move to the next warehouse block
                else:
                    idx += 1
                logging.info(f"Data extracted -> {function_name}")
                print(f"Data extracted -> {function_name}")
    except Exception as e:
        print(f"Error while parsing data: {e}")
        logging.error(f"Error while parsing data: {e}")

    return all_warehouses

# ########################### Data sample ##################################################################
# """
# Warehouse Unit: 0
# Starting Products: 74, 64, 74, 63, 53
# Warehouse Formula: New = Old * 7
# Test: divisible by 5
# If true: ship product to Warehouse Unit 1
# If false: ship product to Warehouse Unit 6
# """
# ########################### TEST ##################################################################
# filename = "WareHouse_Data_ETL\data\dataset.txt"
# all_warehouses = parse_data(filename)
#
# print("###### Testing Warehouse and Products inside ######")
# for warehouse in all_warehouses:
#     print(f"Test Warehouse NAME -> {warehouse.name}")
#
#     for product in warehouse.starting_products:
#         new_test_result = warehouse.test.calculate(product.initial_number)
#         print(type(new_test_result))
#         print(f"Init Number -> {product.initial_number}")
#         print(f"TEST SORTING FORMULA TEXT: {warehouse.test.test_formula_text}")
#         print(f"Test Result Product number -> {new_test_result.new_product_number}")
#         print(f"Test Result Warehouse ID -> {new_test_result.new_warehouse_unit_number}")
#         print(f"Test Result Warehouse Logic -> {new_test_result.is_divisible}")
