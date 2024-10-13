"""Navigation bar configuration file."""

from .config import Config


class NavBarConfig:
    """
    Contains classes that define the specific configurations of the navigation bar.
    """

    class OwnArgs:
        """
        Arguments with values of self.
        """

        CORNER_RADIUS: int = Config.Widgets.CORNER_RADIUS
        BORDER_WIDTH: int = Config.Widgets.BORDER_WIDTH
        TRANSPARENT: str = Config.Colors.TRANSPARENT

    class Layout:
        """
        Layout.
        """

        SIDEBAR_TOGGLE_BUTTON: dict[str, str | bool | tuple[int, int]] = {
            "side": "top",
            "fill": "x",
            "expand": False,
            "padx": (3, 3),
            "pady": (7, 7),
        }

        SETTINGS_BUTTON: dict[str, str | bool | tuple[int, int]] = {
            "side": "bottom",
            "fill": "x",
            "expand": False,
            "padx": (3, 3),
            "pady": (7, 7),
        }

    class Widgets:
        """
        Arguments with values of each single widget.
        """

        SIDEBAR_TOGGLE_BUTTON: dict[str, int | str | bool | tuple[int, int]] = {
            "width": Config.Dimensions.SQUARE_BUTTON_WIDTH_HEIGHT,
            "height": Config.Dimensions.SQUARE_BUTTON_WIDTH_HEIGHT,
            "fg_color": Config.Colors.TRANSPARENT,
            "hover_color": Config.Colors.ONYX_LIGHT,
            "text": "",
            "hide_image": "resources/Images/hide-sidebar.png",
            "show_image": "resources/Images/show-sidebar.png",
            "size": (20, 20),
            "anchor": "center",
        }

        SETTINGS_BUTTON: dict[str, int | str | bool | tuple[int, int]] = {
            "width": Config.Dimensions.SQUARE_BUTTON_WIDTH_HEIGHT,
            "height": Config.Dimensions.SQUARE_BUTTON_WIDTH_HEIGHT,
            "fg_color": Config.Colors.TRANSPARENT,
            "hover_color": Config.Colors.ONYX_LIGHT,
            "text": "",
            "light_image": "resources/Images/settings.png",
            "size": (20, 20),
            "anchor": "center",
        }
