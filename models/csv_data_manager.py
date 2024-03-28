""" This module contains the CSVDataManager class which is responsible for handling the operations related
to reading and parsing CSV files. This includes loading data from a file, managing data frames, and providing
access to the data for visualization purposes. """

from pathlib import Path
import pandas as pd


class CSVDataManager:
    """
    Class for CSV file operations.
    """

    def __init__(self) -> None:
        self.__suffixes: tuple[str, ...] = (".csv", ".CSV")

        self._file_path: str
        self._raw_data_frame: pd.DataFrame = pd.DataFrame()

    @property
    def file_path(self) -> str:
        """
        Get the CSV file path.

        Returns:
            str: The set CSV file path.
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path: str) -> None:
        """
        Set the CSV file path.

        Args:
            file_path (str): The CSV file path to set.
        """
        if not isinstance(file_path, str):
            raise TypeError("Invalid file type!")
        elif file_path == "":
            raise ValueError("Missing 1 required positional argument: 'file_path'!")
        elif not file_path.endswith(self.__suffixes):
            raise ValueError(f"Invalid file type: {Path(file_path).suffix}!")
        else:
            self._file_path = file_path
            self._raw_data_frame = pd.DataFrame()

    @property
    def raw_data(self) -> pd.DataFrame | None:
        """
        Get the raw CSV data.

        Returns:
            pd.DataFrame: The read raw CSV data.
        """
        return self._raw_data_frame

    def open_file(self, file_path: str) -> None:
        """
        Open a CSV file and read the data.
        """
        self.file_path = file_path

        try:
            self._raw_data_frame = pd.read_csv(
                self.file_path, delimiter=";", quotechar="|"
            )
        except FileNotFoundError as exc:
            raise FileNotFoundError(
                f"The file {self.file_path} was not found!"
            ) from exc
        except pd.errors.EmptyDataError as exc:
            raise pd.errors.EmptyDataError(
                f"No columns to parse from file: {self.file_path}"
            ) from exc

csv_data_manager = CSVDataManager()
