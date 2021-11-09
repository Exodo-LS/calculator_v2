"""Testing the Calculator"""
import pytest
from calculator.history.calculations import Calculations
from calculator.operations.addition import Addition
from calculator.operations.subtraction import Subtraction
from calculator.operations.multiplication import Multiplication
from calculator.operations.division import Division


@pytest.fixture()
def clear_history():
    """Defines the function each time it is run"""
    # pylint: disable=redefined-outer-name
    Calculations.clear_history()


@pytest.fixture()
def operation_config():
    """Defines the function each time it is run"""
    # pylint: disable=redefined-outer-name
    values = (1.0, 2.0)
    addition = Addition(values)
    subtraction = Subtraction(values)
    multiplication = Multiplication(values)
    division = Division(values)
    Calculations.add_calculation(addition)
    Calculations.add_calculation(subtraction)
    Calculations.add_calculation(multiplication)
    Calculations.add_calculation(division)


# History Block
def test_add_calculation_to_history(clear_history, operation_config):
    """Testing clear history returns true for success"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert Calculations.count_history() == 4


def test_clear_calculation_history(clear_history, operation_config):
    """testing clear history"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert Calculations.count_history() == 4
    Calculations.clear_history()
    assert Calculations.count_history() == 0
    assert Calculations.clear_history() == True


def test_get_calculation(clear_history, operation_config):
    """Testing getting a specific calculation out of the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_calculation(1).get_result() == -3
    assert Calculations.get_calculation(2).get_result() == 2


def test_get_calc_last_result_value(clear_history, operation_config):
    """Testing getting the last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_last_calculation_result_value() == 0.5


def test_get_calculation_first(clear_history, operation_config):
    """Testing getting the last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_first_calculation().get_result() == 3


def test_history_count(clear_history, operation_config):
    """Testing getting the count of calculations from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.count_history() == 4


def test_get_calc_last_result_object(clear_history, operation_config):
    """Testing getting the last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    # This test if it returns the last calculation as an object
    assert isinstance(Calculations.get_last_calculation_object(), Division)
