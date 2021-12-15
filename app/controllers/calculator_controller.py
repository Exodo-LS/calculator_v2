"""Calculator CController Class"""
# pylint: disable=(no-name-in-module)
# pylint: disable=(import-error)
# pylint: disable=(too-few-public-methods)

from flask import render_template, request, flash
from app.controllers.controller import ControllerBase
from app.controllers.csvmanager.csv_controller import CSVController
from calc.calculator import Calculator


class CalculatorController(ControllerBase):
    """Handles the Calculator's calculations"""
    @staticmethod
    def post():
        """Posts results"""
        if request.form['value1'] == '' or request.form['value2'] == '':
            error = 'You must enter a value for value 1 and or value 2'
        else:
            flash('You successfully calculated')
            value1 = request.form['value1']
            value2 = request.form['value2']
            operation = request.form['operation']
            my_tuple = (value1, value2)
            validate = getattr(Calculator, operation)(my_tuple)
            result = str(Calculator.get_last_result_value())
            if validate:
                CSVController.write(value1, value2, operation, result)
            return render_template('result.html',
                                   value1=value1, value2=value2, operation=operation, result=result)
        return render_template('calculator.html', error=error)
    @staticmethod
    def get():
        """get calculator form"""
        return render_template('calculator.html')
