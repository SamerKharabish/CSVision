"""Defines the FileHandlerController class with the filehandler functionality."""

import os
from tkinter import filedialog, messagebox
import pandas as pd
from models.yaml_manager import YAMLManager
from models.csv_data_manager import csv_data_manager
from configurations.filehandler_config import FileHandlerConfig
from views.sidebar_views.filehandler_view import FileHandlerView
from utils.threads import safe_thread_queue
from utils.observer_publisher import (
    file_state_publisher,
    ProgressStatePublisher,
    progress_state_publisher,
)


class FileHandlerController:
    """
    Functionality of the filehandler.
    """

    __slots__ = ("view", "file_manager")

    def __init__(self, view: FileHandlerView) -> None:
        self.view: FileHandlerView = view

        self.view.open_file_button.configure(command=self.enter_file)
        self.view.export_to_excel_button.configure(
            command=self.start_export_file_thread
        )

        self.file_manager: YAMLManager = YAMLManager(
            FileHandlerConfig.OwnArgs.FILE_PATHS,
            FileHandlerConfig.OwnArgs.NR_OF_FILES_TO_SAVE,
        )

        self.setup_tracings()

    def setup_tracings(self) -> None:
        """
        Tracing variables from the widgets.
        """
        self.view.selected_file_path.trace_add("write", self.start_open_file_thread)

    def enter_file(self) -> None:
        """
        Open a filedialog and show the selected file path in the entry.
        """
        filepath = filedialog.askopenfilename(
            initialdir=FileHandlerConfig.OwnArgs.FILE_PATHS_INITIAL_DIR,
            filetypes=FileHandlerConfig.OwnArgs.FILE_PATHS_FILE_TYPE,
        )

        if filepath:
            self.view.file_entry.enter_file(filepath)

    def start_open_file_thread(self, *_) -> None:
        """
        Start open file thread.
        """
        safe_thread_queue.add_task(
            self.open_file,
            args=(self.view.selected_file_path.get(),),
            before_thread=self.pre_open_file,
            after_thread=self.post_operation_file,
        )

    def start_export_file_thread(self) -> None:
        """
        Start exporting data thread.
        """
        safe_thread_queue.add_task(
            self.export_file,
            args=(self.view.selected_file_path.get(),),
            before_thread=self.pre_operation_file,
            after_thread=self.post_operation_file,
        )

    def pre_open_file(self) -> None:
        """
        Before doing an open file operation.
        """
        file_state_publisher.set_is_open(False)
        self.pre_operation_file()

    def pre_operation_file(self) -> None:
        """
        Before doing an operation to the csv file start the progressbar.
        """
        progress_state_publisher.mode = "indeterminate"
        progress_state_publisher.set_value(ProgressStatePublisher.START_PROGRESSBAR)

    def post_operation_file(self) -> None:
        """
        After doing an operation to the csv file stop the progressbar.
        """
        progress_state_publisher.set_value(ProgressStatePublisher.STOP_PROGRESSBAR)

    def open_file(self, file_name: str) -> None:
        """
        Open a CSV file and read the data.

        Args:
            file_name (str): The CSV file path.
        """
        try:
            csv_data_manager.read_file(file_name)
        except FileNotFoundError as exc:
            file_state_publisher.set_is_open(False)
            messagebox.showerror("Error", str(exc))
        except pd.errors.EmptyDataError as exc:
            file_state_publisher.set_is_open(False)
            messagebox.showerror("Error", str(exc))
        else:
            self.file_manager.dump_yaml_file(file_name)
            file_state_publisher.file_size = str(
                round(os.path.getsize(file_name) / 1024)
            )
            file_state_publisher.set_is_open(True)

    def export_file(self, file_name: str) -> None:
        """
        Export a CSV file.

        Args:
            file_name (str): The CSV file path.
        """
        try:
            csv_data_manager.export_to_excel(file_name)
        except AttributeError as exc:
            messagebox.showerror("Error", str(exc))
        except pd.errors.EmptyDataError as exc:
            messagebox.showerror("Error", str(exc))
        except ValueError as exc:
            messagebox.showerror("Error", str(exc))
