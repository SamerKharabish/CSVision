"""Statusbar configuration file."""

from .config import Config


class StatusbarConfig:
    """
    Contains classes that define the specific configurations of the statusbar.
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

        HEIGHT: int = 20

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

        FILESIZE_LABEL: dict[str:str, str : tuple[int, int], str : tuple[int, int]] = {
            "side": "left",
            "padx": (40, 0),
            "pady": (1, 1),
        }

        PROGRESSBAR: dict[str:str, str : tuple[int, int], str : tuple[int, int]] = {
            "side": "right",
            "padx": (20, 40),
            "pady": (7, 7),
        }

        PROGRESS_LABEL: dict[str:str, str : tuple[int, int], str : tuple[int, int]] = {
            "side": "right",
            "padx": (0, 0),
            "pady": (1, 1),
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

        FILESIZE_LABEL: dict[str:str, str:str, str:int] = {
            "text": "",
            "family": Config.Typography.DEFAULT_FAMILIY,
            "size": Config.Typography.NORMAL_SIZE,
        }

        PROGRESSBAR: dict[str:int] = {
            "width": 310,
        }

        PROGRESS_LABEL: dict[str:str, str:str, str:int] = {
            "text": "",
            "family": Config.Typography.DEFAULT_FAMILIY,
            "size": Config.Typography.NORMAL_SIZE,
        }
