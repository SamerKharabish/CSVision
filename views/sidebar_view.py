""" Defines the HeaderFrameView class with the header frame layout. """

from __future__ import annotations
from typing import TYPE_CHECKING
import customtkinter as ctk
from configurations.sidebar_config import SidebarConfig
from .sidebar_views.navigation_panel_view import NavigationPanelView
from .sidebar_views.header_frame_view import ProcessorPanelView

if TYPE_CHECKING:
    from .main_view import MainView


class SidebarView(ctk.CTkFrame):
    """
    Layout of the sidebar.
    """

    __slots__ = "root", "navigation_panel_view", "processor_panel_view"

    def __init__(self, master: MainView) -> None:
        super().__init__(
            master,
            corner_radius=SidebarConfig.OwnArgs.CORNER_RADIUS,
            border_width=SidebarConfig.OwnArgs.BORDER_WIDTH,
            fg_color=SidebarConfig.OwnArgs.TRANSPARENT,
        )
        self.root: ctk.CTk

        self.__initialize_widgets()
        self.__create_layout()

    def __initialize_widgets(self) -> None:
        """
        Initialize widgets.
        """
        self.navigation_panel_view: NavigationPanelView = NavigationPanelView(self)
        self.processor_panel_view: ProcessorPanelView = ProcessorPanelView(self)

    def __create_layout(self) -> None:
        """
        Create layout.
        """
        self.navigation_panel_view.pack(
            side=SidebarConfig.Widgets.NAVIGATION_PANEL_VIEW["side"],
            fill=SidebarConfig.Widgets.NAVIGATION_PANEL_VIEW["fill"],
            expand=SidebarConfig.Widgets.NAVIGATION_PANEL_VIEW["expand"],
        )

        self.processor_panel_view.pack(
            side=SidebarConfig.Widgets.PROCESSOR_PANEL_VIEW["side"],
            fill=SidebarConfig.Widgets.PROCESSOR_PANEL_VIEW["fill"],
            expand=SidebarConfig.Widgets.PROCESSOR_PANEL_VIEW["expand"],
        )
