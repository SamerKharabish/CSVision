""" Defines the NavigationFrameView class with the navigation frame layout. """

from __future__ import annotations
from typing import TYPE_CHECKING
from PIL import Image
import customtkinter as ctk
from views.configurations_view import Config
from views.sidebar_views.settings_window_view import SettingsWindowView

if TYPE_CHECKING:
    from views.sidebar_frame_view import SidebarFrameView


class NavigationFrameView(ctk.CTkFrame):
    """
    Layout of the navigation frame.
    """

    __slots__ = "root", "settings_window", "toggle_header_button", "settings_button"

    def __init__(self, master: SidebarFrameView) -> None:
        super().__init__(
            master,
            corner_radius=Config.General.CORNER_RADIUS,
            border_width=Config.General.FRAME_BORDER_WIDTH,
            fg_color=Config.Colors.TRANSPARENT,
        )
        self.root: ctk.CTk

        self.__initialize_widgets()
        self.__create_layout()

    def __initialize_widgets(self) -> None:
        """
        Initialize widgets.
        """
        self.settings_window_view: SettingsWindowView = SettingsWindowView(self)

        self.toggle_header_button: ctk.CTkButton = ctk.CTkButton(
            self,
            width=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            height=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            fg_color=Config.Colors.TRANSPARENT,
            hover_color=Config.Colors.TRANSPARENT_BUTTON_HOVER,
            text="",
            image=ctk.CTkImage(
                light_image=Image.open(Config.ImageFormats.HIDE_SIDEPANEL_PNG),
                size=(
                    Config.Dimensions.TOGGLE_HEADER_FRAME_BUTTON_WIDTH_HEIGHT,
                    Config.Dimensions.TOGGLE_HEADER_FRAME_BUTTON_WIDTH_HEIGHT,
                ),
            ),
            anchor=Config.Layout.ACTION_BUTTON_TEXT_ANCHOR,
        )

        self.settings_button: ctk.CTkButton = ctk.CTkButton(
            self,
            width=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            height=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            fg_color=Config.Colors.TRANSPARENT,
            hover_color=Config.Colors.TRANSPARENT_BUTTON_HOVER,
            text="",
            image=ctk.CTkImage(
                light_image=Image.open(Config.ImageFormats.SETTINGS_PNG),
                size=(
                    Config.Dimensions.TOGGLE_HEADER_FRAME_BUTTON_WIDTH_HEIGHT,
                    Config.Dimensions.TOGGLE_HEADER_FRAME_BUTTON_WIDTH_HEIGHT,
                ),
            ),
            anchor=Config.Layout.ACTION_BUTTON_TEXT_ANCHOR,
        )

    def __create_layout(self) -> None:
        """
        Create layout.
        """
        self.toggle_header_button.pack(
            side=Config.Layout.TOGGLE_HEADER_FRAME_BUTTON_SIDE,
            fill=Config.Layout.TOGGLE_HEADER_FRAME_BUTTON_FILL,
            expand=Config.Layout.TOGGLE_HEADER_FRAME_BUTTON_EXPAND,
            padx=Config.Layout.TOGGLE_HEADER_FRAME_BUTTON_PAD,
            pady=Config.Layout.STANDART_PAD,
        )

        self.settings_button.pack(
            side=Config.Layout.SETTINGS_BUTTON_SIDE,
            fill=Config.Layout.SETTINGS_BUTTON_FILL,
            expand=Config.Layout.SETTINGS_BUTTON_EXPAND,
            padx=Config.Layout.SETTINGS_BUTTON_PAD,
            pady=Config.Layout.STANDART_PAD,
        )
