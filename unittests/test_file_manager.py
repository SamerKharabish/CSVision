""" Unit test for the FileManager class. """

import unittest
from unittest.mock import mock_open, patch
from typing import Any, Tuple
from pathlib import Path
from models.file_manager import FileManager


class FakeFileManager(FileManager):
    """
    Class for managing YAML files.
    """

    def __init__(self, file_path: str, suffixes: Tuple[str, ...]) -> None:
        super().__init__(file_path=file_path, suffixes=suffixes)

    def open_file(self) -> Any | None:
        raise FileNotFoundError


class TestFileManager(unittest.TestCase):
    """
    Test class for testing the FileManager class.
    """

    def setUp(self) -> None:
        # Initialize before each test
        pass

    def tearDown(self) -> None:
        # Deinitialize after each test
        pass

    def test_initilization(self) -> None:
        """
        Testing the initilization of the FileManager.
        """

        suffixes: Tuple[str, ...] = (".yaml", ".yml")
        file_path: str = "test.yaml"
        file_manager = FakeFileManager(file_path, suffixes)
        self.assertEqual(file_path, file_manager.file_path)
        self.assertEqual(suffixes, file_manager.suffixes)

        suffixes = (".csv", ".CSV")
        file_path = "test.csv"
        file_manager = FakeFileManager(file_path, suffixes)
        self.assertEqual(file_path, file_manager.file_path)
        self.assertEqual(suffixes, file_manager.suffixes)

    def test_set_new_file_path(self) -> None:
        """
        Testing the setting of a new file.
        """
        suffixes = (".csv", ".CSV")
        file_path = "test.csv"
        file_manager = FakeFileManager(file_path, suffixes)

        with self.assertRaises(TypeError, msg="Invalid file type"):
            file_manager.file_path = 5

        with self.assertRaises(
            ValueError, msg="Missing 1 required positional argument: 'file_path'"
        ):
            file_manager.file_path = ""

        with self.assertRaises(
            ValueError, msg=f"Invalid file type: {Path(file_path).suffix}"
        ):
            file_manager.file_path = "test_new.txt"

    def test_open__file(self) -> None:
        """
        Testing the opening of a file.
        """
        suffixes: Tuple[str, ...] = ".txt"
        file_path = "NonExistentingFilePath.txt"
        file_manager = FakeFileManager(file_path, suffixes)
        with self.assertRaises(
            FileNotFoundError, msg=f"The file {file_path} was not found."
        ):
            file_manager.open_file()
