""" Defines the SidebarFrameController class with the sidebar frame functionality. """

from views.sidebar_frame_view import SidebarFrameView
from utils.helper_functions import find_root
from utils.observer_publisher import (
    SimpleObserver,
    SimplePublisher,
    header_frame_state_publisher,
)
from controllers.sidebar_controller.navigation_frame_controller import (
    NavigationFrameController,
)
from controllers.sidebar_controller.header_frame_controller import (
    HeaderFrameController,
)


class SidebarFrameController(SimpleObserver):
    """
    Functionality of the sidebar frame view.
    """

    __slots__ = ("__view",)

    def __init__(self, view: SidebarFrameView) -> None:
        SimpleObserver.__init__(self)
        self.__view: SidebarFrameView = view

        self.__view.root = find_root(self.__view)

        header_frame_state_publisher.attach(self)

        self.__initialize_controller()

    def __initialize_controller(self) -> None:
        """
        Initialize controller.
        """
        NavigationFrameController(self.__view.navigation_frame_view)
        HeaderFrameController(self.__view.header_frame_view)

    def update(self, simple_publisher: SimplePublisher) -> None:
        if simple_publisher == header_frame_state_publisher:
            if header_frame_state_publisher.hide_frame:
                self.__view.root.after(0, self.__view.header_frame_view.pack_forget())
            else:
                self.__view.root.after(
                    0,
                    self.__view.header_frame_view.pack(
                        side="right", fill="y", expand=True
                    ),
                )
