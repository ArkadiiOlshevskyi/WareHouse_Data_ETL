import logging
import inspect

logger = logging.getLogger(__name__)


def divided_by_3_rounded(product_number: int, divider: int):
    """
    input:
    product: int - index number (that always changing according to transactions)
    divider: int - value for division (that can be adjusted in future)
    :return:
    product_number_updated
    """

    function_name = inspect.currentframe().f_code.co_name
    logger.info(f"Warehouse_operation -> {function_name}")
    print(f"Warehouse_operation -> {function_name}")

    try:
        if divider == 0:
            raise ZeroDivisionError("Multiplier cannot be zero!")

        product_number_updated = product_number // divider
        product_number_updated_rounded = round(product_number_updated)

        logger.info(f"Warehouse_operation -> Successfully, current product number is {product_number_updated_rounded}")
        print(f"Warehouse_operation -> Successfully, current product number is {product_number_updated_rounded}")

        return product_number_updated

    except ZeroDivisionError as e:
        logger.warning(f"Warehouse_operation -> {e}, returning current product number is {product_number}")
        print(f"Warehouse_operation -> {e}, returning current product number is {product_number}")

    except Exception as e:
        logger.error(f"Warehouse_operation -> Failed, current product number is {product_number}")
        print(f"Warehouse_operation -> Failed, current product number is {product_number}")


### TEST CASE ###
product_number = 50
divider = 3


new_numer = divided_by_3_rounded(product_number, divider)
