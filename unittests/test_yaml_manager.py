""" Unit test for the YAMLManager class. """

import unittest
from unittest.mock import mock_open, patch
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

    def test_set_new_file_path(self) -> None:
        """
        Testing the setting of a new YAML file.
        """
        file_path: str = "test.yaml"
        yaml_manager = YAMLManager(file_path, 10)
        self.assertEqual(file_path, yaml_manager.file_path)

        with self.assertRaises(TypeError, msg="Invalid file type!"):
            yaml_manager.file_path = 5

        with self.assertRaises(
            ValueError, msg="Missing 1 required positional argument: 'file_path'!"
        ):
            yaml_manager.file_path = ""

        file_path: str = "test.txt"
        with self.assertRaises(
            ValueError, msg=f"Invalid file type: {Path(file_path).suffix}!"
        ):
            yaml_manager.file_path = file_path

        file_path = "new_test.yaml"
        yaml_manager.file_path = file_path
        self.assertEqual(file_path, yaml_manager.file_path)

    def test_set_new_content_limit(self) -> None:
        """
        Testing the setting of the file content limit.
        """
        content_limit: int = 10
        yaml_manager = YAMLManager("test.yaml", 10)
        self.assertEqual(content_limit, yaml_manager.content_limit)

        with self.assertRaises(TypeError, msg="Invalid content limit type"):
            yaml_manager.content_limit = "5"

        content_limit = 10
        yaml_manager.content_limit = content_limit
        self.assertEqual(content_limit, yaml_manager.content_limit)

    def test_open_file(self) -> None:
        """
        Testing the opening of a YAML file.
        """
        file_path = "NonExistentingFilePath.yaml"
        content_limit: int = 10
        yaml_manager = YAMLManager(file_path, content_limit)
        with self.assertRaises(
            FileNotFoundError, msg=f"The file {file_path} was not found."
        ):
            yaml_manager.open_file()

        mock_file_content = ""
        file_path = "empty_file.yaml"
        yaml_manager = YAMLManager(file_path, content_limit)
        with patch(
            "builtins.open", mock_open(read_data=mock_file_content), create=True
        ) as mocked_file:
            file_list = yaml_manager.open_file()
            mocked_file.assert_called_once_with(file_path, "r", encoding="utf-8")
            self.assertIsInstance(file_list, dict)
            self.assertEqual(file_list, {})

        mock_file_content = "---\ntest1: 'test1'\ntest2: 'test2'\n"
        file_path = "file.yaml"
        yaml_manager = YAMLManager(file_path, content_limit)
        with patch(
            "builtins.open", mock_open(read_data=mock_file_content), create=True
        ) as mocked_file:
            file_list = yaml_manager.open_file()
            mocked_file.assert_called_once_with(file_path, "r", encoding="utf-8")
            self.assertIsInstance(file_list, dict)
            self.assertEqual(file_list, {"test1": "test1", "test2": "test2"})

    def test_update_user_settings(self) -> None:
        """
        Testing the updating user settings.
        """
        # TODO

    def test_update_file_paths(self) -> None:
        """
        Testing the updating file paths.
        """
        # TODO

    def test_dump_yaml_file(self) -> None:
        """
        Testing the dumping of new content into a yaml file.
        """
        # TODO


if __name__ == "__main__":
    unittest.main()
