import logging
import inspect

from parse_txt_data import *


#TODO set config and logging file -> test it
#TODO connect file to data processor
#TODO test paths connection to file and on other machine
#TODO loggigng the main function
#TODO loggigng the parse_txt_data function

#TODO Check all textes for typos and mistakes -> IDE Code inspection

#TODO README file main
#TODO README for each module

#TODO Design file (business logic)


log_file = None
logging.basicConfig()
logger = logging.getLogger(__name__)

# TEST
filename = r"D:\0_tech\1_ARK_DS\heatTransformers_assignment\Arkadii_Assignment_HT\data\dataset.txt"
all_warehouses = parse_data(filename)

# Corrected testing code
print("###### Testing Warehouse and Products inside ######")
for warehouse in all_warehouses:
    print(f"Created -> {warehouse} ")
    print()
    print(f"Test Warehouse Unit -> {warehouse.unit}")
    print(f"Test Warehouse Type -> {type(warehouse.unit)}")

    for product in warehouse.starting_products:
        print()
        print(f"Test product -> {product}")
        print(f"Test product Init Numb -> {product.initial_number}")
        print(f"Test product Last Numb -> {product.last_number}")
        print(f"Test product Type -> {type(product)}")

        test_value_for_formula = product.initial_number

        # Directly using the formula without iterating
        try:
            result = warehouse.formula.calculate(test_value_for_formula)
            print(f"Result of '{warehouse.formula.formula_str}' with input {test_value_for_formula} is {result}")
        except ValueError as e:
            print(e)



#
# def main_python_program(business_days: int, all_warehouses: list):
#     """
#     INPUT:
#         - business_days (int): Number of business days.
#
#     Deserialize data from a text file:
#         - Convert all data to objects (warehouses as datasets and products within them as data points).
#
#     Run an iteration loop over the data:
#         - Loop over 10 days.
#             - Loop over all warehouses per day (7 units for now).
#                 - Loop over the list of products (starting balance).
#                     - Run the 'before_shipped' formula (New = Old / 3).
#                     - Run the warehouse formula (might be unique each time).
#                     - Run the warehouse sorting test (might be unique each time).
#                     - Store the product in the 'arrivals' list of other warehouses.
#                     - Make a transaction record in the database (print for test now and SQL record in PySpark).
#             - Loop over warehouses:
#                 - Move products from the 'arrivals' list to the 'starting' list.
#                 - Print in the console the 'starting' balance of products for all warehouses for
#                   the end of the business day.
#
#     RETURN:
#         - Updated list with warehouses with nice balance.
#     """
#
#     function_name = inspect.currentframe().f_code.co_name
#     logger.info(f"Main python program run...{function_name}")
#     print(f"Main python program run...{function_name}")
#
#     try:
#         for day in business_days:
#             for warehouse in all_warehouses:
#                 for product in product.starting_balance:
#
#
#                     # TODO -> Create temp variable, into what you are copying object from list to work with
#                     print(r"Store Product in separate variable .pop list")
#
#                     print(r"run before_shipped formula (New = Old / 3)")
#                     print(r"run warhouse formula (might be eachtime unique)")
#                     print(r"run warhouse sorting test (might be eachtime unique)")
#                     print(r"store product in arrivals list of other warehouses")
#                     print(r"print make a Transaction record in database")
#
#                     logger.info(r"Transaction was successfull!")
#
#             for warehouse in all_warehouses:
#                 print(r"move products form 'arrivals' list to 'current' list")
#                 print(r"print in console 'current' balance of products for all warehouses")
#                 logger.info(r"WareHouses are updated!")
#
#         all_warehouses_updated:list = []
#         return all_warehouses_updated
#
#     except Exception as e:
#         print(f"Error while processing warehose operations...{e}")
#         logger.error(f"Error while processing warehose operations...{e}")
#
#
# if __name__ == '__main__':
#
#     data_file = None            # Path to dataset
#     business_days: int = 10
#     # raw_data = get_data(data_file)
#     # all_warehouses = parce_warehouses(raw_data)
#     main_python_program(business_days, all_warehouses)