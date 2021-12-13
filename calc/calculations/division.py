"""Division Class"""
from calc.calculations.calculation import Calculation

class Division(Calculation):
    """division calculation object"""
    def get_result(self):
        """get the division results"""
        value_div = 1.0
        for value in self.values:
            value_div = (value_div / value) if value != 0 else 0
        return value_div
