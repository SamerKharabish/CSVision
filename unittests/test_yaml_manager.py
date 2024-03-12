""" Unit test for the YAMLManager class. """

import unittest
from typing import Dict
import os
from models.yaml_manager import YAMLManager


class TestYAMLManager(unittest.TestCase):
    """
    Test class for testing the YAMLManager class.
    """

    def setUp(self) -> None:
        # Initialize before each test
        file_path = "unittests/empty_file.yaml"
        check_file = os.stat(file_path).st_size

        if check_file != 0:
            open(file_path, "w", encoding="utf-8").close()

    def tearDown(self) -> None:
        # Deinitialize after each test
        pass

    def test_initilization(self) -> None:
        """
        Testing the initilization of the YAMLManager.
        """
        file_path = "test.yaml"
        yaml_manager = YAMLManager(file_path)
        self.assertEqual(file_path, yaml_manager.file_path)

    def test_set_new_file_path(self) -> None:
        """
        Testing the setting of a new YAML file.
        """
        file_path = "test.yaml"
        yaml_manager = YAMLManager(file_path)
        self.assertEqual(file_path, yaml_manager.file_path)

        file_path = "test_new.yaml"
        yaml_manager.file_path = file_path
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
        self.assertEqual(yaml_manager.open_yaml_file(), {})

        file_path = "unittests/file.yaml"
        yaml_manager = YAMLManager(file_path)
        file_list = yaml_manager.open_yaml_file()
        self.assertIsInstance(file_list, Dict)

    def test_dump_yaml_file(self) -> None:
        """
        Testing the opening of a yaml file.
        """
        file_path = "unittests/empty_file.yaml"

        yaml_manager = YAMLManager(file_path)
        yaml_manager.dump_yaml_file("test0.csv")

        check_file_size_not_zero = os.stat(file_path).st_size
        self.assertNotEqual(check_file_size_not_zero, 0)

        yaml_manager = YAMLManager(file_path)
        yaml_manager.dump_yaml_file("test1.csv")

        check_file_size_double = os.stat(file_path).st_size
        self.assertEqual(check_file_size_double, check_file_size_not_zero * 2)

        yaml_manager = YAMLManager(file_path)
        yaml_manager.dump_yaml_file("test1.csv")

        check_file_size_double = os.stat(file_path).st_size
        self.assertEqual(check_file_size_double, check_file_size_not_zero * 2)

        yaml_manager.dump_yaml_file("test2.csv")
        yaml_manager.dump_yaml_file("test3.csv")
        yaml_manager.dump_yaml_file("test4.csv")
        yaml_manager.dump_yaml_file("test5.csv")
        yaml_manager.dump_yaml_file("test6.csv")
        yaml_manager.dump_yaml_file("test7.csv")
        yaml_manager.dump_yaml_file("test8.csv")
        yaml_manager.dump_yaml_file("test9.csv")
        yaml_manager.dump_yaml_file("test10.csv")
        yaml_manager.dump_yaml_file("test11.csv")

        check_file_size_double = os.stat(file_path).st_size
        self.assertEqual(
            len(yaml_manager.open_yaml_file()),
            yaml_manager.max_content,
        )

        yaml_manager = YAMLManager(file_path)
        with self.assertRaises(ValueError, msg="New content must be a string."):
            yaml_manager.dump_yaml_file(0)


if __name__ == "__main__":
    unittest.main()
