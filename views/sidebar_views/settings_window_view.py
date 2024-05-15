""" Defines the SettingsWindowView class with the settings toplevel window layout. """

from __future__ import annotations
from typing import TYPE_CHECKING
from sys import platform
import customtkinter as ctk
from views.configurations_view import SettingsWindowConfig

if TYPE_CHECKING:
    from views.sidebar_frame_view import NavigationFrameView


class SettingsWindowView(ctk.CTkToplevel):
    """
    Layout of the settings toplevel window.
    """

    __slots__ = ("root",)

    def __init__(self, master: NavigationFrameView) -> None:
        super().__init__(master)

        self.withdraw()

        self.title(SettingsWindowConfig.General.TITLE)
        self.iconbitmap(SettingsWindowConfig.General.ICON)
        # Because CTkToplevel currently is bugged on windows and doesn't check if a user
        # specified icon is set we need to set the icon again after 200ms
        if platform.startswith("win"):
            self.after(200, lambda: self.iconbitmap(SettingsWindowConfig.General.ICON))

        self.resizable(
            SettingsWindowConfig.Dimensions.RESIZABLE_WIDTH,
            SettingsWindowConfig.Dimensions.RESIZABLE_HEIGHT,
        )

        self.root: ctk.CTk

        self.__initialize_widgets()
        self.__create_layout()

    def __initialize_widgets(self) -> None:
        """
        Initialize widgets.
        """

    def __create_layout(self) -> None:
        """
        Create layout.
        """
