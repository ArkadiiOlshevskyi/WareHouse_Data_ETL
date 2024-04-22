from typing import List

from .Product import Product
from .Formula import Formula
from .SortingTest import SortingTest


class WareHouse:
    def __init__(self, unit: int, starting_products: List[Product],
                 new_arrivals_products: List[Product],
                 formula: Formula,
                 test: SortingTest):
        self.unit = unit
        self.starting_products = starting_products
        self.new_arrivals_products = new_arrivals_products
        self.formula = formula
        self.test = test

    def __str__(self):
        return (f"Warehouse Unit: {self.unit}\n"
                f"Starting Products: {[str(product) for product in self.starting_products]}\n"
                f"New Arrivals Products: {[str(product) for product in self.new_arrivals_products]}\n"
                f"Formula: {self.formula.formula_str}\n"
                f"Test: {self.test.test_formula}")
