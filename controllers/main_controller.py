""" Defines the MainController class with the main functionality. """

from views.configurations_view import MainConfig
from views.main_view import MainView
from utils.helper_functions import find_root
from utils.observer_publisher import header_frame_state_publisher
from controllers.statusbar_frame_controller import StatusbarFrameController
from controllers.sidebar_frame_controller import SidebarFrameController
from controllers.plot_frame_controller import PlotFrameController


class MainController:
    """
    Functionality of the main application.
    """

    __slots__ = ("__view",)

    def __init__(self, view: MainView) -> None:
        self.__view: MainView = view
        self.__view.root = find_root(self.__view)

        self.__initialize_controller()
        self.__setup_bindings()

    def __initialize_controller(self) -> None:
        """
        Initialize controller.
        """
        StatusbarFrameController(self.__view.statusbar_frame_view)
        SidebarFrameController(self.__view.sidebar_frame_view)
        PlotFrameController(self.__view.plot_frame_view)

    def __setup_bindings(self) -> None:
        """
        Binding the MainView widgets to callback functions.
        """
        self.__view.root.bind(
            MainConfig.KeyBindings.RESIZE_HEADER_FRAME,
            self.__toggle_header_frame,
        )

    def __toggle_header_frame(self, _=None) -> None:
        """
        Toggle the visibility of the header frame.
        Bound to the Ctrl + B press event.
        """
        header_frame_state_publisher.hide_frame = (
            not header_frame_state_publisher.hide_frame
        )
