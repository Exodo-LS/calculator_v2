"""Calculation History Class"""
from calculator.operations.addition import Addition
from calculator.operations.subtraction import Subtraction
from calculator.operations.multiplication import Multiplication
from calculator.operations.division import Division


class Calculations:
    """Manages history of the calculator"""
    history = []

    # pylint: disable=too-few-public-methods
    @staticmethod
    def clear_history():
        """Clears history list"""
        Calculations.history.clear()
        return True

    @staticmethod
    def get_history_len():
        """Returns the history list"""
        return len(Calculations.history)

    @staticmethod
    def get_calculation_first():
        """Returns the first item of the history"""
        return Calculations.history[0]

    @staticmethod
    def get_calculation_last():
        """Returns the last item of the history"""
        return Calculations.history[-1]

    @staticmethod
    def get_calculation_last_value():
        """Returns the last item of the history"""
        calculation = Calculations.get_calculation_last()
        return calculation.get_result()

    @staticmethod
    def get_calculation_select(num):
        """Returns selected item in history"""
        return Calculations.history[num]

    @staticmethod
    def remove_calculation(num):
        """Removes a select item from history"""
        Calculations.history.pop(num)
        return Calculations.history

    @staticmethod
    def history_append(calculated):
        """Appends Item To List"""
        Calculations.history.append(calculated)

    @staticmethod
    def append_subtraction(values):
        """Creates Subtraction Object And Adds It To History"""
        Calculations.history_append(Subtraction.create(values))
        return True

    @staticmethod
    def append_multiplication(values):
        """Creates Multiplication Object And Adds It To History"""
        Calculations.history_append(Multiplication.create(values))
        return True

    @staticmethod
    def append_division(values):
        """Creates Division Object And Adds It To History"""
        Calculations.history_append(Division.create(values))
        return True

    @staticmethod
    def append_addition(values):
        """Creates Addition Object And Adds It To History"""
        Calculations.history_append(Addition.create(values))
        return True
