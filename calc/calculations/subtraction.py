"""Subtraction Class"""

from calc.calculations.calculation import Calculation

class Subtraction(Calculation):
    """subtraction calculation object"""
    def get_result(self):
        """get the subtraction results"""
        difference_of_values = 0.0
        for value in self.values:
            dif = self.values[0]
            difference_of_values =  dif - value
        return difference_of_values
