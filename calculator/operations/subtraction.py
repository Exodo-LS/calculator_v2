"""Subtraction Class V2"""
import pprint
from calculator.operations.calculations import Calculations


class Subtraction(Calculations):
    """Contents of Subtraction:"""

    def get_result(self):
        """Gets Subtraction Results"""
        value_diff = 0.0
        for value in self.values:
            value_diff = self.values[0] - self.values[1]
            pprint.pprint(value)
        return value_diff
