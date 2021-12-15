"""Commands Controller CLass"""
# pylint: disable=(no-name-in-module)
# pylint: disable=(import-error)
# pylint: disable=(too-few-public-methods)
from flask import render_template
from app.controllers.controller import ControllerBase

class CommandsController(ControllerBase):
    """Useful Commands from Project 1"""
    @staticmethod
    def get():
        """Displays the commands"""
        return render_template('Useful_Commands.html')
