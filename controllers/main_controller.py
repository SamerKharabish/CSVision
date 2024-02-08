""" Defines the MainController class with the main functionality. """

from views.main_view import MainView
from controllers.statusbar_frame_controller import StatusbarFrameController
from controllers.signal_frame_controller import SignalFrameController
from controllers.plot_frame_controller import PlotFrameController


class MainController:
    """
    Functionality of the main application.
    """

    def __init__(self, master=None) -> None:
        self.view = MainView(master)

        self.initialize_widgets()

    def initialize_widgets(self):
        """
        Initialize widgets.
        """
        self.statusbar_frame_controller = StatusbarFrameController(
            self.view.statusbar_frame_view
        )
        self.signal_frame_controller = SignalFrameController(
            self.view.signal_frame_view
        )
        self.plot_frame_controller = PlotFrameController(self.view.plot_frame_view)
