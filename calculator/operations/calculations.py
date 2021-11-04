"""This class is our Calculations Class"""


class Calculations:
    """Calculations Class Contents:"""
    # pylint: disable=too-few-public-methods

    def __init__(self, values: tuple):
        """Constructor Method"""
        self.values = Calculations.convert_args_to_list_float(values)

    @staticmethod
    def convert_args_to_list_float(values):
        """Make values into a list of floats"""
        value_float = []
        for item in values:
            value_float.append(float(item))
        return value_float
