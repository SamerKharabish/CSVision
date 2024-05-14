""" Defines the HeaderFrameController class with the header frame functionality. """

from views.sidebar_views.header_frame_view import HeaderFrameView
from controllers.sidebar_controllers.filehandling_frame_controller import FileHandlingFrameController

class HeaderFrameController:
    """
    Functionality of the sidebar frame view.
    """

    __slots__ = ("__view",)

    def __init__(self, view: HeaderFrameView) -> None:
        self.__view: HeaderFrameView = view

        FileHandlingFrameController(self.__view.filehandling_frame_view)
