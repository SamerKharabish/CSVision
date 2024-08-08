""" Defines the PresetFrameView class with the preset frame layout. """

from __future__ import annotations
from typing import TYPE_CHECKING
from PIL import Image
import customtkinter as ctk
from views.configurations_view import Config

if TYPE_CHECKING:
    from views.sidebar_frame_view import HeaderFrameView


class PresetFrameView(ctk.CTkFrame):
    """
    Layout of the preset frame.
    """

    def __init__(self, master: HeaderFrameView) -> None:
        super().__init__(
            master,
            height=40,
            corner_radius=Config.General.CORNER_RADIUS,
            border_width=Config.General.FRAME_BORDER_WIDTH,
        )

        self.__initialize_widgets()
        self.__create_layout()

    def __initialize_widgets(self) -> None:
        """
        Initialize widgets.
        """
        self.preset_entry = ctk.CTkEntry(
            self,
            border_width=Config.General.OUTPUT_ENTRY_BORDER_WIDTH,
            border_color=Config.Colors.DIM_GRAY,
            fg_color=Config.Colors.ONYX,
            font=ctk.CTkFont(
                family=Config.Fonts.FONT_SIZE_WEIGHT[0],
                size=Config.Fonts.FONT_SIZE_WEIGHT[1],
            ),
        )

        self.save_preset_button = ctk.CTkButton(
            self,
            width=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            height=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            fg_color=Config.Colors.TRANSPARENT,
            hover_color=Config.Colors.ONYX_LIGHT,
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

        self.load_preset_button = ctk.CTkButton(
            self,
            width=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            height=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            fg_color=Config.Colors.TRANSPARENT,
            hover_color=Config.Colors.ONYX_LIGHT,
            text="",
            image=ctk.CTkImage(
                light_image=Image.open(Config.ImageFormats.REFRESH_PNG),
                size=(
                    Config.Dimensions.ACTION_IMAGE_WIDTH_HEIGHT,
                    Config.Dimensions.ACTION_IMAGE_WIDTH_HEIGHT,
                ),
            ),
            anchor=Config.Layout.ACTION_BUTTON_TEXT_ANCHOR,
        )

    def __create_layout(self) -> None:
        """
        Create layout.
        """
        self.pack_propagate(False)
        self.preset_entry.pack(
            side="left",
            fill="x",
            expand=True,
            padx=Config.Layout.STANDART_PAD,
            pady=Config.Layout.STANDART_PAD,
        )
        self.load_preset_button.pack(
            side="left",
            fill="y",
            expand=False,
            padx=Config.Layout.ZERO_PAD,
            pady=Config.Layout.STANDART_PAD,
        )
        self.save_preset_button.pack(
            side="left",
            fill="y",
            expand=False,
            padx=(0, 7),
            pady=Config.Layout.STANDART_PAD,
        )
