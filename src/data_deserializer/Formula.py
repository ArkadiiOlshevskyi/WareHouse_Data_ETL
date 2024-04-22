class Formula:
    """
    Represents a mathematical formula to adjust product numbers.

    Attributes:
        formula_str (str): The string representation of the formula, where 'Old' represents the old number.
    """
    def __init__(self, formula_str: str):
        self.formula_str = formula_str.replace('New =', '').strip()

    def calculate(self, input_value: int) -> int:
        """
        Calculates the new value using the formula with the provided input value.

        Args:
            input_value (int): The input value to replace 'Old' in the formula.

        Returns:
            int: The result of the formula computation.

        Raises:
            ValueError: If an error occurs in formula evaluation.
        """
        modified_formula = self.formula_str.replace("Old", str(input_value))
        try:
            return eval(modified_formula, {"__builtins__": None})
        except Exception as e:
            raise ValueError(f"Error calculating formula: {e}")
