"""Centralized configuration file."""


class Config:
    """
    Contains classes that define the general configurations of the application.
    """

    class General:
        """
        General configurations.
        """

        ICON: str = "resources/Images/CSVision.ico"

    class Colors:
        """
        Background color, text color, etc.
        """

        TRANSPARENT: str = "transparent"
        ONYX_LIGHT: str = "#3D3E40"

    class Dimensions:
        """
        Dimensions.
        """

        SQUARE_BUTTON_WIDTH_HEIGHT: int = 10

    class Images:
        """
        Images.
        """

    class KeyBindings:
        """
        Key bindings.
        """

    class Layout:
        """
        Layout.
        """

    class Texts:
        """
        Any static text like label text, button text, etc.
        """

    class Typography:
        """
        Font sizes, font families, weights, etc.
        """

        DEFAULT_FAMILY: str = "Kento"

    class Widgets:
        """
        Arguments with values of each single widget.
        """

        CORNER_RADIUS: int = 0
        BORDER_WIDTH: int = 1
