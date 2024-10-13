"""Defines the FileHandlerView class with the filehandler layout."""

from __future__ import annotations
from typing import TYPE_CHECKING
from PIL import Image
import customtkinter as ctk
from configurations.filehandler_config import FileHandlerConfig
from utils.helper_functions import find_root
from utils.input_entry_list import InputEntryList

if TYPE_CHECKING:
    from sidebar_view import SidebarView


class FileHandlerView(ctk.CTkFrame):
    """
    Layout of the filehandler.
    """

    __slots__ = (
        "root",
        "title_frame",
        "title_label",
        "open_file_button",
        "export_to_excel_button",
        "selected_file_path",
        "file_entry",
    )

    def __init__(self, master: SidebarView) -> None:
        super().__init__(
            master,
            corner_radius=FileHandlerConfig.OwnArgs.CORNER_RADIUS,
            border_width=FileHandlerConfig.OwnArgs.BORDER_WIDTH,
            fg_color=FileHandlerConfig.OwnArgs.TRANSPARENT,
        )

        self.root = find_root(self)

        self.initialize_widgets()
        self.create_layout()

    def initialize_widgets(self) -> None:
        """
        Initialize widgets.
        """
        self.title_label: ctk.CTkLabel = ctk.CTkLabel(
            self,
            text=FileHandlerConfig.Widgets.TITLE_LABEL["text"], # type: ignore
            font=ctk.CTkFont(
                family=FileHandlerConfig.Widgets.TITLE_LABEL["family"], # type: ignore
                size=FileHandlerConfig.Widgets.TITLE_LABEL["size"], # type: ignore
                weight=FileHandlerConfig.Widgets.TITLE_LABEL["weight"], # type: ignore
            ),
            anchor=FileHandlerConfig.Widgets.TITLE_LABEL["anchor"], # type: ignore
        )

        self.open_file_button: ctk.CTkButton = ctk.CTkButton(
            self,
            width=FileHandlerConfig.Widgets.OPEN_FILE_BUTTON["width"], # type: ignore
            height=FileHandlerConfig.Widgets.OPEN_FILE_BUTTON["height"], # type: ignore
            fg_color=FileHandlerConfig.Widgets.OPEN_FILE_BUTTON["fg_color"], # type: ignore
            hover_color=FileHandlerConfig.Widgets.OPEN_FILE_BUTTON["hover_color"], # type: ignore
            text=FileHandlerConfig.Widgets.OPEN_FILE_BUTTON["text"], # type: ignore
            image=ctk.CTkImage(
                light_image=Image.open(
                    FileHandlerConfig.Widgets.OPEN_FILE_BUTTON["light_image"] # type: ignore
                ),
                size=FileHandlerConfig.Widgets.OPEN_FILE_BUTTON["size"], # type: ignore
            ),
            anchor=FileHandlerConfig.Widgets.OPEN_FILE_BUTTON["anchor"], # type: ignore
        )

        self.export_to_excel_button: ctk.CTkButton = ctk.CTkButton(
            self,
            width=FileHandlerConfig.Widgets.EXPORT_TO_EXCEL_BUTTON["width"], # type: ignore
            height=FileHandlerConfig.Widgets.EXPORT_TO_EXCEL_BUTTON["height"], # type: ignore
            fg_color=FileHandlerConfig.Widgets.EXPORT_TO_EXCEL_BUTTON["fg_color"], # type: ignore
            hover_color=FileHandlerConfig.Widgets.EXPORT_TO_EXCEL_BUTTON["hover_color"], # type: ignore
            text=FileHandlerConfig.Widgets.EXPORT_TO_EXCEL_BUTTON["text"], # type: ignore
            image=ctk.CTkImage(
                light_image=Image.open(
                    FileHandlerConfig.Widgets.EXPORT_TO_EXCEL_BUTTON["light_image"] # type: ignore
                ),
                size=FileHandlerConfig.Widgets.EXPORT_TO_EXCEL_BUTTON["size"], # type: ignore
            ),
            anchor=FileHandlerConfig.Widgets.EXPORT_TO_EXCEL_BUTTON["anchor"], # type: ignore
        )

        self.selected_file_path: ctk.StringVar = ctk.StringVar()
        self.file_entry: InputEntryList = InputEntryList(
            self,
            border_width=FileHandlerConfig.Widgets.FILE_ENTRY["border_width"], # type: ignore
            fg_color=FileHandlerConfig.Widgets.FILE_ENTRY["fg_color"], # type: ignore
            border_color=FileHandlerConfig.Widgets.FILE_ENTRY["border_color"], # type: ignore
            selected_file_path=self.selected_file_path,
            font=ctk.CTkFont(
                family=FileHandlerConfig.Widgets.FILE_ENTRY["family"], # type: ignore
                size=FileHandlerConfig.Widgets.FILE_ENTRY["size"], # type: ignore
            ),
            state=FileHandlerConfig.Widgets.FILE_ENTRY["state"], # type: ignore
            collection_filepath_yaml=FileHandlerConfig.Widgets.FILE_ENTRY[ # type: ignore
                "collection_filepath_yaml"
            ],
        )

    def create_layout(self) -> None:
        """
        Create layout.
        """
        self.file_entry.pack(
            side=FileHandlerConfig.Layout.FILE_ENTRY["side"],
            fill=FileHandlerConfig.Layout.FILE_ENTRY["fill"],
            expand=FileHandlerConfig.Layout.FILE_ENTRY["expand"],
            padx=FileHandlerConfig.Layout.FILE_ENTRY["padx"],
            pady=FileHandlerConfig.Layout.FILE_ENTRY["pady"],
        )
        self.title_label.pack(
            side=FileHandlerConfig.Layout.TITLE_LABEL["side"],
            fill=FileHandlerConfig.Layout.TITLE_LABEL["fill"],
            expand=FileHandlerConfig.Layout.TITLE_LABEL["expand"],
            padx=FileHandlerConfig.Layout.TITLE_LABEL["padx"],
            pady=FileHandlerConfig.Layout.TITLE_LABEL["pady"],
        )
        self.export_to_excel_button.pack(
            side=FileHandlerConfig.Layout.EXPORT_TO_EXCEL_BUTTON["side"],
            fill=FileHandlerConfig.Layout.EXPORT_TO_EXCEL_BUTTON["fill"],
            expand=FileHandlerConfig.Layout.EXPORT_TO_EXCEL_BUTTON["expand"],
            padx=FileHandlerConfig.Layout.EXPORT_TO_EXCEL_BUTTON["padx"],
            pady=FileHandlerConfig.Layout.EXPORT_TO_EXCEL_BUTTON["pady"],
        )
        self.open_file_button.pack(
            side=FileHandlerConfig.Layout.OPEN_FILE_BUTTON["side"],
            fill=FileHandlerConfig.Layout.OPEN_FILE_BUTTON["fill"],
            expand=FileHandlerConfig.Layout.OPEN_FILE_BUTTON["expand"],
            padx=FileHandlerConfig.Layout.OPEN_FILE_BUTTON["padx"],
            pady=FileHandlerConfig.Layout.OPEN_FILE_BUTTON["pady"],
        )
