"""Defines the NavigationPanelController class with the navigation frame functionality."""

from utils.observer_publisher import (
    SimpleObserver,
    SimplePublisher,
    sidebar_state_publisher,
)
from views.navbar_view import NavigationBarView
from .sidebar_controllers.settings_window_controller import (
    SettingsWindowController,
)


class NavigationBarController(SimpleObserver):
    """
    Functionality of the navigation frame view.
    """

    __slots__ = "view", "settings_window_view", "settings_window_controller"

    def __init__(self, view: NavigationBarView) -> None:
        self.view: NavigationBarView = view

        sidebar_state_publisher.attach(self)

        self.settings_window_controller: SettingsWindowController = (
            SettingsWindowController(self.view.root)
        )

        self.view.toggle_sidebar_button.configure(command=self.toggle_image_event)

        self.view.settings_button.configure(
            command=self.settings_window_controller.update_settings_geometries
        )

    def toggle_image_event(self) -> None:
        """
        Trigger the event of toggling the image of the toggle_sidebar_button.
        """
        self.view.toggle_image()
        sidebar_state_publisher.toggle_sidebar_visibility(self)

    def update(self, simple_publisher: SimplePublisher) -> None:
        if simple_publisher == sidebar_state_publisher:
            if sidebar_state_publisher.get_visibility() is True:
                self.view.set_hide_image()
            else:
                self.view.set_show_image()

    def __del__(self) -> None:
        sidebar_state_publisher.detach(self)
