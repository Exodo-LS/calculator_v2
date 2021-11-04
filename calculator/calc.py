"""Content of calc.py"""
# The imports to perform each operation
from calculator.operations.addition import Addition
from calculator.operations.subtraction import Subtraction
from calculator.operations.multiplication import Multiplication
from calculator.operations.division import Division


class Calculator:
    """This will be the defined Calculator class"""

    # This is the history block of calculator.py
    history = []

    @staticmethod
    def get_calculation_first():
        """Returns the first item of the history"""
        return Calculator.history[0].get_result()

    @staticmethod
    def get_calculation_last():
        """Returns the last item of the history"""
        return Calculator.history[-1].get_result()

    @staticmethod
    def get_history_len():
        """Returns the history list"""
        return len(Calculator.history)

    @staticmethod
    def clear_history():
        """Clears history list"""
        Calculator.history.clear()
        return True

    @staticmethod
    def remove_calculation(num):
        """Removes a select item from history"""
        Calculator.history.pop(num)
        return Calculator.history

    @staticmethod
    def history_append(calculated):
        """Appends Item To List"""
        Calculator.history.append(calculated)

    # This is the calculations part of calculator.py
    @staticmethod
    def addition(*args):
        """This function performs addition"""
        plus = Addition(args)
        Calculator.history_append(plus)
        return Calculator.get_calculation_last()

    @staticmethod
    def subtraction(*args):
        """This function performs subtraction"""
        minus = Subtraction(args)
        Calculator.history_append(minus)
        return Calculator.get_calculation_last()

    @staticmethod
    def multiplication(*args):
        """This function performs multiplication"""
        star = Multiplication(args)
        Calculator.history_append(star)
        return Calculator.get_calculation_last()

    @staticmethod
    def division(*args):
        """This function performs division"""
        slash = Division(args)
        Calculator.history_append(slash)
        return Calculator.get_calculation_last()
