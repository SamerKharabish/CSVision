"""Defines the MainController class with the main functionality."""

from configurations.main_config import MainConfig
from utils.observer_publisher import (
    SimpleObserver,
    SimplePublisher,
    sidebar_state_publisher,
    ProgressStatePublisher,
    progress_state_publisher,
)
from views.main_view import MainView
from .navbar_controller import NavigationBarController
from .plot_frame_controller import PlotController
from .sidebar_controller import (
    SidebarController,
)
from .statusbar_controller import StatusbarController


class MainController(SimpleObserver):
    """
    Functionality of the main application.
    """

    __slots__ = ("view",)

    def __init__(self, view: MainView) -> None:
        SimpleObserver.__init__(self)
        self.view: MainView = view

        sidebar_state_publisher.attach(self)
        progress_state_publisher.attach(self)

        self.initialize_controller()
        self.setup_bindings()

    def initialize_controller(self) -> None:
        """
        Initialize controller.
        """
        NavigationBarController(self.view.nav_bar_view)
        PlotController(self.view.plot_view)
        SidebarController(self.view.sidebar_view)
        StatusbarController(self.view.statusbar_view)

    def setup_bindings(self) -> None:
        """
        Binding the MainView widgets to callback functions.
        """
        self.view.root.bind(
            MainConfig.KeyBindings.RESIZE_SIDEBAR,
            self.toggle_sidebar_event,
        )

    def toggle_sidebar_event(self, _=None) -> None:
        """
        Trigger the event of toggling the sidebar.
        """
        self.view.toggle_sidebar()
        sidebar_state_publisher.toggle_sidebar_visibility(self)

    def update(self, simple_publisher: SimplePublisher) -> None:
        if simple_publisher == sidebar_state_publisher:
            if sidebar_state_publisher.get_visibility():
                self.view.show_sidebar()
            else:
                self.view.hide_sidebar()
        if simple_publisher == progress_state_publisher:
            if (
                progress_state_publisher.value
                == ProgressStatePublisher.START_PROGRESSBAR
            ):
                # TODO: Disable / hide / overlay / ... user input widgets
                pass
            elif (
                progress_state_publisher.value
                == ProgressStatePublisher.STOP_PROGRESSBAR
            ):
                # TODO: Enable / show / remove overlay / ... user input widgets
                pass

    def __del__(self) -> None:
        sidebar_state_publisher.detach(self)
        progress_state_publisher.detach(self)
