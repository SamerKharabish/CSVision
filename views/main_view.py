""" Defines the MainView class with the main layout. """

from __future__ import annotations
from typing import TYPE_CHECKING
import customtkinter as ctk
from .configurations_view import MainConfig
from .statusbar_frame_view import StatusbarFrameView
from .sidebar_frame_view import SidebarFrameView
from .plot_frame_view import PlotFrameView


if TYPE_CHECKING:
    from app import AppView


class MainView(ctk.CTkFrame):
    """
    Layout of the main application.
    """

    __slots__ = "root", "statusbar_frame_view", "sidebar_frame_view", "plot_frame_view"

    def __init__(self, master: AppView) -> None:
        super().__init__(master, corner_radius=MainConfig.General.CORNER_RADIUS)
        self.root: ctk.CTk

        self.__initialize_widgets()
        self.__create_layout()

    def __initialize_widgets(self) -> None:
        """
        Initialize widgets.
        """
        self.statusbar_frame_view: StatusbarFrameView = StatusbarFrameView(self)
        self.sidebar_frame_view: SidebarFrameView = SidebarFrameView(self)
        self.plot_frame_view: PlotFrameView = PlotFrameView(self)

    def __create_layout(self) -> None:
        """
        Create layout.
        """
        self.statusbar_frame_view.pack(
            side=MainConfig.Layout.STATUSBARVIEW_SIDE,
            fill=MainConfig.Layout.STATUSBARVIEW_FILL,
            expand=MainConfig.Layout.STATUSBARVIEW_EXPAND,
        )

        self.sidebar_frame_view.pack(
            side=MainConfig.Layout.SIDEBARVIEW_SIDE,
            fill=MainConfig.Layout.SIDEBARVIEW_FILL,
            expand=MainConfig.Layout.SIDEBARVIEW_EXPAND,
        )

        self.plot_frame_view.pack(
            side=MainConfig.Layout.PLOTVIEW_SIDE,
            fill=MainConfig.Layout.PLOTVIEW_FILL,
            expand=MainConfig.Layout.PLOTVIEW_EXPAND,
        )
