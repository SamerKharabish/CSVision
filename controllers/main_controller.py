""" Defines the MainController class with the main functionality. """

from typing import Any
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

    def __init__(self, master: ctk.CTk = None) -> None:
        self.master: ctk.CTk = master
        self.view: ctk.CTkFrame = MainView(master)

        self.initialize_widgets()
        self.setup_bindings()

    def initialize_widgets(self) -> None:
        """
        Initialize widgets.
        """
        self.statusbar_frame_controller: Any = StatusbarFrameController(
            self.view.statusbar_frame_view
        )
        self.signal_frame_controller: Any = SignalFrameController(
            self.view.signal_frame_view
        )
        self.plot_frame_controller: Any = PlotFrameController(self.view.plot_frame_view)

    def setup_bindings(self) -> None:
        """
        Binding the MainView widgets to callback functions.
        """
        self.master.bind(
            Config.KeyBindings.RESIZE_SIGNAL_FRAME,
            self.signal_frame_controller.on_toggle_side_bar,
        )
