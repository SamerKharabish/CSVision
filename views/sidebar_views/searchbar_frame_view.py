""" Defines the SearchbarFrameView class with the searchbar frame layout. """

from __future__ import annotations
from typing import TYPE_CHECKING
from PIL import Image
import customtkinter as ctk
from views.configurations_view import SearchbarConfig

if TYPE_CHECKING:
    from sidebar_view import SidebarView


class SearchbarFrameView(ctk.CTkFrame):
    """
    Layout of the file searchbar frame.
    """

    __slots__ = (
        "title_frame",
        "title_label",
        "clear_search_result_button",
        "entry_frame",
        "search_entry",
        "search_mode_segmented_button_var",
        "search_selection_segmented_button",
    )

    def __init__(self, master: SidebarView) -> None:
        super().__init__(
            master,
            corner_radius=SearchbarConfig.General.CORNER_RADIUS,
            border_width=SearchbarConfig.General.FRAME_BORDER_WIDTH,
        )

        self.__initialize_widgets()
        self.__create_layout()

    def __initialize_widgets(self) -> None:
        """
        Initialize widgets.
        """
        self.title_frame: ctk.CTkFrame = ctk.CTkFrame(
            self,
            corner_radius=SearchbarConfig.General.CORNER_RADIUS,
            fg_color=SearchbarConfig.Colors.TRANSPARENT,
        )

        self.title_label: ctk.CTkLabel = ctk.CTkLabel(
            self.title_frame,
            text=SearchbarConfig.General.TEXT,
            font=ctk.CTkFont(
                family=SearchbarConfig.Fonts.FONT,
                size=SearchbarConfig.Fonts.FONT_SIZE,
                weight=SearchbarConfig.Fonts.FONT_WEIGHT,
            ),
            anchor=SearchbarConfig.Layout.TITLE_LABELS_ANCHOR,
        )

        self.clear_search_result_button: ctk.CTkButton = ctk.CTkButton(
            self.title_frame,
            width=SearchbarConfig.Dimensions.BUTTON_WIDTH,
            height=SearchbarConfig.Dimensions.BUTTON_HEIGHT,
            fg_color=SearchbarConfig.Colors.TRANSPARENT,
            hover_color=SearchbarConfig.Colors.HOVER,
            text="",
            image=ctk.CTkImage(
                light_image=Image.open(
                    SearchbarConfig.ImageFormats.CLEAR_SEARCH_RESULT_PNG
                ),
                size=(
                    SearchbarConfig.Dimensions.IMAGE_WIDTH,
                    SearchbarConfig.Dimensions.IMAGE_HEIGHT,
                ),
            ),
            anchor=SearchbarConfig.Layout.BUTTON_IMAGE_ANCHOR,
        )

        self.entry_frame: ctk.CTkFrame = ctk.CTkFrame(
            self,
            corner_radius=SearchbarConfig.General.CORNER_RADIUS,
            fg_color=SearchbarConfig.Colors.TRANSPARENT,
        )

        self.search_entry: ctk.CTkEntry = ctk.CTkEntry(
            self.entry_frame,
            width=244,
            border_width=SearchbarConfig.Layout.INPUT_ENTRY_BORDER_WIDTH,
            font=ctk.CTkFont(
                family=SearchbarConfig.Fonts.FONT,
                size=SearchbarConfig.Fonts.FONT_SIZE,
            ),
        )

        self.search_mode_segmented_button_var: ctk.StringVar = ctk.StringVar(
            value=SearchbarConfig.Values.SEARCH_MODE_SEGMENTED_BUTTON[0]
        )
        self.search_selection_segmented_button: ctk.CTkSegmentedButton = (
            ctk.CTkSegmentedButton(
                self.entry_frame,
                font=ctk.CTkFont(
                    family=SearchbarConfig.Fonts.FONT,
                    size=SearchbarConfig.Fonts.FONT_SIZE,
                    weight=SearchbarConfig.Fonts.FONT_WEIGHT,
                ),
                values=SearchbarConfig.Values.SEARCH_MODE_SEGMENTED_BUTTON,
                variable=self.search_mode_segmented_button_var,
            )
        )

    def __create_layout(self) -> None:
        """
        Create layout.
        """
        self.rowconfigure(
            (
                SearchbarConfig.Layout.TITLE_FRAME_ROW,
                SearchbarConfig.Layout.ENTRY_ROW,
                SearchbarConfig.Layout.FILTER_FRAME_ROW,
            ),
            weight=1,
        )

        self.title_frame.grid(
            row=SearchbarConfig.Layout.TITLE_FRAME_ROW,
            column=0,
            sticky=SearchbarConfig.Layout.GENERAL_INNER_FRAME_STICKY,
            padx=SearchbarConfig.Layout.STANDARD_PAD,
            pady=(1, 0),
        )
        self.title_frame.columnconfigure((0, 1), weight=1)
        self.title_label.grid(
            row=0,
            column=0,
            sticky="w",
            padx=SearchbarConfig.Layout.LABELS_IN_FRAME_PADX,
            pady=SearchbarConfig.Layout.ZERO_PAD,
        )
        self.clear_search_result_button.grid(
            row=0,
            column=1,
            sticky="e",
            padx=SearchbarConfig.Layout.ZERO_PAD,
            pady=SearchbarConfig.Layout.ZERO_PAD,
        )

        self.entry_frame.grid(
            row=SearchbarConfig.Layout.ENTRY_ROW,
            column=0,
            sticky=SearchbarConfig.Layout.GENERAL_INNER_FRAME_STICKY,
            padx=SearchbarConfig.Layout.STANDARD_PAD,
            pady=(0, 7),
        )
        self.search_entry.grid(
            row=0,
            column=0,
            sticky="w",
            padx=(0, 3),
            pady=SearchbarConfig.Layout.ZERO_PAD,
        )

        self.search_selection_segmented_button.grid(
            row=0,
            column=1,
            sticky="e",
            padx=(3, 0),
            pady=SearchbarConfig.Layout.ZERO_PAD,
        )
