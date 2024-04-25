import inspect
import logging

logger = logging.getLogger(__name__)


def move_product(all_warehouses: list,
                 processing_product: object,
                 new_warehouse_unit_number: int):
    """
    Moves Product to WareHouse.
    This is processing function, and it performs action without any returning object.
    This function takes Products and object and put in into
    New Ware House (from by Unit Number) from all warehouses selection.

    Parameters:
        all_warehouses (list): List of all selected warehouses.
        processing_product (object): Processing Product(as copy) stored in separate variable.
        new_warehouse_unit_number (int): Number of Warehouse where this Product will be put in New_arrivals_products list.

    Raises:
        Exception: Captures and logs any exceptions that occur during the function's execution.
    """

    function_name = inspect.currentframe().f_code.co_name
    log_message_start = f"Running function -> {function_name}"
    logger.info(log_message_start)
    print(log_message_start)  # Used for development stage

    try:
        for new_warehouse in all_warehouses:
            if new_warehouse.unit == new_warehouse_unit_number:
                new_warehouse.new_arrivals_products.append(processing_product)

                print(f"New Warehouse Arrived Products -> {len(new_warehouse.new_arrivals_products)}")

                message_info = str(f"Processing product Found in -> {processing_product.last_number} \n"
                                   f"Moved to New warehouse -> {new_warehouse.name}")
                logger.info(message_info)
                print(message_info)
            else:
                message_else = str(f"Not Found Processing product in -> {new_warehouse_unit_number}")
                logger.info(message_else)
                print(message_else)

        log_message_done = f"Successfully Performed -> {function_name}"
        logger.info(log_message_done)
        print(log_message_done)  # Used for development stage

    except Exception as e:
        log_message_error = f"Error occurred: {str(e)}"
        logger.error(log_message_error)
        print(log_message_error)  # Used for development stage
        pass
