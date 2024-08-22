""" Defines the MainView class with the main layout. """

from __future__ import annotations
from typing import TYPE_CHECKING
import customtkinter as ctk
from configurations.main_config import MainConfig
from .statusbar_view import StatusbarView
from .sidebar_view import SidebarView
from .plot_frame_view import PlotView


if TYPE_CHECKING:
    from app import AppView


class MainView(ctk.CTkFrame):
    """
    Layout of the main application.
    """

    __slots__ = "root", "statusbar_view", "sidebar_view", "plot_view"

    def __init__(self, master: AppView) -> None:
        super().__init__(master, corner_radius=MainConfig.OwnArgs.CORNER_RADIUS)
        self.root: ctk.CTk

        self.__initialize_widgets()
        self.__create_layout()

    def __initialize_widgets(self) -> None:
        """
        Initialize widgets.
        """
        self.statusbar_view: StatusbarView = StatusbarView(self)
        self.sidebar_view: SidebarView = SidebarView(self)
        self.plot_view: PlotView = PlotView(self)

    def __create_layout(self) -> None:
        """
        Create layout.
        """
        self.statusbar_view.pack(
            side=MainConfig.Layout.STATUSBAR_VIEW["side"],
            fill=MainConfig.Layout.STATUSBAR_VIEW["fill"],
            expand=MainConfig.Layout.STATUSBAR_VIEW["expand"],
        )

        self.sidebar_view.pack(
            side=MainConfig.Layout.SIDEBAR_VIEW["side"],
            fill=MainConfig.Layout.SIDEBAR_VIEW["fill"],
            expand=MainConfig.Layout.SIDEBAR_VIEW["expand"],
        )

        self.plot_view.pack(
            side=MainConfig.Layout.PLOT_VIEW["side"],
            fill=MainConfig.Layout.PLOT_VIEW["fill"],
            expand=MainConfig.Layout.PLOT_VIEW["expand"],
        )
