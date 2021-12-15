"""Glossary Controller CLass"""
from flask import render_template
from app.controllers.controller import ControllerBase

class GlossaryController(ControllerBase):
    """Glossary from Project 2"""
    @staticmethod
    def get():
        """Displays the glossary"""
        return render_template('Glossary.html')