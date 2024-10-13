"""Statusbar configuration file."""

from .config import Config


class StatusbarConfig:
    """
    Contains classes that define the specific configurations of the statusbar.
    """

    class OwnArgs:
        """
        Arguments with values of self.
        """

        CORNER_RADIUS: int = Config.Widgets.CORNER_RADIUS
        BORDER_WIDTH: int = Config.Widgets.BORDER_WIDTH
        TRANSPARENT: str = Config.Colors.TRANSPARENT

        HEIGHT: int = 20

    class Layout:
        """
        Layout.
        """

        FILESIZE_LABEL: dict[str, str | tuple[int, int]] = {
            "side": "left",
            "padx": (40, 0),
            "pady": (1, 1),
        }

        PROGRESSBAR: dict[str, str | tuple[int, int]] = {
            "side": "right",
            "padx": (20, 40),
            "pady": (7, 7),
        }

        PROGRESS_LABEL: dict[str, str | tuple[int, int]] = {
            "side": "right",
            "padx": (0, 0),
            "pady": (1, 1),
        }

    class Widgets:
        """
        Arguments with values of each single widget.
        """

        FILESIZE_LABEL: dict[str, str | int] = {
            "text": "",
            "family": Config.Typography.DEFAULT_FAMILY,
            "size": Config.Typography.NORMAL_SIZE,
        }

        PROGRESSBAR: dict[str, int] = {
            "width": 310,
        }

        PROGRESS_LABEL: dict[str, str | int] = {
            "text": "",
            "family": Config.Typography.DEFAULT_FAMILY,
            "size": Config.Typography.NORMAL_SIZE,
        }
