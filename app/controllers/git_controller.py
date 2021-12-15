"""Git Controller CLass"""
from flask import render_template
from app.controllers.controller import ControllerBase

class GitController(ControllerBase):
    """Git Tutorial from Project 1"""
    @staticmethod
    def get():
        """Displays the git tutorial"""
        return render_template('Git_Tutorial.html')