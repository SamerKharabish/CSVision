""" Defines the FileManager class with functionalities to operate with different file types. """

from pathlib import Path
from typing import Tuple, Optional, Any
from abc import ABC, abstractmethod


class FileManager(ABC):
    """
    Class for managing different file types.
    """

    def __init__(self, file_path: str, suffixes: Tuple[str, ...]) -> None:
        self.__suffixes: Tuple[str, ...] = suffixes
        self._file_path: str = None
        self.file_path = file_path

    @property
    def suffixes(self) -> Tuple[str, ...]:
        """
        Get the allowed file suffixes.

        Returns:
            str: The set file suffixes.
        """
        return self.__suffixes

    @property
    def file_path(self) -> str:
        """
        Get the file path.

        Returns:
            str: The set file path.
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path: str) -> None:
        """
        Set the file path.

        Args:
            file_path (str): The file path to set.
        """
        if not isinstance(file_path, str):
            raise TypeError("Invalid file type")
        elif file_path == "":
            raise ValueError("Missing 1 required positional argument: 'file_path'")
        elif not file_path.endswith(self.__suffixes):
            raise ValueError(f"Invalid file type: {Path(file_path).suffix}")
        else:
            self._file_path = file_path

    def _open_file(self) -> Optional[Any]:
        """
        Template method that defines the structure of the open file operation.
        """
        try:
            return self.open_file()
        except FileNotFoundError as exc:
            raise FileNotFoundError(
                f"The file {self.file_path} was not found."
            ) from exc

    @abstractmethod
    def open_file(self) -> Optional[Any]:
        """
        Subclass-specific implementation of file opening.
        """
