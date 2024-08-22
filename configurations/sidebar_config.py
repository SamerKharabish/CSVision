"""Sidebar configuration file."""

from .config import Config


class SidebarConfig:
    """
    Contains classes that define the specific configurations of the sidebar.
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
        BORDER_WIDTH: int = Config.Widgets.BORDER_WIDTH
        TRANSPARENT: str = Config.Colors.TRANSPARENT

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

    class Widgets:
        """
        Arguments with values of each single widget.
        """
        NAVIGATION_PANEL_VIEW: dict[str:str, str:str, str:bool] = {
            "side": "left",
            "fill": "y",
            "expand": False,
        }

        PROCESSOR_PANEL_VIEW: dict[str:str, str:str, str:bool] = {
            "side": "right",
            "fill": "both",
            "expand": True,
        }
