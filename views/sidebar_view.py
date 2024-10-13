"""Defines the SidebarView class with the sidebar layout."""

from __future__ import annotations
from typing import TYPE_CHECKING
import customtkinter as ctk
from configurations.sidebar_config import SidebarConfig
from .sidebar_views.filehandler_view import FileHandlerView
from .sidebar_views.searchbar_frame_view import SearchbarFrameView
from .sidebar_views.header_list_view import HeaderListView
from .sidebar_views.config_header_list_frame_view import ConfigHeaderListFrameView
from .sidebar_views.preset_frame_view import PresetFrameView

if TYPE_CHECKING:
    from .main_view import MainView


class SidebarView(ctk.CTkFrame):
    """
    Layout of the sidebar.
    """

    __slots__ = (
        "filehandler_frame_view",
        "searchbar_frame_view",
        "header_list_frame_view",
        "config_header_list_frame_view",
        "preset_frame_view",
    )

    def __init__(self, master: MainView) -> None:
        super().__init__(
            master,
            corner_radius=SidebarConfig.OwnArgs.CORNER_RADIUS,
            border_width=SidebarConfig.OwnArgs.BORDER_WIDTH,
            fg_color=SidebarConfig.OwnArgs.TRANSPARENT,
        )
        self.initialize_widgets()
        self.create_layout()

    def initialize_widgets(self) -> None:
        """
        Initialize widgets.
        """
        self.file_handler_view: FileHandlerView = FileHandlerView(self)
        self.searchbar_frame_view: SearchbarFrameView = SearchbarFrameView(self)
        self.header_list_frame_view: HeaderListView = HeaderListView(self)
        self.config_header_list_frame_view: ConfigHeaderListFrameView = (
            ConfigHeaderListFrameView(self)
        )
        self.preset_frame_view: PresetFrameView = PresetFrameView(self)

    def create_layout(self) -> None:
        """
        Create layout.
        """
        self.grid_rowconfigure(
            SidebarConfig.OwnArgs.ROWS_RESIZE,
            weight=SidebarConfig.OwnArgs.ROWS_RESIZE_WEIGHT,
        )
        self.grid_rowconfigure(
            SidebarConfig.OwnArgs.ROWS_FIXED,
            weight=SidebarConfig.OwnArgs.ROWS_FIXED_WEIGHT,
        )
        self.file_handler_view.grid(
            row=SidebarConfig.OwnArgs.ROWS_FIXED[0],
            column=SidebarConfig.OwnArgs.COLUMN,
            sticky=SidebarConfig.OwnArgs.STICKY,
        )
        self.searchbar_frame_view.grid(
            row=SidebarConfig.OwnArgs.ROWS_FIXED[1],
            column=SidebarConfig.OwnArgs.COLUMN,
            sticky=SidebarConfig.OwnArgs.STICKY,
        )
        self.header_list_frame_view.grid(
            row=SidebarConfig.OwnArgs.ROWS_RESIZE[0],
            column=SidebarConfig.OwnArgs.COLUMN,
            sticky=SidebarConfig.OwnArgs.STICKY,
        )
        self.config_header_list_frame_view.grid(
            row=SidebarConfig.OwnArgs.ROWS_RESIZE[1],
            column=SidebarConfig.OwnArgs.COLUMN,
            sticky=SidebarConfig.OwnArgs.STICKY,
        )
        self.preset_frame_view.grid(
            row=SidebarConfig.OwnArgs.ROWS_FIXED[2],
            column=SidebarConfig.OwnArgs.COLUMN,
            sticky=SidebarConfig.OwnArgs.STICKY,
        )
