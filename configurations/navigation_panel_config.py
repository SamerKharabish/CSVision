"""Navigation panel configuration file."""

from .config import Config


class NavigationPanelConfig:
    """
    Contains classes that define the specific configurations of the navigation panel.
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

        PROCESSOR_PANEL_TOGGLE_BUTTON: dict[
            str:str, str:str, str:bool, str : tuple[int, int], str : tuple[int, int]
        ] = {
            "side": "top",
            "fill": "x",
            "expand": False,
            "padx": (3, 3),
            "pady": (7, 7),
        }

        SETTINGS_BUTTON: dict[
            str:str, str:str, str:bool, str : tuple[int, int], str : tuple[int, int]
        ] = {
            "side": "bottom",
            "fill": "x",
            "expand": False,
            "padx": (3, 3),
            "pady": (7, 7),
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

        PROCESSOR_PANEL_TOGGLE_BUTTON: dict[
            str:int,
            str:int,
            str:str,
            str:str,
            str:str,
            str:str,
            str:str,
            str : tuple[int, int],
            str:str,
        ] = {
            "width": Config.Dimensions.SQUARE_BUTTON_WIDTH_HEIGHT,
            "height": Config.Dimensions.SQUARE_BUTTON_WIDTH_HEIGHT,
            "fg_color": Config.Colors.TRANSPARENT,
            "hover_color": Config.Colors.ONYX_LIGHT,
            "text": "",
            "hide_image": "resources/Images/hide-sidepanel.png",
            "show_image": "resources/Images/show-sidepanel.png",
            "size": (20, 20),
            "anchor": "center",
        }

        SETTINGS_BUTTON: dict[
            str:int,
            str:int,
            str:str,
            str:str,
            str:str,
            str:str,
            str : tuple[int, int],
            str:str,
        ] = {
            "width": Config.Dimensions.SQUARE_BUTTON_WIDTH_HEIGHT,
            "height": Config.Dimensions.SQUARE_BUTTON_WIDTH_HEIGHT,
            "fg_color": Config.Colors.TRANSPARENT,
            "hover_color": Config.Colors.ONYX_LIGHT,
            "text": "",
            "light_image": "resources/Images/settings.png",
            "size": (20, 20),
            "anchor": "center",
        }
