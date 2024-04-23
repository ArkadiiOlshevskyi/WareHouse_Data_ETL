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

                    test_str = lines[idx + 3]
                    test_formula_text = lines[idx + 3].split(":")[1]
                    if_true_str = lines[idx + 4]
                    if_false_str = lines[idx + 5]
                    test = SortingTest(test_formula_text, test_str, if_true_str, if_false_str)

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
# # filename = r"D:\0_tech\1_ARK_DS\heatTransformers_assignment\Arkadii_Assignment_HT\src\data_processor_main.py"
# # filename = r"D:\0_tech\1_ARK_DS\heatTransformers_assignment\Arkadii_Assignment_HT\data\dataset.txt"
# filename = "WareHouse_Data_ETL\data\dataset.txt"
# all_warehouses = parse_data(filename)
#
# # Corrected testing code
# print("###### Testing Warehouse and Products inside ######")
# for warehouse in all_warehouses:
#     print(f"Created -> {warehouse} ")
#     print()
#     print(f"Test Warehouse Unit -> {warehouse.unit}")
#     print(f"Test Warehouse NAME -> {warehouse.name}")
#     print(f"Test Warehouse Type -> {type(warehouse.unit)}")
#
#     print(f"TEST SORTING FORMULA TEXT: {warehouse.test.test_formula_text}")
#
#     for product in warehouse.starting_products:
#         print()
#         print(f"Test product -> {product}")
#         print(f"Test product Init Numb -> {product.initial_number}")
#         print(f"Test product Last Numb -> {product.last_number}")
#         print(f"Test product Type -> {type(product)}")
#
#
#         test_value_for_formula = product.initial_number
#
#         # Directly using the formula without iterating
#         try:
#             result = warehouse.formula.calculate(test_value_for_formula)
#             print(f"Result of '{warehouse.formula.formula_str}' "
#                   f"with input {test_value_for_formula} is {result}")
#         except ValueError as e:
#             print(e)
