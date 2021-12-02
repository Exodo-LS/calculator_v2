"""Multiplication Class"""
from calculator.operations.calculations import Calculations


class Multiplication(Calculations):
    """multiplication calculation object"""

    def get_result(self):
        """get the multiplication results"""
        value_product = 1.0
        for value in self.values:
            value_product = value_product * value
        return value_product
