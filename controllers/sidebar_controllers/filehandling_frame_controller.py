""" Defines the FileHandlingFrameController class with the file handling frame functionality. """

from tkinter import filedialog
from views.configurations_view import Config
from views.sidebar_views.filehandling_frame_view import FileHandlingFrameView
from utils.helper_functions import find_root
from utils.threads import DataLoadingThread, DataExportingThread


class FileHandlingFrameController:
    """
    Functionality of the file handling frame view.
    """

    __slots__ = ("__view",)

    def __init__(self, view: FileHandlingFrameView) -> None:
        self.__view: FileHandlingFrameView = view

        self.__view.root = find_root(self.__view)

        self.__view.open_file_button.configure(command=self.__enter_file)
        self.__view.export_to_excel.configure(command=self.__export_file)

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
        loading_thread: DataLoadingThread = DataLoadingThread(
            self.__view.selected_file_path.get(), self.toggle_widgets
        )
        loading_thread.start()

    def __export_file(self) -> None:
        """
        Disable widgets and start exporting data thread.
        """
        self.toggle_widgets("disabled")

        exporting_thread: DataExportingThread = DataExportingThread(self.toggle_widgets)
        exporting_thread.start()

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
