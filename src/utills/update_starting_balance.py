import inspect
import logging

logger = logging.getLogger(__name__)


def update_starting_balance(warehouse: object):
    """
    Moves products from 'new_arrivals_products' to 'starting_products' if the latter is empty,
    and then clears 'new_arrivals_products'.

    Parameters:
        warehouse (Warehouse): The warehouse object to process.

    Returns:
        processed_warehouses (list): list of warehouses that have been processed.
    """
    function_name = inspect.currentframe().f_code.co_name
    log_message_start = f"Running function -> {function_name}"
    logger.info(log_message_start)
    print(log_message_start)  # Used for development stage

    processed_warehouses = []

    try:
        # Check if starting_products list is empty
        if not warehouse.starting_products:
            while warehouse.new_arrivals_products:
                product = warehouse.new_arrivals_products.pop(0)
                warehouse.starting_products.append(product)

                message_success = f"Moved product -> {product} to {warehouse.name}"
                logger.info(message_success)
                print(message_success)

            processed_warehouses.append(warehouse)
        else:
            message_else = f"Warning! Warehouse '{warehouse.name}' still has unprocessed products."
            logger.info(message_else)
            print(message_else)

        return processed_warehouses

    except Exception as e:
        log_message_error = f"Error occurred: -> {str(e)}, {str(e.args)}"
        logger.error(log_message_error)
        print(log_message_error)  # Used for development stage
        raise  # Rethrow after logging


