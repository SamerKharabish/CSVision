""" Defines the NavigationFrameController class with the navigation frame functionality. """

from PIL import Image
import customtkinter as ctk
from views.configurations_view import Config
from views.sidebar_views.navigation_frame_view import NavigationFrameView
from utils.helper_functions import find_root
from utils.observer_publisher import (
    SimpleObserver,
    SimplePublisher,
    header_frame_state_publisher,
)


class NavigationFrameController(SimpleObserver):
    """
    Functionality of the navigation frame view.
    """

    __slots__ = ("__view",)

    def __init__(self, view: NavigationFrameView) -> None:
        self.__view: NavigationFrameView = view

        header_frame_state_publisher.attach(self)

        self.__view.toggle_header_button.configure(
            command=self.__on_toggle_header_frame
        )

        self.__view.root = find_root(self.__view)

    def update(self, simple_publisher: SimplePublisher) -> None:
        if simple_publisher == header_frame_state_publisher:
            self.__toggle_image()

    def __on_toggle_header_frame(self) -> None:
        """
        Toggle the image of the toggle-button of the header frame.
        """
        header_frame_state_publisher.hide_frame = (
            not header_frame_state_publisher.hide_frame
        )

        self.__toggle_image()

    def __toggle_image(self) -> None:
        """
        Toggle the image of the toggle header button.
        """
        if header_frame_state_publisher.hide_frame:
            self.__view.root.after(
                0,
                self.__view.toggle_header_button.configure(
                    image=ctk.CTkImage(
                        light_image=Image.open(
                            Config.ImageFormats.SHOW_HEADER_FRAME_BUTTON_PNG
                        ),
                        size=(
                            Config.Dimensions.TOGGLE_HEADER_FRAME_BUTTON_WIDTH_HEIGHT,
                            Config.Dimensions.TOGGLE_HEADER_FRAME_BUTTON_WIDTH_HEIGHT,
                        ),
                    )
                ),
            )
        else:
            self.__view.root.after(
                0,
                self.__view.toggle_header_button.configure(
                    image=ctk.CTkImage(
                        light_image=Image.open(
                            Config.ImageFormats.HIDE_HEADER_FRAME_BUTTON_PNG
                        ),
                        size=(
                            Config.Dimensions.TOGGLE_HEADER_FRAME_BUTTON_WIDTH_HEIGHT,
                            Config.Dimensions.TOGGLE_HEADER_FRAME_BUTTON_WIDTH_HEIGHT,
                        ),
                    )
                ),
            )