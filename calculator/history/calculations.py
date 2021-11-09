"""Calculation History Class"""
from calculator.operations.addition import Addition
from calculator.operations.subtraction import Subtraction
from calculator.operations.multiplication import Multiplication
from calculator.operations.division import Division


class Calculations:
    """Calculations class manages the history of calculations"""
    history = []

    # pylint: disable=too-few-public-methods
    @staticmethod
    def clear_history():
        """clear the history of calculations"""
        Calculations.history.clear()
        return True

    @staticmethod
    def count_history():
        """get number of items in history"""
        return len(Calculations.history)

    @staticmethod
    def get_last_calculation_object():
        """get last calculation"""
        return Calculations.history[-1]

    @staticmethod
    def get_last_calculation_result_value():
        """get last calculation convenience method"""
        calculation = Calculations.get_last_calculation_object()
        return calculation.get_result()

    @staticmethod
    def get_first_calculation():
        """get first calculation"""
        return Calculations.history[0]

    @staticmethod
    def get_calculation(num):
        """ get a specific calculation from history"""
        return Calculations.history[num]

    @staticmethod
    def add_calculation(calculation):
        """ get a generic calculation from history"""
        return Calculations.history.append(calculation)

    @staticmethod
    def add_addition_calculation(values):
        """create an addition and add object to history using factory method create"""
        Calculations.add_calculation(Addition.create(values))
        # Get the result of the calculation
        return Calculations.get_last_calculation_object()

    @staticmethod
    def add_subtraction_calculation(values):
        """create a subtraction object to history using factory method create"""
        Calculations.add_calculation(Subtraction.create(values))
        return Calculations.get_last_calculation_object()

    @staticmethod
    def add_multiplication_calculation(values):
        """Add a multiplication object to history using factory method create"""
        Calculations.add_calculation(Multiplication.create(values))
        return Calculations.get_last_calculation_object()

    @staticmethod
    def add_division_calculation(values):
        """Add a division object to history using factory method create"""
        Calculations.add_calculation(Division.create(values))
        return Calculations.get_last_calculation_object()
