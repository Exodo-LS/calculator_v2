"""Testing to see if the Calculator works"""
import pytest
from calculator.calculate import Calculate
from calculator.history.calculations import Calculations


# As Instructed In Class
@pytest.fixture
def clear_history():
    """Defines the function each time it is run"""
    # pylint: disable=redefined-outer-name
    Calculations.clear_history()


# Operations Block
def test_calc_add(clear_history):
    """This tests the Addition Function"""
    # pylint: disable=unused-argument,redefined-outer-name
    my_tuple = (1.0, 3.0, 6.0, 10.0)
    Calculate.add_values(my_tuple)
    assert Calculate.get_result() == 20.0


def test_calc_subtract(clear_history):
    """This tests the Subtraction Function"""
    # pylint: disable=unused-argument,redefined-outer-name
    my_tuple = (1.0, 3.0, 5.0)
    Calculate.subtract_values(my_tuple)
    assert Calculate.get_result() == -7.0


def test_calc_multiply(clear_history):
    """This tests the Multiplication Function"""
    # pylint: disable=unused-argument,redefined-outer-name
    my_tuple = (5.0, 4.0, 3.0)
    Calculate.multiply_values(my_tuple)
    assert Calculate.get_result() == 60.0


def test_calc_divide(clear_history):
    """This tests the Division Function"""
    # pylint: disable=unused-argument,redefined-outer-name
    my_tuple = (18.0, 3.0, 2.0)
    Calculate.divide_values(my_tuple)
    assert Calculate.get_result() == 3.0
