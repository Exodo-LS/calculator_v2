"""Subtraction Class"""
from calculator.operations.calculations import Calculations


class Subtraction(Calculations):
    """subtraction calculation object"""

    def get_result(self):
        """get the subtraction results"""
        value_dif = 0.0
        for value in self.values:
            value_dif = value_dif - value
        return value_dif
