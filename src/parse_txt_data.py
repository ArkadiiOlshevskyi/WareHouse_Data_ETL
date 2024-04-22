import os
from typing import List

from data_deserializer.WareHouse import *
from data_deserializer.SortingTest import *
from data_deserializer.Formula import *


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
    current_dir = os.getcwd()
    full_path = os.path.join(current_dir, data_filename)

    all_warehouses = []

    try:
        with open(full_path, 'r') as data_file:
            lines = data_file.readlines()
            idx = 0
            while idx < len(lines):
                if lines[idx].startswith("Warehouse Unit"):
                    unit = int(lines[idx].split(":")[1].strip())
                    products_line = lines[idx + 1]
                    products = [int(p.strip()) for p in products_line.split(":")[1].strip().split(",")]
                    product_objs = [Product(initial_number=num, last_number=0) for num in products]
                    formula = Formula(lines[idx + 2].split(":")[1].strip())
                    test_str = lines[idx + 3]
                    if_true_str = lines[idx + 4]
                    if_false_str = lines[idx + 5]
                    test = SortingTest(test_str, if_true_str, if_false_str)
                    new_warehouse = WareHouse(unit, product_objs, [], formula, test)
                    all_warehouses.append(new_warehouse)
                    idx += 6  # move to the next warehouse block
                else:
                    idx += 1
    except Exception as e:
        print(f"Error while parsing data: {e}")

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
# filename = r"D:\0_tech\1_ARK_DS\heatTransformers_assignment\Arkadii_Assignment_HT\data\dataset.txt"
# all_warehouses = parse_data(filename)
#
# # Corrected testing code
# print("###### Testing Warehouse and Products inside ######")
# for warehouse in all_warehouses:
#     print(f"Created -> {warehouse} ")
#     print()
#     print(f"Test Warehouse Unit -> {warehouse.unit}")
#     print(f"Test Warehouse Type -> {type(warehouse.unit)}")
#
#     for product in warehouse.starting_products:
#         print()
#         print(f"Test product -> {product}")
#         print(f"Test product Init Numb -> {product.initial_number}")
#         print(f"Test product Last Numb -> {product.last_number}")
#         print(f"Test product Type -> {type(product)}")
#
#         test_value_for_formula = product.initial_number
#
#         # Directly using the formula without iterating
#         try:
#             result = warehouse.formula.calculate(test_value_for_formula)
#             print(f"Result of '{warehouse.formula.formula_str}' with input {test_value_for_formula} is {result}")
#         except ValueError as e:
#             print(e)
