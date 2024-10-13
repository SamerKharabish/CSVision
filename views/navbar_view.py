""" Defines the NavigationPanelView class with the navigation frame layout. """

from __future__ import annotations
from typing import TYPE_CHECKING
from PIL import Image
import customtkinter as ctk
from configurations.navbar_config import NavBarConfig
from utils.helper_functions import find_root

if TYPE_CHECKING:
    from .main_view import MainView


class NavigationBarView(ctk.CTkFrame):
    """
    Layout of the navigation frame.
    """

    __slots__ = "root", "toggle_header_button", "settings_button"

    def __init__(self, master: MainView) -> None:
        super().__init__(
            master,
            corner_radius=NavBarConfig.OwnArgs.CORNER_RADIUS,
            border_width=NavBarConfig.OwnArgs.BORDER_WIDTH,
            fg_color=NavBarConfig.OwnArgs.TRANSPARENT,
        )
        self.root: ctk.CTk = find_root(self)

        self.current_image: ctk.CTkImage

        self.__initialize_widgets()
        self.__create_layout()

    def __initialize_widgets(self) -> None:
        """
        Initialize widgets.
        """
        self.hide_image: ctk.CTkImage = ctk.CTkImage(
            light_image=Image.open(
                NavBarConfig.Widgets.SIDEBAR_TOGGLE_BUTTON["hide_image"]  # type: ignore
            ),
            size=NavBarConfig.Widgets.SIDEBAR_TOGGLE_BUTTON["size"], # type: ignore
        )
        self.show_image: ctk.CTkImage = ctk.CTkImage(
            light_image=Image.open(
                NavBarConfig.Widgets.SIDEBAR_TOGGLE_BUTTON["show_image"] # type: ignore
            ),
            size=NavBarConfig.Widgets.SIDEBAR_TOGGLE_BUTTON["size"], # type: ignore
        )
        self.current_image = self.hide_image

        self.toggle_sidebar_button: ctk.CTkButton = ctk.CTkButton(
            self,
            width=NavBarConfig.Widgets.SIDEBAR_TOGGLE_BUTTON["width"], # type: ignore
            height=NavBarConfig.Widgets.SIDEBAR_TOGGLE_BUTTON["height"], # type: ignore
            fg_color=NavBarConfig.Widgets.SIDEBAR_TOGGLE_BUTTON["fg_color"], # type: ignore
            hover_color=NavBarConfig.Widgets.SIDEBAR_TOGGLE_BUTTON["hover_color"], # type: ignore
            text=NavBarConfig.Widgets.SIDEBAR_TOGGLE_BUTTON["text"], # type: ignore
            image=self.hide_image,
            anchor=NavBarConfig.Widgets.SIDEBAR_TOGGLE_BUTTON["anchor"], # type: ignore
        )

        self.settings_button: ctk.CTkButton = ctk.CTkButton(
            self,
            width=NavBarConfig.Widgets.SETTINGS_BUTTON["width"], # type: ignore
            height=NavBarConfig.Widgets.SETTINGS_BUTTON["height"], # type: ignore
            fg_color=NavBarConfig.Widgets.SETTINGS_BUTTON["fg_color"], # type: ignore
            hover_color=NavBarConfig.Widgets.SETTINGS_BUTTON["hover_color"], # type: ignore
            text=NavBarConfig.Widgets.SETTINGS_BUTTON["text"], # type: ignore
            image=ctk.CTkImage(
                light_image=Image.open(
                    NavBarConfig.Widgets.SETTINGS_BUTTON["light_image"] # type: ignore
                ),
                size=NavBarConfig.Widgets.SETTINGS_BUTTON["size"], # type: ignore
            ),
            anchor=NavBarConfig.Widgets.SETTINGS_BUTTON["anchor"], # type: ignore
        )

    def __create_layout(self) -> None:
        """
        Create layout.
        """
        self.toggle_sidebar_button.pack(
            side=NavBarConfig.Layout.SIDEBAR_TOGGLE_BUTTON["side"],
            fill=NavBarConfig.Layout.SIDEBAR_TOGGLE_BUTTON["fill"],
            expand=NavBarConfig.Layout.SIDEBAR_TOGGLE_BUTTON["expand"],
            padx=NavBarConfig.Layout.SIDEBAR_TOGGLE_BUTTON["padx"],
            pady=NavBarConfig.Layout.SIDEBAR_TOGGLE_BUTTON["pady"],
        )

        self.settings_button.pack(
            side=NavBarConfig.Layout.SETTINGS_BUTTON["side"],
            fill=NavBarConfig.Layout.SETTINGS_BUTTON["fill"],
            expand=NavBarConfig.Layout.SETTINGS_BUTTON["expand"],
            padx=NavBarConfig.Layout.SETTINGS_BUTTON["padx"],
            pady=NavBarConfig.Layout.SETTINGS_BUTTON["pady"],
        )

    def set_hide_image(self) -> None:
        """
        Set the "hide_image" for the toggle button.
        """
        self.toggle_sidebar_button.configure(
            image=self.hide_image,
        )

    def set_show_image(self) -> None:
        """
        Set the "show_image" for the toggle button.
        """
        self.toggle_sidebar_button.configure(
            image=self.show_image,
        )

    def toggle_image(self) -> None:
        """
        Toggle the "hide_image" and "show_image" for the toggle button.
        """
        if self.current_image == self.show_image:
            self.set_hide_image()
            self.current_image = self.hide_image
        else:
            self.set_show_image()
            self.current_image = self.show_image
