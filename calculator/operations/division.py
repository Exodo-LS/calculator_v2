"""Division Class V2"""
from calculator.operations.calculations import Calculations


class Division(Calculations):
    """Contents of Division:"""

    def get_result(self):
        """Gets Division Results"""
        value_div = 0.0
        for value in self.values:
            if value != 0:
                value_div = self.values[0] / self.values[1]
            else:
                value_div = 0
        return value_div
