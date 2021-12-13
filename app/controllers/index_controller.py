from app.controllers.controller import ControllerBase
from flask import render_template, flash

class IndexController(ControllerBase):
    @staticmethod
    def get():
        flash('Welcome to Project 3')
        return render_template('index.html')
