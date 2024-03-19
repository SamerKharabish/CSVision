""" Defines the YAMLManager class with functionalities to read, write, append,
    and update data in YAML files. """

from pathlib import Path
from typing import Dict, Tuple
from datetime import datetime
import yaml


class YAMLManager:
    """
    Class for managing YAML files.
    """

    def __init__(self, file_path: str, content_limit: int) -> None:
        self.__suffixes: Tuple[str, ...] = (".yaml", ".yml")

        self._file_path: str = None
        self.file_path = file_path

        self._content_limit: int = content_limit
        self.content_limit = content_limit

    @property
    def file_path(self) -> str:
        """
        Get the YAML file path.

        Returns:
            str: The set YAML file path.
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path: str) -> None:
        """
        Set the YAML file path.

        Args:
            file_path (str): The YAML file path to set.
        """
        if not isinstance(file_path, str):
            raise TypeError("Invalid file type!")
        elif file_path == "":
            raise ValueError("Missing 1 required positional argument: 'file_path'!")
        elif not file_path.endswith(self.__suffixes):
            raise ValueError(f"Invalid file type: {Path(file_path).suffix}!")
        else:
            self._file_path = file_path

    @property
    def content_limit(self) -> int:
        """
        Get the maximum length of the content.

        Returns:
            int: Maximum content length of the YAML file.
        """
        return self._content_limit

    @content_limit.setter
    def content_limit(self, content_limit: int) -> None:
        """
        Set the file content limit.

        Args:
            content_limit (int): The content limit to set.
        """
        if not isinstance(content_limit, int):
            raise TypeError("Invalid content limit type!")
        else:
            self._content_limit = content_limit

    def open_file(self) -> Dict:
        """
        Open a YAML file.

        Returns:
            Dict: Returns the content of the YAML file or an empty dictionary.
        """
        try:
            with open(self.file_path, "r", encoding="utf-8") as file_open:
                return yaml.safe_load(file_open) or {}
        except FileNotFoundError as exc:
            raise FileNotFoundError(
                f"The file {self.file_path} was not found!"
            ) from exc

    def dump_yaml_file(self, new_content: str) -> None:
        """
        Updates a YAML file with new content.

        Args:
            new_content (str): Content to be added to the YAML file.
        """
        if not isinstance(new_content, str):
            raise ValueError("New content must be a string!")

        try:
            old_content_dict = self.open_file()

            new_content_dict = {
                datetime.now().strftime("%d-%m-%Y %H:%M:%S,%f"): new_content
            }

            if old_content_dict:
                file_found = False
                for date_time, file in old_content_dict.items():
                    if new_content == file:
                        file_found = True

                        del old_content_dict[date_time]

                        old_content_dict[
                            datetime.now().strftime("%d-%m-%Y %H:%M:%S,%f")
                        ] = new_content

                        break

                if not file_found:
                    if len(old_content_dict) >= self.content_limit:
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
