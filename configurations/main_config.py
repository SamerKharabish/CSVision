"""Main configuration file."""

from .config import Config


class MainConfig:
    """
    Contains classes that define the specific configurations of the main window.
    """

    class OwnArgs:
        """
        Arguments with values of self.
        """

        CORNER_RADIUS: int = Config.Widgets.CORNER_RADIUS

    class KeyBindings:
        """
        Key bindings.
        """

        RESIZE_SIDEBAR: str = "<Control-b>"

    class Layout:
        """
        Layout.
        """

        NAV_BAR_VIEW: dict[str, str | bool] = {
            "side": "left",
            "fill": "y",
            "expand": False,
        }

        PLOT_VIEW: dict[str, str | bool] = {
            "side": "right",
            "fill": "both",
            "expand": True,
        }

        SIDEBAR_VIEW: dict[str, str | bool] = {
            "side": "left",
            "fill": "y",
            "expand": False,
        }

        STATUSBAR_VIEW: dict[str, str | bool] = {
            "side": "bottom",
            "fill": "x",
            "expand": False,
        }

    class Widgets:
        """
        Arguments with values of each single widget.
        """

        OVERLAY: dict[str, str | int] = {
            "corner_radius": Config.Widgets.CORNER_RADIUS,
            "border_width": Config.Widgets.BORDER_WIDTH,
            "fg_color": Config.Colors.TRANSPARENT,
        }
