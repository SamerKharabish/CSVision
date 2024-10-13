"""Sidebar configuration file."""

from .config import Config


class SidebarConfig:
    """
    Contains classes that define the specific configurations of the sidebar.
    """

    class OwnArgs:
        """
        Arguments with values of self.
        """

        CORNER_RADIUS: int = Config.Widgets.CORNER_RADIUS
        BORDER_WIDTH: int = Config.Widgets.BORDER_WIDTH
        TRANSPARENT: str = Config.Colors.TRANSPARENT

        FILEHANDLER_FRAME_ROW: int = 0
        SEARCHBAR_FRAME_ROW: int = 1
        HEADER_LIST_FRAME_ROW: int = 2
        CONFIG_HEADER_LIST_FRAME_ROW: int = 3
        PRESET_FRAME_ROW: int = 4

        ROWS_RESIZE: tuple[int, int] = (
            HEADER_LIST_FRAME_ROW,
            CONFIG_HEADER_LIST_FRAME_ROW,
        )
        ROWS_RESIZE_WEIGHT: int = 1

        ROWS_FIXED: tuple[int, int, int] = (
            FILEHANDLER_FRAME_ROW,
            SEARCHBAR_FRAME_ROW,
            PRESET_FRAME_ROW,
        )
        ROWS_FIXED_WEIGHT: int = 0

        COLUMN: int = 0
        STICKY: str = "nsew"
