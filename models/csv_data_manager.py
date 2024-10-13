""" This module contains the CSVDataManager class which is responsible for handling the operations related
to reading and parsing CSV files. This includes loading data from a file, managing data frames, and providing
access to the data for visualization purposes. """

from pathlib import Path
from collections import defaultdict
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

    def get_raw_data_columns_count(self) -> int:
        """
        Get the number of columns from the CSV file.

        Returns:
            int: The number of columns from the CSV file.
        """
        return len(self.__raw_data_frame.columns)

    def get_classified_headers(
        self,
        exclude_index: int,
        prefix: str = None,
        postfix: str = None,
        separator: str = "",
        order: bool = True,
    ) -> defaultdict[str, list[int] | list[tuple[str, int]]]:
        """
        Classify the headers from the CSV file based on their values, excluding one specified column by index.

        Classification codes:
            0 - 'not constant'
            1 - 'constant at exactly zero'
            2 - 'constant at a value different from zero'

        Args:
            exclude_index (int): Index of the column to exclude from classification.
            prefix (str, optional): The prefix of the header of the column. Defaults to None.
            postfix (str, optional): The postfix of the header of the column. Defaults to None.
            separator (str, optional): Separator to divide the header of the column into two substrings.
                                        Defaults to "".
            order (bool, optional): Indicator of which of the substrings will be the key and which part of the value.
                                                If True, then the first half will be the key else the second half. Defaults to True.

        Returns:
            defaultdict[str, list[str] | list[str, int]]: A dictionary with the header of the column or a substring of it as
                                                            keys and a list of their classification or a tuple of the other
                                                            substring and its classification as values.
        """
        # Determine the columns to process, excluding the specified index
        columns_to_process = self.raw_data.columns.tolist()
        columns_to_process = (
            columns_to_process[:exclude_index] + columns_to_process[exclude_index + 1 :]
        )

        # Vectorized classification using efficient operations
        column_classification: defaultdict[str, list[int] | list[tuple[str, int]]] = (
            defaultdict(list)
        )

        raw_data_copy = self.raw_data.copy()

        for column in columns_to_process:
            unique_values = raw_data_copy[column].unique()

            column_modified = search_substring(column, prefix, postfix)

            if separator != "":
                if order:
                    column_first_half, column_second_half = column_modified.split(
                        separator
                    )
                else:
                    column_second_half, column_first_half = column_modified.split(
                        separator
                    )

                column_first_half = column_first_half.strip()
                column_second_half = column_second_half.strip()
            else:
                column_first_half = column_modified

            classification = (
                0 if len(unique_values) > 1 else 1 if unique_values[0] == 0 else 2
            )

            if separator != "":
                column_classification[column_first_half.strip()].append(
                    (column_second_half.strip(), classification)
                )
            else:
                column_classification[column_modified].append(classification)

        return column_classification

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
