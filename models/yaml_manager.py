""" Defines the YAMLManager class with functionalities to read, write, append,
    and update data in YAML files. """

from pathlib import Path
from typing import Dict
from datetime import datetime
import yaml


class YAMLManager:
    """
    Class for managing YAML files.
    """

    def __init__(self, file_path: str) -> None:
        self.file_path: str = file_path
        self._max_content: int = 10

    @property
    def max_content(self) -> int:
        """
        Get the maximum item length of the dictionary.

        Returns:
            str: Maximum item length of the dictionary.
        """
        return self._max_content

    @property
    def file_path(self) -> str:
        """
        Get the file path.

        Returns:
            str: File path of the YAML file.
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path: str) -> None:
        """
        Set the file path.

        Args:
            file_path (str): The file path to the YAML file.
        """
        if not isinstance(file_path, str):
            raise TypeError("Invalid file type")
        elif file_path == "":
            raise ValueError("Missing 1 required positional argument: 'file_path'")
        elif not file_path.endswith(".yaml") and not file_path.endswith(".yml"):
            raise ValueError(f"Invalid file type: {Path(file_path).suffix}")
        else:
            self._file_path = file_path

    def open_yaml_file(self) -> Dict:
        """
        Open the YAML file.

        Returns:
            List[dict]: Returns the content of the YAML file or None.
        """
        try:
            with open(self.file_path, "r", encoding="utf-8") as file_open:
                return yaml.safe_load(file_open) or {}
        except FileNotFoundError as exc:
            raise FileNotFoundError(
                f"The file {self.file_path} was not found."
            ) from exc

    def dump_yaml_file(self, new_content: str) -> None:
        """
        Updates the YAML file with new content.

        Args:
            new_content (str): Content to be added to the YAML file.
        """
        if not isinstance(new_content, str):
            raise ValueError("New content must be a string.")

        file_found = False

        try:
            old_content_dict = self.open_yaml_file()

            new_content_dict = {
                datetime.now().strftime("%d-%m-%Y %H:%M:%S,%f"): new_content
            }

            if old_content_dict:
                for date_time, file in old_content_dict.items():
                    if new_content == file:
                        file_found = True

                        del old_content_dict[date_time]

                        old_content_dict[
                            datetime.now().strftime("%d-%m-%Y %H:%M:%S,%f")
                        ] = new_content

                        break

                if not file_found:
                    if len(old_content_dict) >= self._max_content:
                        old_content_dict.pop(next(iter(old_content_dict)))
                    old_content_dict.update(new_content_dict)
            else:
                old_content_dict = new_content_dict

            with open(self.file_path, "w", encoding="utf-8") as file_dump:
                yaml.dump(old_content_dict, file_dump, default_flow_style=False)

        except FileNotFoundError as exc:
            raise FileNotFoundError(
                f"The file {self.file_path} was not found."
            ) from exc
