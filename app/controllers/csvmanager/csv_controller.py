"""CSV Controller Class"""
# pylint: disable=(no-member)
from pathlib import Path
import pandas as pd

class CSVController:
    """This class takes care of the both reading from and writing to the csv file"""
    @staticmethod
    def csv_directory():
        """Sets the path for the csv file"""
        return str(Path(__file__).parent.absolute()) + '/output/history.csv'
    @staticmethod
    def write(value1, value2, operation, result):
        """Writes to the csv file"""
        data_frame = pd.read_csv(CSVController.csv_directory())
        data_frame.loc[len(data_frame.index)] = [value1, value2, operation, result]
        data_frame.to_csv(CSVController.csv_directory(), index=False)
    @staticmethod
    def read():
        """Reads from the csv file"""
        data_frame = pd.read_csv(CSVController.csv_directory())
        return list(data_frame.values.tolist())

    @staticmethod
    def column_header():
        """Reads the csv file to get the column titles for the table"""
        data_frame = pd.read_csv(CSVController.csv_directory())
        return data_frame.columns.values
