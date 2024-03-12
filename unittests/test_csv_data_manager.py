""" Unit test for the CSVDataManager class. """

import unittest
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
        file_path = "test.csv"
        csv_data_manager = CSVDataManager(file_path)
        self.assertEqual(file_path, csv_data_manager.file_path)
