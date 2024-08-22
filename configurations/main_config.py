"""Main configuration file."""

from .config import Config


class MainConfig:
    """
    Contains classes that define the specific configurations of the main window.
    """

    class General:
        """
        General configurations.
        """

    class OwnArgs:
        """
        Arguments with values of self.
        """

        CORNER_RADIUS: int = Config.Widgets.CORNER_RADIUS

    class Colors:
        """
        Background color, text color, etc.
        """

    class Dimensions:
        """
        Dimensions.
        """

    class Images:
        """
        Images.
        """

    class KeyBindings:
        """
        Key bindings.
        """

        RESIZE_SIDEBAR: str = "<Control-b>"

    class Layout:
        """
        Layout.
        """

        STATUSBAR_VIEW: dict[str:str, str:str, str:bool] = {
            "side": "bottom",
            "fill": "x",
            "expand": False,
        }

        SIDEBAR_VIEW: dict[str:str, str:str, str:bool] = {
            "side": "left",
            "fill": "y",
            "expand": False,
        }

        PLOT_VIEW: dict[str:str, str:str, str:bool] = {
            "side": "right",
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
