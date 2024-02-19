"""Centralized configuration file for the visual representation of the application."""


class Config:
    """
    Contains classes that define the configurations of the visual representation of the application.
    """

    class General:
        """
        General configurations.
        """

        CORNER_RADIUS: int = 0
        BORDER_WIDTH: int = 1

    class Titles:
        """
        Titles
        """

        APP_WINDOW_TITLE: str = "CSVision"

    class Dimensions:
        """
        Dimensions
        """

        APP_WINDOW_WIDTH: int = 1150
        APP_WINDOW_MIN_WIDTH: int = APP_WINDOW_WIDTH
        APP_WINDOW_HEIGHT: int = 666
        APP_WINDOW_MIN_HEIGHT: int = APP_WINDOW_HEIGHT - 200

        SIGNAL_FRAME_WIDTH: int = int(APP_WINDOW_WIDTH * 0.25)
        SIGNAL_FRAME_MIN_WIDTH: int = 50

        STATUSBAR_FRAME_HEIGHT: int = 30

    class Images:
        """
        Images
        """

        MAIN_WINDOW_ICON: str = "resources/Images/CSVision.ico"

    class Layout:
        """
        Layout
        """

        MAIN_VIEW_SIDE: str = "top"
        MAIN_VIEW_FILL: str = "both"
        MAIN_VIEW_EXPAND: bool = True

        STATUSBAR_FRAME_SIDE: str = "bottom"
        STATUSBAR_FRAME_FILL: str = "x"
        STATUSBAR_FRAME_EXPAND: bool = False

        SIGNAL_FRAME_SIDE: str = "left"
        SIGNAL_FRAME_FILL: str = "y"
        SIGNAL_FRAME_EXPAND: bool = False

        PLOT_FRAME_SIDE: str = "right"
        PLOT_FRAME_FILL: str = "both"
        PLOT_FRAME_EXPAND: bool = True

    class KeyBindings:
        """
        Key bindings
        """

        CLOSE_APPLICATION: str = "<Escape>"
        RESIZE_SIGNAL_FRAME: str = "<Control-b>"
