""" Defines the SignalFrameController class with the signal frame functionality. """

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

    __slots__ = "__view", "__signal_frame_minimized"

    def __init__(self, view: ctk.CTkFrame) -> None:
        self.__view: ctk.CTkFrame = view
        self.__signal_frame_minimized: bool = (
            Config.General.SIGNAL_FRAME_MINIMIZED
        )  # Tracks the state of the signal frame

        self.__view.toggle_side_bar_button.configure(command=self.on_toggle_side_bar)

        self.__view.root = find_root(self.__view)
        self.__initialize_controller()

    def __initialize_controller(self) -> None:
        """
        Initialize controller.
        """
        FileHandlingFrameController(self.__view.filehandling_frame_view)
        SignalListFrameController(self.__view.signallist_frame_view)

    def on_toggle_side_bar(self, _=None) -> None:
        """
        Toggle the visibility of the signal frame.
        Bound to the Ctrl + B press event.
        """
        if self.__signal_frame_minimized:
            self.__hide_sidebar()
        else:
            self.__show_sidebar()

    def __hide_sidebar(self) -> None:
        """
        Hide the signal frame and update the toggle button image to indicate it can be shown.
        """
        self.__view.root.after(
            0, self.__view.signal_panel.pack(side="right", fill="y", expand=True)
        )
        self.__view.root.after(
            0,
            self.__view.toggle_side_bar_button.configure(
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
        self.__signal_frame_minimized = False

    def __show_sidebar(self) -> None:
        """
        Show the signal frame and update the toggle button image to indicate it can be hidden.
        """
        self.__view.root.after(0, self.__view.signal_panel.pack_forget())
        self.__view.root.after(
            0,
            self.__view.toggle_side_bar_button.configure(
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
        self.__signal_frame_minimized = True


class FileHandlingFrameController:
    """
    Functionality of the file handling frame view.
    """

    __slots__ = "__view", "__exporting_thread", "__loading_thread"

    def __init__(self, view: ctk.CTkFrame) -> None:
        self.__view: ctk.CTkFrame = view

        self.__view.root = find_root(self.__view)

        self.__exporting_thread: DataExportingThread = DataExportingThread(
            self.toggle_widgets
        )
        self.__loading_thread: DataLoadingThread = DataLoadingThread(
            self.toggle_widgets
        )

        self.__view.open_file_button.configure(command=self.__enter_file)
        self.__view.export_to_excel.configure(command=self.__exporting_thread.start)

        self.__setup_tracings()

    def __setup_tracings(self) -> None:
        """
        Tracing variables from the widgets.
        """
        self.__view.selected_file_path.trace("w", self.__open_file)

    def __enter_file(self) -> None:
        """
        Open a filedialog and show the selected file path in the entry.
        """
        filetype = Config.Values.FILE_TYPE_TO_READ
        filepath = filedialog.askopenfilename(initialdir="/", filetypes=filetype)

        if filepath:
            self.__view.file_entry.enter_file(filepath)

    def __open_file(self, *_: any) -> None:
        """
        Disable widgets and start loading data thread.
        """
        self.__loading_thread.file_path = self.__view.selected_file_path.get()
        self.__loading_thread.start()

    def toggle_widgets(self, state: str = "normal"):
        """
        Toggle the state of the widgets.

        Args:
            state (str, optional): The state to toggle to. Defaults to "normal".
        """
        self.__view.root.after(
            10, lambda: self.__view.file_entry.configure(state=state)
        )
        self.__view.root.after(
            10, lambda: self.__view.open_file_button.configure(state=state)
        )
        self.__view.root.after(
            10, lambda: self.__view.export_to_excel.configure(state=state)
        )
