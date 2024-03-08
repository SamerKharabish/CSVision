""" Defines the SignalFrameController class with the signal frame functionality. """

import os
from tkinter import filedialog
from PIL import Image
import customtkinter as ctk
from utils.helper_functions import find_root, calculate_absolute_position
from views.configurations_view import Config
from models.yaml_manager import YAMLManager


class SignalFrameController:
    """
    Functionality of the signal frame.
    """

    def __init__(self, view: ctk.CTkFrame) -> None:
        self.view: ctk.CTkFrame = view
        self.view.root = find_root(self.view)
        self.signal_frame_minimized: bool = (
            Config.General.SIGNAL_FRAME_MINIMIZED
        )  # Tracks the state of the signal frame

        self.view.toggle_side_bar_button.configure(command=self.toggle_side_bar)
        self.view.filehandling_frame_view.open_file_button.configure(
            command=self.open_file
        )

        self.file_manager = YAMLManager("models/file_paths.yaml")

        self.setup_bindings()

    def setup_bindings(self) -> None:
        """
        Binding the AppController widgets to accessibility callback functions.
        """
        self.view.filehandling_frame_view.file_entry.bind(
            "<Button-1>", self.on_file_entry
        )

    def on_file_entry(self, _: None = None) -> None:
        """
        Creates and positions an file menu window relative to the file entry.
        """
        file_options_dict = self.file_manager.open_yaml_file()

        # Calculate the file entry's absolute position
        file_entry_x, file_entry_y = calculate_absolute_position(
            self.view.filehandling_frame_view.file_entry
        )

        # Calculate the new window's position
        new_window_x = self.view.root.winfo_rootx() + file_entry_x
        new_window_y = (
            self.view.root.winfo_rooty()
            + file_entry_y
            + self.view.filehandling_frame_view.file_entry.winfo_height()
        )

    def on_toggle_side_bar(self, _: None = None) -> None:
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

    def open_file(self) -> None:
        filetype = [("CSV", "*.csv*")]
        filepath = filedialog.askopenfilename(initialdir="/", filetypes=filetype)

        if filepath:
            self.file_manager.dump_yaml_file(filepath)
            filesize_kb = round(os.path.getsize(filepath) / 1024, 3)
            # TODO: show filesize in statusbar
            formatted_filesize = f"{filesize_kb:,.3f} KB".replace(",", ".")
            self.view.filehandling_frame_view.file_entry.configure(state="normal")
            self.view.filehandling_frame_view.file_entry.delete(0, ctk.END)
            self.view.filehandling_frame_view.file_entry.insert(
                0, filepath.rsplit("/", 1)[1]
            )
            self.view.filehandling_frame_view.file_entry.configure(state="readonly")
            print(f"File selected: {filepath}; size: {formatted_filesize}")
