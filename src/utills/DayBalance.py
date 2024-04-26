import inspect
import logging

logger = logging.getLogger(__name__)


class DayBalance:
    """
    DataFrame that contains information of WareHouses Product balances in one current business day
    """
    # count = 0  # Initialize a class attribute to track the count of objects.

    def __init__(self,
                 day_number: int,
                 day_name: str,
                 logical_operator: bool,
                 other_object: object):
        """
        Initialize the MyObject with specified attributes.
        Parameters:
            name (str): The name of the object.
            number (int): A numeric identifier for the object.
            logical_operator (bool): A boolean value representing a logical property of the object.
            other_object (object): Another object related to this instance.
        """
        self.name = name
        self.number = number
        self.logical_operator = logical_operator
        self.other_object = other_object
        MyObject.count += 1  # Increment the class counter each time an object is created

    def __str__(self):
        """
        Return a string representation of the object with all its details.
        Returns:
            str: Formatted string containing all the object's attributes.
        """
        other_object_repr = str(self.other_object) if self.other_object else "None"
        return (f"New Template Object:\n"
                f"Object Name ID: {self.name}\n"
                f"Object Number: {self.number}\n"
                f"Object Logical Operator: {self.logical_operator}\n"
                f"Object Encapsulated Object: {other_object_repr}\n")
