""" Defines the YAMLManager class with functionalities to read, write, append,
    and update data in YAML files. """

from pathlib import Path
from typing import List
import yaml


class YAMLManager:
    """
    Class for managing YAML files.
    """

    def __init__(self, file_path: str) -> None:
        if not isinstance(file_path, str):
            raise TypeError("Invalid file type")
        elif file_path == "":
            raise ValueError("Missing 1 required positional argument: 'file_path'")
        elif not file_path.endswith(".yaml") and not file_path.endswith(".yml"):
            raise ValueError(f"Invalid file type: {Path(file_path).suffix}")
        else:
            self._file_path: str = file_path

    @property
    def file_path(self) -> str:
        """
        Get the file path.

        Returns:
            str: File path of the YAML file
        """
        return self._file_path

    def open_yaml_file(self) -> List[dict]:
        """
        Open the YAML file.

        Raises:
            FileNotFoundError: If the file path is not found.

        Returns:
            List[dict]: Returns the content of the YAML file or None.
        """
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return yaml.safe_load(file)
        except FileNotFoundError as exc:
            raise FileNotFoundError(
                f"The file {self.file_path} was not found."
            ) from exc

    def dump_yaml_file(self) -> List[dict]:
        pass
