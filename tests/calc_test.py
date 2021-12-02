"""Testing to see if the Calculator works"""
import pytest
from calculator.calculate import Calculate
from calculator.history.calculations import Calculations
from calculator.operations.addition import Addition
from calculator.operations.multiplication import Multiplication
from calculator.operations.subtraction import Subtraction
from calculator.operations.division import Division


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

    # ARRANGE
    my_tuple = (1.0, 3.0, 6.0, 10.0)
    # ACT
    Calculate.add_numbers(my_tuple)
    #ASSERT
    assert isinstance(Calculate.add_numbers(my_tuple), Addition)
    assert Calculate.get_last() == 20.0


def test_calc_subtract(clear_history):
    """This tests the Subtraction Function"""
    # pylint: disable=unused-argument,redefined-outer-name
    my_tuple = (1.0, 3.0, 5.0, 6.0)
    calc_result = Calculate.subtract_numbers(my_tuple)
    assert isinstance(calc_result, Subtraction)
    assert Calculate.get_last() == -15.0
    assert calc_result.get_result() == -15.0


def test_calc_multiply(clear_history):
    """This tests the Multiplication Function"""
    # pylint: disable=unused-argument,redefined-outer-name
    my_tuple = (5.0, 4.0, 3.0)
    Calculate.multiply_numbers(my_tuple)
    assert isinstance(Calculate.multiply_numbers(my_tuple), Multiplication)
    assert Calculate.get_last() == 60.0


def test_calc_divide(clear_history):
    """This tests the Division Function"""
    # pylint: disable=unused-argument,redefined-outer-name
    my_tuple = (1.0, 5.0, 2.0)
    Calculate.divide_numbers(my_tuple)
    assert isinstance(Calculate.divide_numbers(my_tuple), Division)
    assert Calculate.get_last() == 0.1


def test_calc_divide_zero(clear_history):
    """This tests the Division Function"""
    # pylint: disable=unused-argument,redefined-outer-name
    my_tuple = (1.0, 5.0, 2.0, 0.0)
    Calculate.divide_numbers(my_tuple)
    assert isinstance(Calculate.divide_numbers(my_tuple), Division)
    assert Calculate.get_last() == "Divide By Zero Detected"


def test_calc_polymorphism(clear_history):
    """This tests the Addition Function"""
    # pylint: disable=unused-argument,redefined-outer-name
    my_tuple = (1.0, 3.0, 6.0, 10.0)
    poly_tuple = (1.0, 3.0, 6.0)
    Calculate.add_numbers(my_tuple)
    Calculate.add_numbers(poly_tuple)
