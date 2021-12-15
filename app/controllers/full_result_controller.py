"""Full Result Controller CLass"""
from flask import render_template
from app.controllers.controller import ControllerBase
from app.controllers.csvmanager.csv_controller import CSVController

class FullResultController(ControllerBase):
    """Get the whole history and puts it on a table form"""
    @staticmethod
    def get():
        """Displays the full csv output to the history table"""
        return render_template("full_results.html",
                               titles=CSVController.column_header(),
                               row_data=CSVController.read(), zip=zip)
