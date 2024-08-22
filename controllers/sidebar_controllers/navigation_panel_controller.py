""" Defines the NavigationPanelController class with the navigation frame functionality. """

from PIL import Image
import customtkinter as ctk
from configurations.navigation_panel_config import NavigationPanelConfig as NPC
from views.sidebar_views.navigation_panel_view import NavigationPanelView
from views.sidebar_views.settings_window_view import SettingsWindowView
from utils.helper_functions import find_root
from utils.observer_publisher import (
    SimpleObserver,
    SimplePublisher,
    processor_panel_state_publisher,
)
from .settings_window_controller import (
    SettingsWindowController,
)


class NavigationPanelController(SimpleObserver):
    """
    Functionality of the navigation frame view.
    """

    __slots__ = "__view", "__settings_window_view", "__settings_window_controller"

    def __init__(self, view: NavigationPanelView) -> None:
        self.__view: NavigationPanelView = view

        self.__view.root = find_root(self.__view)

        processor_panel_state_publisher.attach(self)

        self.__initialize_settings_window()

        self.__view.processor_panel_toggle_button.configure(
            command=self.__toggle_processor_panel
        )

        self.__view.settings_button.configure(
            command=self.__settings_window_controller.update_settings_geometries
        )

    def __initialize_settings_window(self) -> None:
        """
        Initialize the settings window.
        """
        self.__settings_window_view: SettingsWindowView = SettingsWindowView(
            self.__view.root
        )
        self.__settings_window_controller: SettingsWindowController = (
            SettingsWindowController(self.__settings_window_view)
        )

    def __toggle_processor_panel(self) -> None:
        """
        Toggle the visibility of the processor panel.
        """
        processor_panel_state_publisher.hide_panel = (
            not processor_panel_state_publisher.hide_panel
        )

        self.__toggle_image()

    def __toggle_image(self) -> None:
        """
        Toggle the image of the processor_panel_toggle_button.
        """
        if processor_panel_state_publisher.hide_panel:
            self.__view.root.after(
                0,
                self.__view.processor_panel_toggle_button.configure(
                    image=ctk.CTkImage(
                        light_image=Image.open(
                            NPC.Widgets.PROCESSOR_PANEL_TOGGLE_BUTTON["show_image"]
                        ),
                        size=NPC.Widgets.PROCESSOR_PANEL_TOGGLE_BUTTON["size"],
                    )
                ),
            )
        else:
            self.__view.root.after(
                0,
                self.__view.processor_panel_toggle_button.configure(
                    image=ctk.CTkImage(
                        light_image=Image.open(
                            NPC.Widgets.PROCESSOR_PANEL_TOGGLE_BUTTON["hide_image"]
                        ),
                        size=NPC.Widgets.PROCESSOR_PANEL_TOGGLE_BUTTON["size"],
                    )
                ),
            )

    def update(self, simple_publisher: SimplePublisher) -> None:
        if simple_publisher == processor_panel_state_publisher:
            self.__toggle_image()

    def __del__(self) -> None:
        processor_panel_state_publisher.detach(self)
