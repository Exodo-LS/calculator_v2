"""Testing the Calculator"""
import pytest
from calculator.history.calculations import Calculations
from calculator.operations.addition import Addition


@pytest.fixture()
def clear_history():
    """Defines the function each time it is run"""
    # pylint: disable=redefined-outer-name
    Calculations.clear_history()


@pytest.fixture()
def addition_config():
    """Defines the function each time it is run"""
    # pylint: disable=redefined-outer-name
    values = (1.0, 2.0)
    addition = Addition(values)
    Calculations.history_append(addition)


# History Block
def test_get_history_len(clear_history, addition_config):
    """Tests if there are values in history"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert Calculations.get_history_len() == 1


def test_clear_history(clear_history, addition_config):
    """Tests the clear history"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert Calculations.get_history_len() == 1
    Calculations.clear_history()
    assert Calculations.get_history_len() == 0
    assert Calculations.clear_history() == True


def test_get_calculation_first(clear_history, addition_config):
    """Testing get calculation first"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert Calculations.get_calculation_first().get_result() == 3.0


def test_get_calculation_last_value(clear_history, addition_config):
    """Testing get calculation last"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert Calculations.get_calculation_last_value().get_result() == 3.0


def test_get_calculation_select(clear_history, addition_config):
    """Testing get calculation select"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert Calculations.get_calculation_select(0).get_result() == 3.0


def test_get_calculation_last(clear_history, addition_config):
    """Tests if it returns last calculation as an object"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert isinstance(Calculations.get_calculation_last(), Addition)
