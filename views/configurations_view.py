"""Centralized configuration file for the visual representation of the application."""


class Config:
    """
    Contains classes that define the configurations of the visual representation of the application.
    """

    class Titles:
        """
        Titles
        """

        MAIN_WINDOW_TITLE = "CSVision"

    class Radii:
        """
        Radii
        """

        CONTENT_FRAME_RADIUS = 8

    class Dimensions:
        """
        Dimensions
        """

        MAIN_WINDOW_WIDTH = 1150
        MAIN_WINDOW_MIN_WIDTH = MAIN_WINDOW_WIDTH
        MAIN_WINDOW_HEIGHT = 666
        MAIN_WINDOW_MIN_HEIGHT = MAIN_WINDOW_HEIGHT - 200

    class Images:
        """
        Images
        """

        MAIN_WINDOW_ICON = "resources/Images/CSVision.ico"
