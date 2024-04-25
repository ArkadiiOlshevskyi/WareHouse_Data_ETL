import inspect
import logging

logger = logging.getLogger(__name__)


class SortingTestResult:
    """
    Encapsulates the result of a sorting test applied to a product.
    Attributes:
        new_product_number (int): The product number being tested.
        new_warehouse_unit_number (int): The warehouse unit to which the product is assigned.
        is_divisible (bool): Indicates if the product number is divisible by the divisor ("True" or "False").
    """

    def __init__(self, new_product_number: int,
                 warehouse_unit_number: int,
                 is_divisible: bool):
        self.new_product_number = new_product_number
        self.new_warehouse_unit_number = warehouse_unit_number
        self.is_divisible = is_divisible

    def __str__(self):
        return (f"New Product Number: {self.new_product_number}, "
                f"New Warehouse Unit: {self.new_warehouse_unit_number}, "
                f"Is Divisible: {self.is_divisible}")


class SortingTest:
    """
    Represents a test to sort products into different warehouse units based on divisibility.
    Attributes:
        divisor (int): The divisor for the test.
        if_true_warehouse_unit (int): Warehouse unit number if the product is divisible.
        if_false_warehouse_unit (int): Warehouse unit number if the product is not divisible.
    """

    def __init__(self,
                 test_formula_text: str,
                 if_true_warehouse_unit: str,
                 if_false_warehouse_unit: str):
        self.divisor = int(test_formula_text.split()[-1])
        self.if_true_warehouse_unit = int(if_true_warehouse_unit.split()[-1])
        self.if_false_warehouse_unit = int(if_false_warehouse_unit.split()[-1])
        self.test_formula_text = test_formula_text

    def calculate(self, initial_product_number: int) -> SortingTestResult:
        """
        Evaluates the product number for divisibility, assigns a warehouse based on the result.
        Args:
            initial_product_number (int): The product number to test.
        Returns:
            SortingTestResult: Outcome of the test, including product number, assigned warehouse unit, and divisibility result.
        """
        function_name = inspect.currentframe().f_code.co_name
        message_info = (f"Running {self.__class__.__name__} {function_name} \n"
                    f"with product_number = {initial_product_number} \n"
                    f"and Sorting Test -> {self.test_formula_text}")
        logger.info(message_info)
        print(message_info)

        try:
            is_divisible = initial_product_number % self.divisor == 0
            warehouse_unit_number = self.if_true_warehouse_unit if is_divisible else self.if_false_warehouse_unit
            new_product_number = round(initial_product_number / self.divisor)

            result = SortingTestResult(new_product_number,
                                       warehouse_unit_number,
                                       is_divisible)
            logger.info(f"Successfully tested: {result}")
            print(f"Successfully tested: {result}")
            return result
        except Exception as e:
            logger.error(f"Error during test: {e}")
            print(f"Error during test: {e}")
            raise
