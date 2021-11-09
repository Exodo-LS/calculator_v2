"""This is the revised calc.py"""
from calculator.history.calculations import Calculations


class Calculate:
    """This is the contents of calculate.py"""

    # It just calls methods from the Calculations class
    @staticmethod
    def get_result():
        """This returns the latest result of the calculator"""
        return Calculations.get_calculation_last()

    @staticmethod
    def add_values(tuple_values: tuple):
        """Addition Operation"""
        Calculations.append_addition(tuple_values)
        return True

    @staticmethod
    def subtract_values(tuple_values: tuple):
        """Subtraction Operation"""
        Calculations.append_subtraction(tuple_values)
        return True

    @staticmethod
    def multiply_values(tuple_values: tuple):
        """Multiplication Operation"""
        Calculations.append_multiplication(tuple_values)
        return True

    @staticmethod
    def divide_values(tuple_values: tuple):
        """Division Operation"""
        Calculations.append_division(tuple_values)
        return True
