"""Multiplication Class V2"""
from calculator.operations.calculations import Calculations


class Multiplication(Calculations):
    """Contents of Multiplication:"""

    def get_result(self):
        """Gets Multiplication Results"""
        value_product = 1.0
        for value in self.values:
            value_product *= value
        return value_product
