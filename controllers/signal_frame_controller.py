""" Defines the SignalFrameController class with the signal frame functionality. """

import os
from tkinter import filedialog
from PIL import Image
import customtkinter as ctk
from utils.helper_functions import find_root
from views.configurations_view import Config


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
            filesize_kb = round(os.path.getsize(filepath) / 1024, 3)
            formatted_filesize = f"{filesize_kb:,.3f} KB".replace(",", ".")
            self.view.filehandling_frame_view.file_entry.delete(0, ctk.END)
            self.view.filehandling_frame_view.file_entry.insert(
                0, filepath.rsplit("/", 1)[1]
            )
            print(f"File selected: {filepath}; size: {formatted_filesize}")
