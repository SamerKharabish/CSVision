""" This module contains the CSVDataManager class which is responsible for handling the operations related
to reading and parsing CSV files. This includes loading data from a file, managing data frames, and providing
access to the data for visualization purposes. """


from models.file_manager import FileManager


class CSVDataManager(FileManager):
    """
    Class for CSV file operations.
    """

    def __init__(self, file_path: str) -> None:
        super().__init__(file_path, (".csv", ".CSV"))