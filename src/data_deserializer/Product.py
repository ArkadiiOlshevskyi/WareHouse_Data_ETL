class Product:
    """
    Represents a product stored in a warehouse.

    Attributes:
        initial_number (int): The original identifier or count for this product.
        last_number (int): The most recent identifier or count for this product after processing.
    """
    def __init__(self, initial_number: int, last_number: int):
        self.initial_number = initial_number
        self.last_number = last_number

    def __str__(self):
        return (f"Product: Initial Number -> {self.initial_number}, "
                f"Last Number -> {self.last_number}")

    def update_last_number(self, new_number: int):
        """
        Updates Product last number to a new processed value.
        Args:
            new_number (int): The new last number to be set for the product.
        :param new_number:
        :return:
        """
        self.last_number = new_number
