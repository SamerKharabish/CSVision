""" Defines the SignalFrameController class with the signal frame functionality. """

from typing import Any
from threading import Thread
from tkinter import filedialog
from PIL import Image
import customtkinter as ctk
from utils.helper_functions import find_root
from utils.threads import DataLoadingThread, DataExportingThread
from views.configurations_view import Config


class SignalFrameController:
    """
    Functionality of the signal frame view.
    """

    def __init__(self, view: ctk.CTkFrame) -> None:
        self.view: ctk.CTkFrame = view
        self.signal_frame_minimized: bool = (
            Config.General.SIGNAL_FRAME_MINIMIZED
        )  # Tracks the state of the signal frame

        self.view.toggle_side_bar_button.configure(command=self.on_toggle_side_bar)

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
        Toggle the visibility of the signal frame.
        Bound to the Ctrl + B press event.
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
        self.loading_thread: Thread = None

        self.view.root = find_root(self.view)

        self.view.open_file_button.configure(command=self.enter_file)
        self.view.export_to_excel.configure(command=self.export_file)

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
            self.view.file_entry.enter_file(filepath)

    def open_file(self, *_: Any) -> None:
        """
        Disable widgets and start loading data thread.
        """
        filepath = self.view.selected_file_path.get()

        self.loading_thread = DataLoadingThread(filepath, self.toggle_widgets)
        self.loading_thread.start()

    def export_file(self) -> None:
        """
        Disable widgets and start exporting data thread.
        """
        self.loading_thread = DataExportingThread(self.toggle_widgets)
        self.loading_thread.start()

    def toggle_widgets(self, state: str = "normal"):
        """
        Toggle the state of the widgets.

        Args:
            state (str, optional): The state to toggle to. Defaults to "normal".
        """
        self.view.root.after(10, lambda: self.view.file_entry.configure(state=state))
        self.view.root.after(
            10, lambda: self.view.open_file_button.configure(state=state)
        )
        self.view.root.after(
            10, lambda: self.view.export_to_excel.configure(state=state)
        )
