""" This module contains the CSVDataManager class which is responsible for handling the operations related
to reading and parsing CSV files. This includes loading data from a file, managing data frames, and providing
access to the data for visualization purposes. """

from pathlib import Path
import pandas as pd
from utils.helper_functions import search_substring


class CSVDataManager:
    """
    Class for CSV file operations.
    """

    __slots__ = "__suffixes", "__file_path", "__raw_data_frame"

    def __init__(self) -> None:
        self.__suffixes: tuple[str, ...] = (".csv", ".CSV")

        self.__file_path: str
        self.__raw_data_frame: pd.DataFrame = pd.DataFrame()

    @property
    def file_path(self) -> str:
        """
        Get the CSV file path.

        Returns:
            str: The set CSV file path.
        """
        return self.__file_path

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
            try:
                if self.__file_path != file_path:
                    self.__file_path = file_path
                    self.__raw_data_frame = pd.DataFrame()
            except AttributeError:
                self.__file_path = file_path

    @property
    def raw_data(self) -> pd.DataFrame | None:
        """
        Get the raw CSV data.

        Returns:
            pd.DataFrame: The read raw CSV data.
        """
        return self.__raw_data_frame

    def get_header_list(self, prefix: str = None, postfix: str = None) -> list[str]:
        """
        Get the list of headers from the CSV file without prefix or postfix.

        Args:
            prefix (str, optional): The prefix of the header. Defaults to None.
            postfix (str, optional): The postfix of the header. Defaults to None.

        Returns:
            list[str]: The reduced header list.
        """
        headers = self.raw_data.columns.tolist()
        header_list = []

        if prefix or postfix:
            for header in headers:
                header_list.append(search_substring(header, prefix, postfix))
        else:
            header_list = headers

        return header_list

    def read_file(self, file_path: str) -> None:
        """
        Open a CSV file and read the data.

        Args:
            file_path (str): The CSV file path.

        Raises:
            FileNotFoundError: If the file was not found.
            pd.errors.EmptyDataError: If the file is empty.
        """
        self.file_path = file_path

        try:
            self.__raw_data_frame = pd.read_csv(
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

    def export_to_excel(self, file_path: str) -> None:
        """
        Export CSV data to an excel file.

        Args:
            file_path (str): The CSV file path.

        Raises:
            pd.errors.EmptyDataError: If the file is empty.
        """
        self.file_path = file_path

        if not self.__raw_data_frame.empty:
            self.__raw_data_frame.to_excel(
                self.file_path.replace(".csv", ".xlsx"),
                engine="xlsxwriter",
                index=False,
            )
        else:
            raise pd.errors.EmptyDataError(
                f"No columns to parse from file: {self.file_path}"
            )


csv_data_manager = CSVDataManager()
