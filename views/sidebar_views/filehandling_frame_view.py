""" Defines the FileHandlingFrameView class with the file handling frame layout. """

from __future__ import annotations
from typing import TYPE_CHECKING
from PIL import Image
import customtkinter as ctk
from utils.input_entry_list import InputEntryList
from views.configurations_view import Config

if TYPE_CHECKING:
    from views.sidebar_frame_view import HeaderFrameView


class FileHandlingFrameView(ctk.CTkFrame):
    """
    Layout of the file handling frame.
    """

    def __init__(self, master: HeaderFrameView) -> None:
        super().__init__(master,
            corner_radius=Config.General.CORNER_RADIUS,
            border_width=Config.General.FRAME_BORDER_WIDTH,)

        self.__initialize_widgets()
        self.__create_layout()

    def __initialize_widgets(self) -> None:
        """
        Initialize widgets.
        """
        self.title_frame = ctk.CTkFrame(
            self,
            corner_radius=Config.General.CORNER_RADIUS,
            fg_color=Config.Colors.TRANSPARENT,
        )

        self.title_label = ctk.CTkLabel(
            self.title_frame,
            text=Config.LabelTexts.FILEHANDLING_TEXT,
            font=ctk.CTkFont(
                family=Config.Fonts.LABEL_TEXTS[0],
                size=Config.Fonts.LABEL_TEXTS[1],
                weight=Config.Fonts.LABEL_TEXTS[2],
            ),
            anchor=Config.Layout.HEADER_FRAME_LABELS_ANCHOR,
        )

        self.open_file_button = ctk.CTkButton(
            self.title_frame,
            width=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            height=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            fg_color=Config.Colors.TRANSPARENT,
            hover_color=Config.Colors.TRANSPARENT_BUTTON_HOVER,
            text="",
            image=ctk.CTkImage(
                light_image=Image.open(Config.ImageFormats.OPEN_FILE_PNG),
                size=(
                    Config.Dimensions.ACTION_IMAGE_WIDTH_HEIGHT,
                    Config.Dimensions.ACTION_IMAGE_WIDTH_HEIGHT,
                ),
            ),
            anchor=Config.Layout.ACTION_BUTTON_TEXT_ANCHOR,
        )

        self.export_to_excel = ctk.CTkButton(
            self.title_frame,
            width=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            height=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            fg_color=Config.Colors.TRANSPARENT,
            hover_color=Config.Colors.TRANSPARENT_BUTTON_HOVER,
            text="",
            image=ctk.CTkImage(
                light_image=Image.open(Config.ImageFormats.EXCEL_PNG),
                size=(
                    Config.Dimensions.ACTION_IMAGE_WIDTH_HEIGHT,
                    Config.Dimensions.ACTION_IMAGE_WIDTH_HEIGHT,
                ),
            ),
            anchor=Config.Layout.ACTION_BUTTON_TEXT_ANCHOR,
        )

        self.selected_file_path = ctk.StringVar()
        self.file_entry = InputEntryList(
            self,
            width=320,
            border_width=Config.General.OUTPUT_ENTRY_BORDER_WIDTH,
            fg_color=Config.Colors.ONYX,
            border_color=Config.Colors.BORDER_COLOR,
            selected_file_path=self.selected_file_path,
            font=ctk.CTkFont(
                family=Config.Fonts.LABEL_TEXTS[0], size=Config.Fonts.LABEL_TEXTS[1]
            ),
            state="readonly",
            collection_filepath_yaml=Config.Values.COLLECTION_FILEPATH_YAML,
        )

    def __create_layout(self) -> None:
        """
        Create layout.
        """
        self.rowconfigure(
            (
                Config.Layout.FILEHANDLING_TITLE_FARME_ROW,
                Config.Layout.FILEHANDLING_ENTRY_ROW,
                Config.Layout.FILEHANDLING_FILTER_FARME_ROW,
            ),
            weight=1,
        )

        self.title_frame.grid(
            row=Config.Layout.FILEHANDLING_TITLE_FARME_ROW,
            column=0,
            sticky=Config.Layout.GENERAL_INNER_FRAME_STICKY,
            padx=Config.Layout.STANDART_PAD,
            pady=(3, 0),
        )
        self.title_frame.columnconfigure(0, weight=50)
        self.title_frame.columnconfigure((1, 2), weight=1)
        self.title_label.grid(
            row=0,
            column=0,
            sticky="w",
            padx=Config.Layout.LABELS_IN_FRAME_PADX,
            pady=Config.Layout.ZERO_PAD,
        )
        self.open_file_button.grid(
            row=0,
            column=1,
            sticky="e",
            padx=Config.Layout.ZERO_PAD,
            pady=Config.Layout.ZERO_PAD,
        )
        self.export_to_excel.grid(
            row=0,
            column=2,
            sticky="e",
            padx=Config.Layout.ZERO_PAD,
            pady=Config.Layout.ZERO_PAD,
        )

        self.file_entry.grid(
            row=Config.Layout.FILEHANDLING_ENTRY_ROW,
            column=0,
            sticky=Config.Layout.GENERAL_INNER_FRAME_STICKY,
            padx=Config.Layout.STANDART_PAD,
            pady=(0, 7),
        )
