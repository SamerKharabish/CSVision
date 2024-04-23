""" Defines all thread classes. """

import os
from threading import Thread
from tkinter import messagebox
import pandas as pd
from utils.observer_publisher import progress_publisher, file_size_publisher
from models.yaml_manager import YAMLManager
from models.csv_data_manager import csv_data_manager

class DataLoadingThread(Thread):
    """
    Handle the data loading thread.
    """

    def __init__(self, toggle_callback: callable) -> None:
        super().__init__()

        self.daemon = True

        self.toggle_callback: callable = toggle_callback

        self._file_path: str
        self.file_manager: YAMLManager = YAMLManager("models/file_paths.yaml", 10)

    @property
    def file_path(self) -> str:
        """
        Get the CSV file path.

        Returns:
            str: The set CSV file path.
        """
        return self._file_path

    @file_path.setter
    def file_path(self, file_path: str) -> None:
        """
        Set the CSV file path.

        Args:
            file_path (str): The CSV file path to set.
        """
        self._file_path = file_path

    def run(self) -> None:
        progress_publisher.progress = "indeterminate"
        try:
            self.toggle_callback("disabled")
            csv_data_manager.open_file(self.file_path)
            self.file_manager.dump_yaml_file(self.file_path)
            file_size_publisher.file_size = round(
                os.path.getsize(self.file_path) / 1024
            )
        except FileNotFoundError as exc:
            file_size_publisher.file_size = None
            messagebox.showerror("Error", exc)
        except pd.errors.EmptyDataError as exc:
            file_size_publisher.file_size = None
            messagebox.showerror("Error", exc)
        progress_publisher.progress = "stop"
        self.toggle_callback()


class DataExportingThread(Thread):
    """
    Handle the data exporting thread.
    """

    def __init__(self, toogle_callback: callable) -> None:
        super().__init__()

        self.daemon = True

        self.toggle_callback: callable = toogle_callback

    def run(self) -> None:
        progress_publisher.progress = "indeterminate"
        try:
            self.toggle_callback("disabled")
            csv_data_manager.export_to_excel(csv_data_manager.file_path)
        except AttributeError:
            pass
        except pd.errors.EmptyDataError:
            pass
        progress_publisher.progress = "stop"
        self.toggle_callback()
