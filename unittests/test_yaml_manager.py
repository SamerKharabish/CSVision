""" Unit test for the YAMLManager class. """

import unittest
from typing import List
import os
from pathlib import Path
from models.yaml_manager import YAMLManager


class TestYAMLManager(unittest.TestCase):
    """
    Test class for testing the YAMLManager class.
    """

    def setUp(self) -> None:
        # Initialize before each test
        pass

    def tearDown(self) -> None:
        # Deinitialize after each test
        pass

    def test_initilization(self) -> None:
        """
        Testing the initilization of the YAMLManager.
        """
        file_path = 0
        with self.assertRaises(TypeError, msg="Invalid file type"):
            YAMLManager(file_path)

        file_path = ""
        with self.assertRaises(
            ValueError, msg="Missing 1 required positional argument: 'file_path'"
        ):
            YAMLManager(file_path)

        file_path = "hello.txt"
        with self.assertRaises(
            ValueError, msg=f"Invalid file type: {Path(file_path).suffix}"
        ):
            YAMLManager(file_path)

        file_path = "file.yaml"
        yaml_manager = YAMLManager(file_path)
        self.assertEqual(file_path, yaml_manager.file_path)

    def test_open_yaml_file(self) -> None:
        """
        Testing the opening of a yaml file.
        """
        file_path = "NotExistingFilePath.yaml"
        yaml_manager = YAMLManager(file_path)
        with self.assertRaises(
            FileNotFoundError, msg=f"The file {file_path} was not found."
        ):
            yaml_manager.open_yaml_file()

        file_path = "unittests/empty_file.yaml"
        yaml_manager = YAMLManager(file_path)
        self.assertIsNone(yaml_manager.open_yaml_file(), None)

        file_path = "unittests/file.yaml"
        yaml_manager = YAMLManager(file_path)
        self.assertIsInstance(yaml_manager.open_yaml_file(), List)

    def test_dump_yaml_file(self) -> None:
        """
        Testing the opening of a yaml file.
        """
        file_path = "unittests/empty_file.yaml"
        check_file = os.stat(file_path).st_size

        if check_file != 0:
            open(file_path, "w", encoding="utf-8").close()

        yaml_manager = YAMLManager(file_path)
        yaml_manager.dump_yaml_file()

        check_file = os.stat(file_path).st_size
        self.assertNotEqual(check_file, 0)


if __name__ == "__main__":
    unittest.main()
