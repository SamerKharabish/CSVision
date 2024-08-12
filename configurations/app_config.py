"""Application configuration file."""

from .config import Config


class AppConfig:
    """
    Contains classes that define the specific configurations of the application.
    """

    class General:
        """
        General configurations.
        """

        TITLE: str = "CSVision"
        ICON: str = Config.General.ICON

    class Colors:
        """
        Background color, text color, etc.
        """

    class Dimensions:
        """
        Dimensions.
        """

        WIDTH: int = 1150
        HEIGHT: int = 666

        MIN_WIDTH: int = WIDTH - 200
        MIN_HEIGHT: int = HEIGHT - 200

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

        MAIN_VIEW: dict[str:str, str:str, str:bool] = {
            "side": "top",
            "fill": "both",
            "expand": True,
        }

    class Texts:
        """
        Any static text like label text, button text, etc.
        """

    class Typography:
        """
        Font sizes, font families, weights, etc.
        """

    class Widgets:
        """
        Arguments with values of each single widget.
        """
