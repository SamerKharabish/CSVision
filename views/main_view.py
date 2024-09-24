"""Defines the MainView class with the main layout."""

from __future__ import annotations
from typing import TYPE_CHECKING
import customtkinter as ctk
from configurations.main_config import MainConfig
from utils.helper_functions import find_root
from .navbar_view import NavigationBarView
from .plot_frame_view import PlotView
from .sidebar_view import SidebarView
from .statusbar_view import StatusbarView


if TYPE_CHECKING:
    from app import AppView


class MainView(ctk.CTkFrame):
    """
    Layout of the main application.
    """

    __slots__ = (
        "root",
        "nav_bar_view",
        "plot_view",
        "sidebar_view",
        "statusbar_view",
    )

    def __init__(self, master: AppView) -> None:
        super().__init__(master, corner_radius=MainConfig.OwnArgs.CORNER_RADIUS)

        self.root: ctk.CTk = find_root(self)

        self.initialize_widgets()
        self.create_layout()

    def initialize_widgets(self) -> None:
        """
        Initialize widgets.
        """
        self.nav_bar_view: NavigationBarView = NavigationBarView(self)
        self.plot_view: PlotView = PlotView(self)
        self.sidebar_view: SidebarView = SidebarView(self)
        self.statusbar_view: StatusbarView = StatusbarView(self)

    def create_layout(self) -> None:
        """
        Create layout.
        """
        self.statusbar_view.pack(
            side=MainConfig.Layout.STATUSBAR_VIEW["side"],
            fill=MainConfig.Layout.STATUSBAR_VIEW["fill"],
            expand=MainConfig.Layout.STATUSBAR_VIEW["expand"],
        )

        self.nav_bar_view.pack(
            side=MainConfig.Layout.NAV_BAR_VIEW["side"],
            fill=MainConfig.Layout.NAV_BAR_VIEW["fill"],
            expand=MainConfig.Layout.NAV_BAR_VIEW["expand"],
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

    def hide_sidebar(self) -> None:
        """
        Hide the sidebar.
        """
        self.sidebar_view.pack_forget()

    def show_sidebar(self) -> None:
        """
        Show the sidebar.
        """
        self.sidebar_view.pack(
            side=MainConfig.Layout.SIDEBAR_VIEW["side"],
            fill=MainConfig.Layout.SIDEBAR_VIEW["fill"],
            expand=MainConfig.Layout.SIDEBAR_VIEW["expand"],
        )

    def toggle_sidebar(self) -> None:
        """
        Toggle the sidebar.
        """
        if self.sidebar_view.winfo_manager():
            self.hide_sidebar()
        else:
            self.show_sidebar()
