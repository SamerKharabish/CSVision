""" Defines the SearchbarFrameView class with the searchbar frame layout. """

from __future__ import annotations
from typing import TYPE_CHECKING
from PIL import Image
import customtkinter as ctk
from views.configurations_view import Config

if TYPE_CHECKING:
    from views.sidebar_frame_view import HeaderFrameView


class SearchbarFrameView(ctk.CTkFrame):
    """
    Layout of the file searchbar frame.
    """

    def __init__(self, master: HeaderFrameView) -> None:
        super().__init__(
            master,
            corner_radius=Config.General.CORNER_RADIUS,
            border_width=Config.General.FRAME_BORDER_WIDTH,
        )

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
            text=Config.LabelTexts.SEARCHBAR_TEXT,
            font=ctk.CTkFont(
                family=Config.Fonts.FONT_SIZE_WEIGHT[0],
                size=Config.Fonts.FONT_SIZE_WEIGHT[1],
                weight=Config.Fonts.FONT_SIZE_WEIGHT[2],
            ),
            anchor=Config.Layout.HEADER_FRAME_LABELS_ANCHOR,
        )

        self.clear_search_result_button = ctk.CTkButton(
            self.title_frame,
            width=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            height=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            fg_color=Config.Colors.TRANSPARENT,
            hover_color=Config.Colors.ONYX_LIGHT,
            text="",
            image=ctk.CTkImage(
                light_image=Image.open(Config.ImageFormats.CLEAR_SEARCH_RESULT_PNG),
                size=(
                    Config.Dimensions.ACTION_IMAGE_WIDTH_HEIGHT,
                    Config.Dimensions.ACTION_IMAGE_WIDTH_HEIGHT,
                ),
            ),
            anchor=Config.Layout.ACTION_BUTTON_TEXT_ANCHOR,
        )

        self.entry_frame = ctk.CTkFrame(
            self,
            corner_radius=Config.General.CORNER_RADIUS,
            fg_color=Config.Colors.TRANSPARENT,
        )

        self.search_entry = ctk.CTkEntry(
            self.entry_frame,
            width=204,
            border_width=Config.General.INPUT_ENTRY_BORDER_WIDTH,
            font=ctk.CTkFont(
                family=Config.Fonts.FONT_SIZE_WEIGHT[0],
                size=Config.Fonts.FONT_SIZE_WEIGHT[1],
            ),
        )

        self.search_selection_segmented_button_var = ctk.StringVar(
            value=Config.Values.SEARCH_SELECTION_SEGMENTED_BUTTON[0]
        )
        self.search_selection_segmented_button = ctk.CTkSegmentedButton(
            self.entry_frame,
            font=ctk.CTkFont(
                family=Config.Fonts.FONT_SIZE_WEIGHT[0],
                size=Config.Fonts.FONT_SIZE_WEIGHT[1],
                weight=Config.Fonts.FONT_SIZE_WEIGHT[2],
            ),
            values=Config.Values.SEARCH_SELECTION_SEGMENTED_BUTTON,
            variable=self.search_selection_segmented_button_var,
        )

        self.filter_subheadings_segmented_button_var = ctk.StringVar(
            value=Config.Values.FILTER_SUBHEADINGS_SEGMENTED_BUTTON[0]
        )
        self.filter_subheadings_segmented_button = ctk.CTkSegmentedButton(
            self,
            font=ctk.CTkFont(
                family=Config.Fonts.FONT_SIZE_WEIGHT[0],
                size=Config.Fonts.FONT_SIZE_WEIGHT[1],
                weight=Config.Fonts.FONT_SIZE_WEIGHT[2],
            ),
            values=Config.Values.FILTER_SUBHEADINGS_SEGMENTED_BUTTON,
            variable=self.filter_subheadings_segmented_button_var,
        )

    def __create_layout(self) -> None:
        """
        Create layout.
        """
        self.rowconfigure(
            (
                Config.Layout.SEARCHBAR_TITLE_FARME_ROW,
                Config.Layout.SEARCHBAR_ENTRY_ROW,
                Config.Layout.SEARCHBAR_FILTER_FARME_ROW,
            ),
            weight=1,
        )

        self.title_frame.grid(
            row=Config.Layout.SEARCHBAR_TITLE_FARME_ROW,
            column=0,
            sticky=Config.Layout.GENERAL_INNER_FRAME_STICKY,
            padx=Config.Layout.STANDART_PAD,
            pady=(3, 0),
        )
        self.title_frame.columnconfigure((0, 1), weight=1)
        self.title_label.grid(
            row=0,
            column=0,
            sticky="w",
            padx=Config.Layout.LABELS_IN_FRAME_PADX,
            pady=Config.Layout.ZERO_PAD,
        )
        self.clear_search_result_button.grid(
            row=0,
            column=1,
            sticky="e",
            padx=Config.Layout.ZERO_PAD,
            pady=Config.Layout.ZERO_PAD,
        )

        self.entry_frame.grid(
            row=Config.Layout.SEARCHBAR_ENTRY_ROW,
            column=0,
            sticky=Config.Layout.GENERAL_INNER_FRAME_STICKY,
            padx=Config.Layout.STANDART_PAD,
            pady=Config.Layout.ZERO_PAD,
        )
        self.entry_frame.columnconfigure(0, weight=2)
        self.entry_frame.columnconfigure(1, weight=1)
        self.search_entry.grid(
            row=0,
            column=0,
            sticky="w",
            padx=(0, 3),
            pady=Config.Layout.ZERO_PAD,
        )

        self.search_selection_segmented_button.grid(
            row=0,
            column=1,
            sticky="e",
            padx=(3, 0),
            pady=Config.Layout.ZERO_PAD,
        )

        self.filter_subheadings_segmented_button.grid(
            row=Config.Layout.SEARCHBAR_FILTER_FARME_ROW,
            column=0,
            sticky=Config.Layout.GENERAL_INNER_FRAME_STICKY,
            padx=Config.Layout.STANDART_PAD,
            pady=Config.Layout.STANDART_PAD,
        )
