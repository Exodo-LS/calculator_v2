"""Testing to see if the Calculator works"""
import pprint
import pytest
from calculator.calc import Calculator


# As Instructed In Class
@pytest.fixture
def clear_history():
    """Defines the function each time it is run"""
    # pylint: disable=redefined-outer-name
    Calculator.clear_history()


# Operations Block
def test_calc_add(clear_history):
    """This tests the Addition Function"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.addition(1.0, 0.0) == 1.0
    assert Calculator.addition(1.0, 1.0) == 2.0
    assert Calculator.addition(1.0, 2.0) == 3.0
    assert Calculator.addition(1.0, 3.0) == 4.0
    assert Calculator.addition(1.0, 4.0) == 5.0
    assert Calculator.addition(1.0, 5.0) == 6.0
    assert Calculator.get_history_len() == 6
    assert Calculator.get_calculation_first() == 1.0
    assert Calculator.get_calculation_last() == 6.0
    pprint.pprint(Calculator.history)


def test_calc_subtract(clear_history):
    """This tests the Subtraction Function"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.subtraction(1.0, 1.0) == 0.0
    assert Calculator.subtraction(1.0, 2.0) == -1.0
    assert Calculator.subtraction(5.0, 3.0) == 2.0
    assert Calculator.subtraction(2.0, 4.0) == -2.0
    assert Calculator.subtraction(3.0, 5.0) == -2.0
    assert Calculator.get_history_len() == 5
    assert Calculator.get_calculation_first() == 0.0
    assert Calculator.get_calculation_last() == -2.0
    pprint.pprint(Calculator.history)


def test_calc_multiply(clear_history):
    """This tests the Multiplication Function"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.multiplication(1.0, 0.0) == 0.0
    assert Calculator.multiplication(1.0, 1.0) == 1.0
    assert Calculator.multiplication(1.0, 2.0) == 2.0
    assert Calculator.multiplication(2.0, 3.0) == 6.0
    assert Calculator.multiplication(3.0, 4.0) == 12.0
    assert Calculator.multiplication(4.0, 5.0) == 20.0
    assert Calculator.get_history_len() == 6
    assert Calculator.get_calculation_first() == 0.0
    assert Calculator.get_calculation_last() == 20.0
    pprint.pprint(Calculator.history)


def test_calc_divide(clear_history):
    """This tests the Division Function"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.division(0.0, 1.0) == 0.0
    assert Calculator.division(1.0, 1.0) == 1.0
    assert Calculator.division(4.0, 2.0) == 2.0
    assert Calculator.division(9.0, 3.0) == 3.0
    assert Calculator.division(16.0, 4.0) == 4.0
    assert Calculator.division(25.0, 5.0) == 5.0
    assert Calculator.get_history_len() == 6
    assert Calculator.get_calculation_first() == 0.0
    assert Calculator.get_calculation_last() == 5.0
    pprint.pprint(Calculator.history)


# History Block
def test_get_calculation_first(clear_history):
    """This tests getting the first position of the list"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.addition(1.0, 6.0) == 7.0
    assert Calculator.addition(5.0, 7.0) == 12.0
    assert Calculator.get_calculation_first() == 7.0
    pprint.pprint(Calculator.history)


def test_get_calculation_last(clear_history):
    """This tests getting the first position of the list"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.addition(1.0, 6.0) == 7.0
    assert Calculator.addition(5.0, 7.0) == 12.0
    assert Calculator.get_calculation_last() == 12.0
    pprint.pprint(Calculator.history)


def test_get_history_len(clear_history):
    """This tests getting the length of the listen"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.get_history_len() == 0
    assert Calculator.addition(1.0, 6.0) == 7.0
    assert Calculator.addition(5.0, 7.0) == 12.0
    assert Calculator.addition(2.0, 2.0) == 4
    assert Calculator.get_history_len() == 3
    pprint.pprint(Calculator.history)


def test_clear_history(clear_history):
    """This tests the Clear History function"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.addition(1.0, 6.0) == 7.0
    assert Calculator.addition(5.0, 7.0) == 12.0
    assert Calculator.addition(2.0, 2.0) == 4.0
    assert Calculator.addition(3.0, 6.0) == 9.0
    assert Calculator.get_history_len() == 4
    Calculator.clear_history()
    assert Calculator.get_history_len() == 0
    pprint.pprint(Calculator.history)


def test_remove_calculation(clear_history):
    """This tests the Removal of an Item Function"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.addition(1.0, 6.0) == 7.0
    assert Calculator.addition(5.0, 7.0) == 12.0
    assert Calculator.addition(2.0, 2.0) == 4.0
    assert Calculator.addition(3.0, 6.0) == 9.0
    assert Calculator.get_history_len() == 4
    Calculator.remove_calculation(3)
    assert Calculator.get_history_len() == 3
    pprint.pprint(Calculator.history)
