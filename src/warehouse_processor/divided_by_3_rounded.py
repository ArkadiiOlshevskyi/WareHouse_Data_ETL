import logging
import inspect

logger = logging.getLogger(__name__)


def divided_by_3_rounded(product_number: int, divider: int) -> int:
    """
    Divides a product number by a given divider, rounding the result.

    This function divides the provided product number by the specified divider, then
    rounds the result to the nearest integer. It logs and prints the process.

    Args:
        product_number (int): The product index number, which changes according to transactions.
        divider (int): The value for division, adjustable in the future.

    Returns:
        int: The rounded result of the division if successful.

    Raises:
        ZeroDivisionError: If the divider is zero.
        Exception: For any other issues during the division process.
    """
    function_name = inspect.currentframe().f_code.co_name
    logger.info(f"Warehouse_operation -> {function_name}")
    print(f"Warehouse_operation -> {function_name}")

    if divider == 0:
        message = "Divider cannot be zero!"
        logger.warning(f"Warehouse_operation -> {message}")
        print(f"Warehouse_operation -> {message}")
        raise ZeroDivisionError(message)

    try:
        product_number_updated = product_number // divider
        product_number_updated_rounded = round(product_number_updated)

        logger.info(f"Warehouse_operation -> Successfully, current product number is -> {product_number_updated_rounded}")
        print(f"Warehouse_operation -> Successfully, current product number is -> {product_number_updated_rounded}")

        return product_number_updated_rounded

    except Exception as e:
        logger.error(f"Warehouse_operation -> Failed, current product number is {product_number}, error: {str(e)}")
        print(f"Warehouse_operation -> Failed, current product number is {product_number}, error: {str(e)}")
        raise

# ### TEST CASE ###
# product_number = 50
# divider = 3
#
# new_number = divided_by_3_rounded(product_number, divider)
