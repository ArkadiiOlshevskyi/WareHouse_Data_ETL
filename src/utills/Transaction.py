import uuid
from datetime import datetime


class Transaction:
    """
    Designed for creating rows into SQL or any database.
    When Product is moved from one storage to another, a record about it is created.
    - generated uuid id - for unique id number of transaction
    - time_stamp        - for unique time value of transaction
    """

    # TODO -> transaction should reflect SQL row (table structure)
    def __init__(self,
                 warehouse_id: int,
                 warehouse_name: str,
                 warehouse_formula: str,
                 product_origin: int,
                 product_destination: int,
                 starting_product_id: int,
                 current_product_id: int,
                 product_test: str,
                 product_test_bool: bool,   # TODO loading to SQL bool value
                 day_number: int):

        self.transaction_id = str(uuid.uuid4())
        self.transaction_datetime_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.warehouse_id = warehouse_id
        self.warehouse_name = warehouse_name
        self.warehouse_formula = warehouse_formula
        self.product_origin = product_origin
        self.product_destination = product_destination
        self.starting_product_id = starting_product_id
        self.current_product_id = current_product_id
        self.product_test = product_test                # str human readable formula from dataset
        self.product_test_bool = product_test_bool
        self.day_number = day_number                    # counter

    def __str__(self):
        return (f"Transaction № {self.transaction_id} from {self.transaction_datetime_stamp}:\n"
                f"Warehouse ID: {self.warehouse_id}\n"
                f"Warehouse Name: {self.warehouse_name}\n"
                f"Warehouse Formula: {self.warehouse_formula}\n"
                f"Product Origin: {self.product_origin}\n"
                f"Product Destination: {self.product_destination}\n"
                f"Starting Product ID: {self.starting_product_id}\n"
                f"Current Product ID: {self.current_product_id}\n"
                f"Product Test: {self.product_test}\n"
                f"Product Test Bool: {self.product_test_bool}\n"
                f"Day Number: {self.day_number}\n"
                )


# # TEST
# new_transaction = Transaction(
#     warehouse_id=1,
#     warehouse_name="Warehouse 1",
#     warehouse_formula="New = Old + 7",
#     product_origin=1,
#     product_destination=3,
#     starting_product_id=77,
#     current_product_id=1488,
#     product_test="divisible on 7",
#     product_test_bool=False,
#     day_number=2
# )
#
# print(f"New TEST Transaction Created:\n{new_transaction}")
