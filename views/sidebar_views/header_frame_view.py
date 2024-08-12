""" Defines the HeaderFrameView class with the header frame layout. """

from __future__ import annotations
from typing import TYPE_CHECKING
import customtkinter as ctk
from views.configurations_view import Config
from .filehandling_frame_view import FileHandlingFrameView
from .searchbar_frame_view import SearchbarFrameView
from .header_list_frame_view import HeaderListFrameView
from .config_header_list_frame_view import ConfigHeaderListFrameView
from .preset_frame_view import PresetFrameView

if TYPE_CHECKING:
    from views.sidebar_frame_view import SidebarFrameView


class HeaderFrameView(ctk.CTkFrame):
    """
    Layout of the header frame.
    """

    __slots__ = (
        "filehandling_frame_view",
        "searchbar_frame_view",
        "header_list_frame_view",
        "config_header_list_frame_view",
        "preset_frame_view",
    )

    def __init__(self, master: SidebarFrameView) -> None:
        super().__init__(
            master,
            corner_radius=Config.General.CORNER_RADIUS,
            border_width=Config.General.FRAME_BORDER_WIDTH,
            fg_color=Config.Colors.TRANSPARENT,
        )
        self.__initialize_widgets()
        self.__create_layout()

    def __initialize_widgets(self) -> None:
        """
        Initialize widgets.
        """
        self.filehandling_frame_view: FileHandlingFrameView = FileHandlingFrameView(
            self
        )
        self.searchbar_frame_view: SearchbarFrameView = SearchbarFrameView(self)
        self.header_list_frame_view: HeaderListFrameView = HeaderListFrameView(self)
        self.config_header_list_frame_view: ConfigHeaderListFrameView = (
            ConfigHeaderListFrameView(self)
        )
        self.preset_frame_view: PresetFrameView = PresetFrameView(self)

    def __create_layout(self) -> None:
        """
        Create layout.
        """
        self.grid_rowconfigure(
            (
                Config.Layout.HEADER_LIST_FRAME_ROW,
                Config.Layout.CONFIG_HEADER_LIST_FRAME_ROW,
            ),
            weight=1,
        )
        self.filehandling_frame_view.grid(
            row=Config.Layout.FILEHANDLING_FRAME_ROW,
            column=0,
            sticky=Config.Layout.GENERAL_FRAME_STICKY,
        )
        self.searchbar_frame_view.grid(
            row=Config.Layout.SEARCHBAR_FRAME_ROW,
            column=0,
            sticky=Config.Layout.GENERAL_FRAME_STICKY,
        )
        self.header_list_frame_view.grid(
            row=Config.Layout.HEADER_LIST_FRAME_ROW,
            column=0,
            sticky=Config.Layout.GENERAL_FRAME_STICKY,
        )
        self.config_header_list_frame_view.grid(
            row=Config.Layout.CONFIG_HEADER_LIST_FRAME_ROW,
            column=0,
            sticky=Config.Layout.GENERAL_FRAME_STICKY,
        )
        self.preset_frame_view.grid(
            row=Config.Layout.PRESET_FRAME_ROW,
            column=0,
            sticky=Config.Layout.GENERAL_FRAME_STICKY,
        )
