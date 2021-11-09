"""Subtraction Class V2"""
from calculator.operations.calculations import Calculations


class Subtraction(Calculations):
    """Contents of Subtraction:"""

    def get_result(self):
        """Gets Subtraction Results"""
        value_diff = 0.0
        for value in self.values:
            value_diff = value_diff - value
        return value_diff
