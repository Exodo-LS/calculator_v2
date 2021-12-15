"""Index Controller Class"""
# pylint: disable=(too-few-public-methods)
# pylint: disable=(no-name-in-module)
# pylint: disable=(import-error)

from flask import render_template, flash
from app.controllers.controller import ControllerBase

class IndexController(ControllerBase):
    """Initializes the index form"""
    @staticmethod
    def get():
        """gets the index form"""
        flash('Welcome to Project 3')
        return render_template('index.html')
