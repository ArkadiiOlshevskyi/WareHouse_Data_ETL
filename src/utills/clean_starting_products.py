import inspect
import logging

logger = logging.getLogger(__name__)


def remove_products(warehouse: object,
                    products_to_remove: list
                    ):
    """
    Removes Products from WareHouse by matching them with Processed product copies.
    This is processing function, and it performs action without any returning object.
    This function takes Products and object and put in into
    New Ware House (from by Unit Number) from all warehouses selection.

    Parameters:
        warehouse (object): WareHouse object.
        products_to_remove (list): Processing Product(as copy) stored in separate variable.

    Raises:
        Exception: Captures and logs any exceptions that occur during the function's execution.
    """

    function_name = inspect.currentframe().f_code.co_name
    log_message_start = f"Running function -> {function_name}"
    logger.info(log_message_start)
    print(log_message_start)  # Used for development stage

    try:
        # Track if any products were actually removed
        removed_any = False

        for removed_product in products_to_remove:
            if removed_product in warehouse.starting_products:
                warehouse.starting_products.remove(removed_product)

                message_success = str(f"Removed product -> {removed_product.initial_number} from {warehouse.name}")
                logger.info(message_success)
                print(message_success)
                removed_any = True

            else:
                logger.info(f"Product -> {removed_product.initial_number} not found in -> {warehouse.name}")

        if not removed_any:
            message_else = f"No products were removed from -> {warehouse.name}."
            logger.info(message_else)
            print(message_else)
        #
        # for warehouse.starting_products in warehouse:
        #     if

    except Exception as e:
        log_message_error = f"Error occurred: -> {str(e)}, {str(e.args)}"
        logger.error(log_message_error)
        print(log_message_error)  # Used for development stage
        pass
