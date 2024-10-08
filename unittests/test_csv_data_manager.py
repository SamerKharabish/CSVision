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

        for attr in CSVDataManager.__slots__:
            if not attr.startswith("_CSVDataManager__") and not attr.startswith(
                "_raw_data_frame"
            ):
                with self.subTest(attr=attr):
                    self.assertIsNone(
                        getattr(csv_data_manager, attr, None), f"{attr} is not None"
                    )

        self.assertTrue(csv_data_manager.raw_data.empty)

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
        self.assertTrue(csv_data_manager.raw_data.empty)

        file_path = "new_test1.csv"
        csv_data_manager.file_path = file_path
        self.assertEqual(file_path, csv_data_manager.file_path)
        self.assertTrue(csv_data_manager.raw_data.empty)

    def test_open_csv_file(self) -> None:
        """
        Testing the opening of a CSV file.
        """
        file_path = "NonExistentingFilePath.csv"
        yaml_manager = CSVDataManager()
        with self.assertRaises(
            FileNotFoundError, msg=f"The file {file_path} was not found."
        ):
            yaml_manager.read_file(file_path)

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
                csv_data_manager.read_file(file_path)

        mock_file_content = "time_index;value\n10;20\n"
        file_path = "file.csv"
        csv_data_manager = CSVDataManager()
        with patch(
            "builtins.open", mock_open(read_data=mock_file_content), create=True
        ):
            csv_data_manager.read_file(file_path)
            self.assertEqual("time_index", csv_data_manager.raw_data.columns[0])
            self.assertEqual("value", csv_data_manager.raw_data.columns[1])
            self.assertEqual(10, csv_data_manager.raw_data["time_index"][0])
            self.assertEqual(20, csv_data_manager.raw_data["value"][0])

    def test_get_header_list(self) -> None:
        """
        Testing the getter function for the header list..
        """
        mock_file_content = "heading1::subheading1;heading2::subheading2"
        csv_data_manager = CSVDataManager()
        with patch(
            "builtins.open", mock_open(read_data=mock_file_content), create=True
        ):
            csv_data_manager.read_file("file.csv")
            self.assertEqual(
                ["heading1::subheading1", "heading2::subheading2"],
                csv_data_manager.get_header_list(),
            )

        mock_file_content = "asdf_heading1::subheading1;asdf_heading2::subheading2"
        with patch(
            "builtins.open", mock_open(read_data=mock_file_content), create=True
        ):
            csv_data_manager.read_file("file.csv")
            self.assertEqual(
                ["heading1::subheading1", "heading2::subheading2"],
                csv_data_manager.get_header_list("asdf_"),
            )

        mock_file_content = "heading1::subheading1_asdf;heading2::subheading2_asdf"
        with patch(
            "builtins.open", mock_open(read_data=mock_file_content), create=True
        ):
            csv_data_manager.read_file("file.csv")
            self.assertEqual(
                ["heading1::subheading1", "heading2::subheading2"],
                csv_data_manager.get_header_list(postfix="_asdf"),
            )

        mock_file_content = (
            "asdf_heading1::subheading1_asdf;asdf_heading2::subheading2_asdf"
        )
        with patch(
            "builtins.open", mock_open(read_data=mock_file_content), create=True
        ):
            csv_data_manager.read_file("file.csv")
            self.assertEqual(
                ["heading1::subheading1", "heading2::subheading2"],
                csv_data_manager.get_header_list("asdf_", "_asdf"),
            )


if __name__ == "__main__":
    unittest.main()
