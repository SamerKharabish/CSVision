""" Defines the SidebarController class with the sidebar frame functionality. """

from configurations.sidebar_config import SidebarConfig
from views.sidebar_view import SidebarView
from utils.helper_functions import find_root
from utils.observer_publisher import (
    SimpleObserver,
    SimplePublisher,
    processor_panel_state_publisher,
)
from .sidebar_controllers.navigation_panel_controller import (
    NavigationPanelController,
)
from .sidebar_controllers.header_frame_controller import (
    ProcessorPanelController,
)


class SidebarController(SimpleObserver):
    """
    Functionality of the sidebar frame view.
    """

    __slots__ = ("__view",)

    def __init__(self, view: SidebarView) -> None:
        SimpleObserver.__init__(self)
        self.__view: SidebarView = view

        self.__view.root = find_root(self.__view)

        processor_panel_state_publisher.attach(self)

        self.__initialize_controller()

    def __initialize_controller(self) -> None:
        """
        Initialize controller.
        """
        NavigationPanelController(self.__view.navigation_panel_view)
        ProcessorPanelController(self.__view.processor_panel_view)

    def update(self, simple_publisher: SimplePublisher) -> None:
        # Toggle the visibility of the processor panel when the Ctrl + B press
        # event tiggered or the processor_panel_toggle_button was pressed
        if simple_publisher == processor_panel_state_publisher:
            # Hide the processor panel
            if processor_panel_state_publisher.hide_panel:
                self.__view.root.after(
                    0, self.__view.processor_panel_view.pack_forget()
                )
            # Show the processor panel
            else:
                self.__view.root.after(
                    0,
                    self.__view.processor_panel_view.pack(
                        side=SidebarConfig.Widgets.PROCESSOR_PANEL_VIEW["side"],
                        fill=SidebarConfig.Widgets.PROCESSOR_PANEL_VIEW["fill"],
                        expand=SidebarConfig.Widgets.PROCESSOR_PANEL_VIEW["expand"],
                    ),
                )

    def __del__(self) -> None:
        processor_panel_state_publisher.detach(self)
