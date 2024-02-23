"""Centralized configuration file for the visual representation of the application."""

from typing import Tuple, List


class Config:
    """
    Contains classes that define the configurations of the visual representation of the application.
    """

    class General:
        """
        General configurations.
        """

        CORNER_RADIUS: int = 0
        FRAME_BORDER_WIDTH: int = 1
        INPUT_ENTRY_BORDER_WIDTH: int = 0
        OUTPUT_ENTRY_BORDER_WIDTH: int = 1

    class WindowTitles:
        """
        Titles
        """

        APP_WINDOW_TITLE: str = "CSVision"

    class Dimensions:
        """
        Dimensions
        """

        APP_WINDOW_WIDTH: int = 1150
        APP_WINDOW_MIN_WIDTH: int = APP_WINDOW_WIDTH
        APP_WINDOW_HEIGHT: int = 666
        APP_WINDOW_MIN_HEIGHT: int = APP_WINDOW_HEIGHT - 200

        SIGNAL_FRAME_MIN_WIDTH: int = 40

        STATUSBAR_FRAME_HEIGHT: int = 20

        ACTION_BUTTON_WIDTH_HEIGHT: int = 10
        ACTION_IMAGE_WIDTH_HEIGHT: int = 17

    class ImageFormats:
        """
        Image formats
        """

        MAIN_WINDOW_ICO: str = "resources/Images/CSVision.ico"
        CLEAR_SEARCH_RESULT_PNG: str = "resources/Images/clear-search-results.png"
        DOWN_ARROW_PNG: str = "resources/Images/down-arrow.png"
        EXCEL_PNG: str = "resources/Images/excel.png"
        OPEN_FILE_PNG: str = "resources/Images/open-file.png"
        REFRESH_PNG: str = "resources/Images/refresh.png"

    class Layout:
        """
        Layout
        """

        MAIN_VIEW_SIDE: str = "top"
        MAIN_VIEW_FILL: str = "both"
        MAIN_VIEW_EXPAND: bool = True

        STATUSBAR_FRAME_SIDE: str = "bottom"
        STATUSBAR_FRAME_FILL: str = "x"
        STATUSBAR_FRAME_EXPAND: bool = False

        SIGNAL_FRAME_SIDE: str = "left"
        SIGNAL_FRAME_FILL: str = "y"
        SIGNAL_FRAME_EXPAND: bool = False

        PLOT_FRAME_SIDE: str = "right"
        PLOT_FRAME_FILL: str = "both"
        PLOT_FRAME_EXPAND: bool = True

        FILEHANDLING_FRAME_ROW: int = 0
        SEARCHBAR_FRAME_ROW: int = 1
        SIGNALLIST_FRAME_ROW: int = 2
        CONFIG_SIGNALLIST_FRAME_ROW: int = 3
        GENERAL_FRAME_STICKY: str = "nesw"

        SEARCHBAR_TITLE_FARME_ROW: int = 0
        SEARCHBAR_ENTRY_ROW: int = 1
        SEARCHBAR_FILTER_FARME_ROW: int = 2
        FILEHANDLING_TITLE_FARME_ROW: int = 0
        FILEHANDLING_ENTRY_ROW: int = 1
        FILEHANDLING_FILTER_FARME_ROW: int = 2
        CONFIG_SIGNALLIST_SCROLLABLE_FRAME_ROW: int = 0
        CONFIG_SIGNALLIST_PRESET_FRAME_ROW: int = 1
        GENERAL_INNER_FRAME_STICKY: str = "ew"

        SIGNAL_FRAME_LABELS_ANCHOR: str = "w"
        ACTION_BUTTON_TEXT_ANCHOR: str = "center"
        STANDART_PAD: Tuple[int, int] = (7, 7)
        ZERO_PAD: Tuple[int, int] = (0, 0)
        LABELS_IN_FRAME_PADX: Tuple[int, int] = (14, 0)

        SIGNAL_FRAME_SCROLLABLEFRAME_SIDE: str = "top"
        SIGNAL_FRAME_SCROLLABLEFRAME_FILL: str = "both"
        SIGNAL_FRAME_SCROLLABLEFRAME_EXPAND: bool = True
        SIGNAL_FRAME_SCROLLABLEFRAME_PADX: Tuple[int, int] = (1, 1)
        SIGNAL_FRAME_SCROLLABLEFRAME_PADY: Tuple[int, int] = (1, 1)

    class KeyBindings:
        """
        Key bindings
        """

        CLOSE_APPLICATION: str = "<Escape>"
        RESIZE_SIGNAL_FRAME: str = "<Control-b>"

    class LabelTexts:
        """
        Label texts
        """

        FILEHANDLING_TEXT: str = "EXPLORER"
        SEARCHBAR_TEXT: str = "SEARCH"
        SIGNALLIST_TEXT: str = f"{'SIGNALS':>9}"
        CONFIG_SIGNALLIST_TEXT: str = f"{'CONFIGURATIONS':>16}"

    class Fonts:
        """
        Fonts
        """

        LABEL_TEXTS: Tuple[str, int] = ("Calibri", 14)
        BUTTON_TEXTS: Tuple[str, int, str] = ("Calibri", 14, "bold")

    class Colors:
        """
        Colors
        """

        TRANSPARENT: str = "transparent"
        ONYX: str = "#343638"
        TRANSPARENT_BUTTON_HOVER: str = "#3E3E3E"
        BORDER_COLOR: str = "#6C6C6C"
        COLORED_BUTTON_HOVER: str = "#3D3E40"

    class Values:
        """
        Values of different widgets.
        """

        SEARCH_SELECTION_SEGMENTED_BUTTON: List[str] = ["Signals", "Groups"]
        FILTER_SIGNALS_SEGMENTED_BUTTON: List[str] = [
            "All",
            "Non const. zero",
            "Non const.",
        ]
        FILE_OPTIONMENU: List[str] = [" "]
        FILE_ACTION_OPTIONMENU: List[str] = [
            "OPEN FILE",
            "LOAD FILE",
            "EXPORT to EXCEL",
        ]
