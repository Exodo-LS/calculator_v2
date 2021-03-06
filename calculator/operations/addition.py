"""Addition Class V2"""
from calculator.operations.calculations import Calculations


class Addition(Calculations):
    """Contents of Addition Class:"""

    def get_result(self):
        """Gets the Addition Results"""
        value_sum = 0.0
        for value in self.values:
            value_sum += value
        return value_sum
