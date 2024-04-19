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

    def __init__(self, filename: str, toggle_callback: callable) -> None:
        super().__init__()

        self.daemon = True

        self.toggle_callback: callable = toggle_callback

        self.filename: str = filename
        self.file_manager: YAMLManager = YAMLManager("models/file_paths.yaml", 10)

    def run(self) -> None:
        progress_publisher.progress = "indeterminate"
        try:
            csv_data_manager.open_file(self.filename)
            self.file_manager.dump_yaml_file(self.filename)
            file_size_publisher.file_size = round(os.path.getsize(self.filename) / 1024)
            self.toggle_callback("disabled")
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
            csv_data_manager.export_to_excel(csv_data_manager.file_path)
            self.toggle_callback("disabled")
        except AttributeError:
            pass
        except pd.errors.EmptyDataError:
            pass
        progress_publisher.progress = "stop"
        self.toggle_callback()
