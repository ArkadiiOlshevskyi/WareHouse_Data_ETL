class TestResult:
    """
    Encapsulates the result of a sorting test applied to a product.

    Attributes:
        product_number (int): The product number being tested.
        warehouse_unit_number (int): The resulting warehouse unit to which the product is assigned.
    """
    def __init__(self, product_number: int, warehouse_unit_number: int):
        self.product_number = product_number
        self.warehouse_unit_number = warehouse_unit_number


class SortingTest:
    """
    Represents a conditional test to sort products into different warehouse units based on a criteria.

    Attributes:
        test_formula (str): The test condition, typically involving divisibility.
        if_true_warehouse_unit (int): Warehouse unit number if the condition is true.
        if_false_warehouse_unit (int): Warehouse unit number if the condition is false.
    """
    def __init__(self,
                 test_formula_text: str,
                 test_str: str,
                 if_true_str: str,
                 if_false_str: str):
        self.test_formula_text = test_formula_text
        self.test_formula = test_str.strip().replace("divisible by", "x %")
        self.if_true_warehouse_unit = int(if_true_str.split()[-1])
        self.if_false_warehouse_unit = int(if_false_str.split()[-1])

    def calculate(self, product_number: int) -> TestResult:
        """
        Evaluates the test formula and determines the warehouse unit based on the outcome.

        Args:
            product_number (int): The number to test against the formula.

        Returns:
            TestResult: The outcome of the test, indicating the appropriate warehouse unit.

        Raises:
            ValueError: If an error occurs in evaluating the test condition.
        """
        try:
            result = eval(self.test_formula, {'__builtins__': None}, {'x': product_number})
            warehouse_unit_number = self.if_true_warehouse_unit if result == 0 else self.if_false_warehouse_unit
            return TestResult(product_number, warehouse_unit_number)
        except Exception as e:
            raise ValueError(f"Error calculating test formula: {e}")
