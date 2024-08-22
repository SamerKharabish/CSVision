""" Defines the MainController class with the main functionality. """

from configurations.main_config import MainConfig
from utils.helper_functions import find_root
from utils.observer_publisher import processor_panel_state_publisher
from views.main_view import MainView
from .statusbar_controller import StatusbarController
from .sidebar_controller import SidebarController
from .plot_frame_controller import PlotController


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
        StatusbarController(self.__view.statusbar_view)
        SidebarController(self.__view.sidebar_view)
        PlotController(self.__view.plot_view)

    def __setup_bindings(self) -> None:
        """
        Binding the MainView widgets to callback functions.
        """
        self.__view.root.bind(
            MainConfig.KeyBindings.RESIZE_SIDEBAR,
            self.__toggle_processor_panel,
        )

    def __toggle_processor_panel(self, _=None) -> None:
        """
        Toggle the visibility of the processor panel.
        Bound to the Ctrl + B press event.
        """
        processor_panel_state_publisher.hide_panel = (
            not processor_panel_state_publisher.hide_panel
        )
