import logging
import inspect

logger = logging.getLogger(__name__)


def filter_divide_by_5(product_number: int, multiplier: int):
    """
    input:
    product: int - index number (that always changing according to transactions)
    multiplier: int - value for multiplication (that can be adjusted in future)
    :return:
    product_number_updated
    """

    function_name = inspect.currentframe().f_code.co_name
    logger.info(f"Warehouse_operation -> {function_name}")
    print(f"Warehouse_operation -> {function_name}")

    try:
        if multiplier == 0:
            raise ZeroDivisionError("Multiplier cannot be zero!")

        product_number_updated = product_number * multiplier

        logger.info(f"Warehouse_operation -> Successfully, current product number is {product_number_updated}")
        print(f"Warehouse_operation -> Successfully, current product number is {product_number_updated}")

        return product_number_updated

    except ZeroDivisionError as e:
        logger.warning(f"Warehouse_operation -> {e}, returning current product number is {product_number}")
        print(f"Warehouse_operation -> {e}, returning current product number is {product_number}")

    except Exception as e:
        logger.error(f"Warehouse_operation -> Failed, current product number is {product_number}")
        print(f"Warehouse_operation -> Failed, current product number is {product_number}")
