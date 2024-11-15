"""HeaderList configuration file."""

from typing import Literal
from .config import Config


class HeaderListConfig:
    """
    Contains classes that define the specific configurations of the header list.
    """

    class OwnArgs:
        """
        Arguments with values of self.
        """

        CORNER_RADIUS: int = Config.Widgets.CORNER_RADIUS
        BORDER_WIDTH: int = Config.Widgets.BORDER_WIDTH
        TRANSPARENT: str = Config.Colors.TRANSPARENT

        USER_SETTINGS: str = Config.General.USER_SETTINGS

        # TODO: Add this to the settings
        INITIAL_NR_OF_GROUPS: int = 20
        INITIAL_NR_OF_BUTTONS_PER_GROUP: int = 10
        MAX_BUTTONS_PER_GROUP: int = 20

    class Layout:
        """
        Layout.
        """

        FILTER_MODE_SEG_BUTTON: dict[str, str | None | bool | tuple[int, int]] = {
            "side": "bottom",
            "fill": None,
            "expand": False,
            "padx": (0, 0),
            "pady": (0, 7),
        }

        HEADER_SCROLLABLEFRAME: dict[str, str | bool | tuple[int, int] | int] = {
            "side": "top",
            "fill": "both",
            "expand": True,
            "padx": (7, 7),
            "pady": (1, 1),
            "column": 0,
            "column_weight": 1,
        }

        HEADER_SCROLLABLEFRAME_WIDGETS: dict[str, str | tuple[int, int]] = {
            "sticky": "nsew",
            "label_padx": (7, 7),
            "label_pady": (1, 1),
            "button_padx": (2, 2),
            "button_pady": (0, 3),
        }

    class Texts:
        """
        Any static text like label text, button text, etc.
        """

        FILTER_MODE_OPTIONS: list[str] = [
            "All",
            "Non const. zero",
            "Non const.",
        ]

    class Widgets:
        """
        Arguments with values of each single widget.
        """

        FILTER_MODE_SEG_BUTTON: dict[str, str | int | Literal["normal", "bold"]] = {
            "family": Config.Typography.DEFAULT_FAMILY,
            "size": Config.Typography.NORMAL_SIZE,
            "weight": "bold",
        }

        HEADER_SCROLLABLEFRAME: dict[str, str | int] = {
            "label_text": "HEADERS",
            "family": Config.Typography.DEFAULT_FAMILY,
            "size": Config.Typography.NORMAL_SIZE,
            "weight": "bold",
            "label_anchor": "w",
        }

        HEADER_SCROLLABLEFRAME_WIDGETS: dict[str, str | int] = {
            "family": Config.Typography.DEFAULT_FAMILY,
            "size": Config.Typography.NORMAL_SIZE,
            "weight": "bold",
            "label_anchor": "w",
            "button_height": 25,
            "button_corner_radius": 7,
            "initial_nr_of_groups": 20,
            "initial_nr_of_buttons_per_group": 10,
        }
