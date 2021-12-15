"""Division Class"""
from calc.calculations.calculation import Calculation

class Division(Calculation):
    """division calculation object"""
    def get_result(self):
        """get the division results"""
        value_div = 0.0
        for value in self.values:
            value_div = (self.values[0] / value) if value != 0 else 'Divide By Zero Error'
        return value_div
