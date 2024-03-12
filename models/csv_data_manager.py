""" This module contains the CSVDataManager class which is responsible for handling the operations related
to reading and parsing CSV files. This includes loading data from a file, managing data frames, and providing
access to the data for visualization purposes. """


class CSVDataManager:
    """
    Class for CSV file operations.
    """

    def __init__(self, file_path: str) -> None:
        self.file_path: str = file_path

    @property
    def file_path(self) -> str:
        """
        Get the file path.

        Returns:
            str: File path of the CSV file.
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path: str) -> None:
        """
        Set the file path.

        Args:
            file_path (str): The file path to the CSV file.
        """
        if not isinstance(file_path, str):
            raise TypeError("Invalid file type")
        elif file_path == "":
            raise ValueError("Missing 1 required positional argument: 'file_path'")
        else:
            self._file_path = file_path
