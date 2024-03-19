""" Unit test for the CSVDataManager class. """

import unittest
from unittest.mock import mock_open, patch
from pathlib import Path
import pandas as pd
from models.csv_data_manager import CSVDataManager


class TestCSVDataManager(unittest.TestCase):
    """
    Test class for testing the CSVDataManager class.
    """

    def setUp(self) -> None:
        # Initialize before each test
        pass

    def tearDown(self) -> None:
        # Deinitialize after each test
        pass

    def test_initilization(self) -> None:
        """
        Testing the initilization of the CSVDataManager.
        """
        csv_data_manager = CSVDataManager()

        for attr, value in vars(csv_data_manager).items():
            if not attr.startswith("_CSVDataManager__"):
                with self.subTest(attr=attr):
                    self.assertIsNone(value, f"{attr} is not None")

    def test_set_new_file_path(self) -> None:
        """
        Testing the setting of a new CSV file.
        """
        csv_data_manager = CSVDataManager()

        with self.assertRaises(TypeError, msg="Invalid file type!"):
            csv_data_manager.file_path = 5

        with self.assertRaises(
            ValueError, msg="Missing 1 required positional argument: 'file_path'!"
        ):
            csv_data_manager.file_path = ""

        file_path: str = "test.txt"
        with self.assertRaises(
            ValueError, msg=f"Invalid file type: {Path(file_path).suffix}!"
        ):
            csv_data_manager.file_path = file_path

        file_path = "new_test.csv"
        csv_data_manager.file_path = file_path
        self.assertEqual(file_path, csv_data_manager.file_path)

    def test_open_csv_file(self) -> None:
        """
        Testing the opening of a CSV file.
        """
        file_path = "NonExistentingFilePath.csv"
        yaml_manager = CSVDataManager()
        with self.assertRaises(
            FileNotFoundError, msg=f"The file {file_path} was not found."
        ):
            yaml_manager.open_file(file_path)

        mock_file_content = ""
        file_path = "empty_file.csv"
        csv_data_manager = CSVDataManager()
        with patch(
            "builtins.open", mock_open(read_data=mock_file_content), create=True
        ):
            with self.assertRaises(
                pd.errors.EmptyDataError,
                msg=f"No columns to parse from file: {file_path}",
            ):
                csv_data_manager.open_file(file_path)

        mock_file_content = "time_index;value\n10;20\n"
        file_path = "file.csv"
        csv_data_manager = CSVDataManager()
        with patch(
            "builtins.open", mock_open(read_data=mock_file_content), create=True
        ):
            csv_data_manager.open_file(file_path)
            self.assertEqual("time_index", csv_data_manager.raw_data.columns[0])
            self.assertEqual("value", csv_data_manager.raw_data.columns[1])
            self.assertEqual(10, csv_data_manager.raw_data["time_index"][0])
            self.assertEqual(20, csv_data_manager.raw_data["value"][0])


if __name__ == "__main__":
    unittest.main()
