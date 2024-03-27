""" Defines the SignalFrameController class with the signal frame functionality. """

import os
from typing import Any
from tkinter import filedialog
from PIL import Image
import customtkinter as ctk
from utils.helper_functions import find_root
from utils.observer_publisher import SimplePublisher
from views.configurations_view import Config
from models.yaml_manager import YAMLManager


class SignalFrameController:
    """
    Functionality of the signal frame view.
    """

    def __init__(self, view: ctk.CTkFrame) -> None:
        self.view: ctk.CTkFrame = view
        self.signal_frame_minimized: bool = (
            Config.General.SIGNAL_FRAME_MINIMIZED
        )  # Tracks the state of the signal frame

        self.view.toggle_side_bar_button.configure(command=self.toggle_side_bar)

        self.view.root = find_root(self.view)
        self.initialize_controller()

    def initialize_controller(self) -> None:
        """
        Initialize controller.
        """
        self.file_handling_frame_controller = FileHandlingFrameController(
            self.view.filehandling_frame_view
        )

    def on_toggle_side_bar(self, _=None) -> None:
        """
        Bound to the Ctrl + B press event.
        """
        self.toggle_side_bar()

    def toggle_side_bar(self) -> None:
        """
        Toggle the visibility of the signal frame.
        """

        if self.signal_frame_minimized:
            self.hide_sidebar()
        else:
            self.show_sidebar()

    def hide_sidebar(self) -> None:
        """
        Hide the signal frame and update the toggle button image to indicate it can be shown.
        """
        self.view.root.after(
            0, self.view.signal_panel.pack(side="right", fill="y", expand=True)
        )
        self.view.root.after(
            0,
            self.view.toggle_side_bar_button.configure(
                image=ctk.CTkImage(
                    light_image=Image.open(
                        Config.ImageFormats.HIDE_SIDEPANEL_BUTTON_PNG
                    ),
                    size=(
                        Config.Dimensions.TOGGLE_SIDEPANEL_BUTTON_WIDTH_HEIGHT,
                        Config.Dimensions.TOGGLE_SIDEPANEL_BUTTON_WIDTH_HEIGHT,
                    ),
                )
            ),
        )
        self.signal_frame_minimized = False

    def show_sidebar(self) -> None:
        """
        Show the signal frame and update the toggle button image to indicate it can be hidden.
        """
        self.view.root.after(0, self.view.signal_panel.pack_forget())
        self.view.root.after(
            0,
            self.view.toggle_side_bar_button.configure(
                image=ctk.CTkImage(
                    light_image=Image.open(
                        Config.ImageFormats.SHOW_SIDEPANEL_BUTTON_PNG
                    ),
                    size=(
                        Config.Dimensions.TOGGLE_SIDEPANEL_BUTTON_WIDTH_HEIGHT,
                        Config.Dimensions.TOGGLE_SIDEPANEL_BUTTON_WIDTH_HEIGHT,
                    ),
                )
            ),
        )
        self.signal_frame_minimized = True


class FileHandlingFrameController:
    """
    Functionality of the file handling frame view.
    """

    def __init__(self, view: ctk.CTkFrame) -> None:
        self.view: ctk.CTkFrame = view

        self.view.open_file_button.configure(command=self.enter_file)

        self.file_manager: YAMLManager = YAMLManager("models/file_paths.yaml", 10)

        self.setup_tracings()

    def setup_tracings(self) -> None:
        """
        Tracing variables from the widgets.
        """
        self.view.selected_file_path.trace("w", self.open_file)

    def enter_file(self) -> None:
        """
        Open a filedialog and show the selected file path in the entry.
        """
        filetype = Config.Values.FILE_TYPE_TO_READ
        filepath = filedialog.askopenfilename(initialdir="/", filetypes=filetype)

        if filepath:
            self.view.file_entry.configure(state="normal")
            self.view.file_entry.delete(0, ctk.END)
            self.view.file_entry.insert(0, filepath.rsplit("/", 1)[1])
            self.view.file_entry.configure(state="readonly")

            self.view.selected_file_path.set(filepath)

    def open_file(self, *_: Any) -> None:
        """
        Safe file path in yaml file and publish the file size.
        """
        filepath = self.view.selected_file_path.get()

        self.file_manager.dump_yaml_file(filepath)

        file_size_publisher.file_size = round(os.path.getsize(filepath) / 1024)


class FileSizePublisher(SimplePublisher):
    """
    Monitor the file size.
    """

    def __init__(self):
        SimplePublisher.__init__(self)
        super(FileSizePublisher, self).__init__()
        self._file_size: str

    @property
    def file_size(self) -> str:
        """
        Get the file size.

        Returns:
            str: The set file size.
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size: str) -> None:
        """
        Set the file size.

        Args:
            file_size (str): The file size to set.
        """
        self._file_size = f"{file_size:,.0f} kB".replace(",", ".")
        self.notify()


file_size_publisher = FileSizePublisher()
