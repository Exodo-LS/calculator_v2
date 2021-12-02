"""Division Class V2"""
from calculator.operations.calculations import Calculations


class Division(Calculations):
    """Contents of Division:"""

    def get_result(self):
        """Gets Division Results"""
        value_div = 1.0
        for value in self.values:
            value_div = (value_div / value) if value != 0 else "Divide By Zero Detected"
        return value_div
