"""Docker Controller CLass"""
# pylint: disable=(no-name-in-module)
# pylint: disable=(import-error)
# pylint: disable=(too-few-public-methods)
from flask import render_template
from app.controllers.controller import ControllerBase

class DockerController(ControllerBase):
    """Docker Tutorial from Project 1"""
    @staticmethod
    def get():
        """Displays the Docker Tutorial"""
        return render_template('Docker_Tutorial.html')
