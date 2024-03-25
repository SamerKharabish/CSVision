""" Defines the MainController class with the main functionality. """

import customtkinter as ctk
from views.main_view import MainView
from views.configurations_view import Config
from controllers.statusbar_frame_controller import StatusbarFrameController
from controllers.signal_frame_controller import SignalFrameController
from controllers.plot_frame_controller import PlotFrameController


class MainController:
    """
    Functionality of the main application.
    """

    def __init__(self, master: ctk.CTk) -> None:
        self.__master: ctk.CTk = master
        self.__view: ctk.CTkFrame = MainView(master)

        self.__initialize_controller()
        self.__setup_bindings()

    def __initialize_controller(self) -> None:
        """
        Initialize controller.
        """
        self.statusbar_frame_controller: StatusbarFrameController = (
            StatusbarFrameController(self.__view.statusbar_frame_view)
        )
        self.signal_frame_controller: SignalFrameController = SignalFrameController(
            self.__view.signal_frame_view
        )
        self.plot_frame_controller: PlotFrameController = PlotFrameController(
            self.__view.plot_frame_view
        )

    def __setup_bindings(self) -> None:
        """
        Binding the MainView widgets to callback functions.
        """
        self.__master.bind(
            Config.KeyBindings.RESIZE_SIGNAL_FRAME,
            self.signal_frame_controller.on_toggle_side_bar,
        )
