""" Defines the HeaderFrameView class with the header frame layout. """

from __future__ import annotations
from typing import TYPE_CHECKING
import customtkinter as ctk
from .configurations_view import Config
from .sidebar_views.navigation_frame_view import NavigationFrameView
from .sidebar_views.header_frame_view import HeaderFrameView

if TYPE_CHECKING:
    from .main_view import MainView


class SidebarFrameView(ctk.CTkFrame):
    """
    Layout of the header frame.
    """

    __slots__ = "root", "navigation_frame_view", "header_panel"

    def __init__(self, master: MainView) -> None:
        super().__init__(
            master,
            corner_radius=Config.General.CORNER_RADIUS,
            fg_color=Config.Colors.TRANSPARENT,
        )
        self.root: ctk.CTk

        self.__initialize_widgets()
        self.__create_layout()

    def __initialize_widgets(self) -> None:
        """
        Initialize widgets.
        """
        self.navigation_frame_view: NavigationFrameView = NavigationFrameView(self)
        self.header_frame_view: HeaderFrameView = HeaderFrameView(self)

        self.filehandling_frame_view = self.header_frame_view.filehandling_frame_view


    def __create_layout(self) -> None:
        """
        Create layout.
        """
        self.navigation_frame_view.pack(
            side=Config.Layout.NAVIGATION_FRAME_SIDE,
            fill=Config.Layout.NAVIGATION_FRAME_FILL,
            expand=Config.Layout.NAVIGATION_FRAME_EXPAND,
        )

        self.header_frame_view.pack(
            side=Config.Layout.HEADER_PANEL_SIDE,
            fill=Config.Layout.HEADER_PANEL_FILL,
            expand=Config.Layout.HEADER_PANEL_EXPAND,
        )
