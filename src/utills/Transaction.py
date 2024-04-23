import uuid
from datetime import datetime

class Transaction:
    """
    Designed for creating rows in to SQL or any database
    When Product moved from storage to storage, there are record about it.
    # generated uuid id - for unique id number of transaction
    # time_stamp        - for unique time value of transaction
    """

    # TODO -> transaction should reflect SQL row (table stucture)
    def __init__(self,
                 transaction_number: str,
                 time_stamp: str):

        self.transaction_number = transaction_number    
        self.time_stamp = time_stamp          # updatable value during warehouse processing

    @classmethod
    def create(cls):
        transaction_number = str(uuid.uuid4())
        time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return cls(transaction_number, time_stamp)
    
    def execute(self,
                all_warehouses: list,
                current_warehouse: object,
                new_warehouse_unit_number: int,
                product: object):
        """
        Executing Transaction by moving Product to New WareHouse
        Product appends in NewArrivalsProducts list of New WareHouse.
        :param all_warehouses:
        :param current_warehouse:
        :param new_warehouse_unit_number:
        :param product:
        :return: Transaction: object - will be used in SQL record creation
        """
        self.all_warehouses = all_warehouses
        self.current_warehouse = current_warehouse
        self.new_warehouse_unit_number = new_warehouse_unit_number
        self.product = product


# #### test ####
# new_transaction = Transaction.create()
# print(new_transaction)
# print(new_transaction.transaction_number)
# print(new_transaction.time_stamp)
