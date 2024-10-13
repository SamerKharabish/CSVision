"""Defines the SidebarController class with the sidebar functionality."""

from views.sidebar_view import SidebarView
from .sidebar_controllers.filehandler_controller import (
    FileHandlerController,
)
from .sidebar_controllers.header_list_controller import (
    HeaderListController,
)


class SidebarController:
    """
    Functionality of the sidebar.
    """

    __slots__ = ("view",)

    def __init__(self, view: SidebarView) -> None:
        self.view: SidebarView = view

        FileHandlerController(self.view.file_handler_view)
        HeaderListController(self.view.header_list_frame_view)
