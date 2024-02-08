"""Centralized configuration file for the visual representation of the application."""


class Config:
    """
    Contains classes that define the configurations of the visual representation of the application.
    """

    class Titles:
        """
        Titles
        """

        APP_WINDOW_TITLE = "CSVision"

    class Radii:
        """
        Radii
        """

        OUTER_RADIUS = 8
        INNER_RADIUS = 6

    class Dimensions:
        """
        Dimensions
        """

        APP_WINDOW_WIDTH = 1150
        APP_WINDOW_MIN_WIDTH = APP_WINDOW_WIDTH
        APP_WINDOW_HEIGHT = 666
        APP_WINDOW_MIN_HEIGHT = APP_WINDOW_HEIGHT - 200

        SIGNAL_FRAME_WIDTH = APP_WINDOW_WIDTH * 0.25

        STATUSBAR_FRAME_HEIGHT = 30

    class Images:
        """
        Images
        """

        MAIN_WINDOW_ICON = "resources/Images/CSVision.ico"

    class Padding:
        """
        Padding
        """

        PADX = (8, 8)
        PADY = (8, 8)
        PADX_RIGHT_SHORT = (PADX[0], PADX[1] / 2)
        PADX_LEFT_SHORT = (PADX[0] / 2, PADX[1])
        PADY_TOP_SHORT = (PADY[0] / 2, PADY[1])
        PADY_BOTTOM_SHORT = (PADY[0], PADY[1] / 2)

    class Layout:
        """
        Layout
        """

        MAIN_VIEW_SIDE = "top"
        MAIN_VIEW_FILL = "both"
        MAIN_VIEW_EXPAND = True

        STATUSBAR_FRAME_SIDE = "bottom"
        STATUSBAR_FRAME_FILL = "x"
        STATUSBAR_FRAME_EXPAND = False

        SIGNAL_FRAME_SIDE = "left"
        SIGNAL_FRAME_FILL = "y"
        SIGNAL_FRAME_EXPAND = False

        PLOT_FRAME_SIDE = "right"
        PLOT_FRAME_FILL = "both"
        PLOT_FRAME_EXPAND = True
