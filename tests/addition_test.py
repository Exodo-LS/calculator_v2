"""Testing Addition"""
from calc.calculations.addition import Addition

def test_calculation_addition():
    """testing that our calculator has a static method for addition"""
    #Arrange
    my_numbers = (1.0,2.0)
    addition = Addition(my_numbers)
    #Act
    #Assert
    assert addition.get_result() == 3.0
