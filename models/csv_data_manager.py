""" This module contains the CSVDataManager class which is responsible for handling the operations related
to reading and parsing CSV files. This includes loading data from a file, managing data frames, and providing
access to the data for visualization purposes. """


import pandas as pd
from models.file_manager import FileManager


class CSVDataManager(FileManager):
    """
    Class for CSV file operations.
    """

    def __init__(self, file_path: str) -> None:
        super().__init__(file_path, (".csv", ".CSV"))

    def open_file(self) -> pd.DataFrame:
        """
        Open the CSV file.

        Returns:
            pd.DataFrame: Returns the content of the CSV file.
        """
        try:
            return pd.read_csv(self.file_path, delimiter=";", quotechar="|")
        except pd.errors.EmptyDataError as exc:
            raise pd.errors.EmptyDataError(
                f"No columns to parse from file: {self.file_path}"
            ) from exc
