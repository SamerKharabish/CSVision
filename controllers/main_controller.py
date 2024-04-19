""" Defines the MainController class with the main functionality. """

from views.configurations_view import Config
from views.main_view import MainView
from utils.helper_functions import find_root
from controllers.statusbar_frame_controller import StatusbarFrameController
from controllers.signal_frame_controller import SignalFrameController
from controllers.plot_frame_controller import PlotFrameController


class MainController:
    """
    Functionality of the main application.
    """

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
        self.__signal_frame_controller: SignalFrameController = SignalFrameController(
            self.__view.signal_frame_view
        )
        PlotFrameController(self.__view.plot_frame_view)

    def __setup_bindings(self) -> None:
        """
        Binding the MainView widgets to callback functions.
        """
        self.__view.root.bind(
            Config.KeyBindings.RESIZE_SIGNAL_FRAME,
            self.__signal_frame_controller.on_toggle_side_bar,
        )
