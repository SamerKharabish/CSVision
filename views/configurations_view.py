"""Centralized configuration file for the visual representation of the application."""

from typing import Tuple


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
        ENTRY_BORDER_WIDTH: int = 0

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

        SIGNAL_FRAME_WIDTH: int = int(APP_WINDOW_WIDTH * 0.25)
        SIGNAL_FRAME_MIN_WIDTH: int = 40

        STATUSBAR_FRAME_HEIGHT: int = 20

        FILEHANDLING_FRAME_HEIGHT: int = 80
        SEARCHBAR_FRAME_HEIGHT: int = FILEHANDLING_FRAME_HEIGHT

        ACTION_BUTTON_WIDTH_HEIGHT: int = 10
        ACTION_IMAGE_WIDTH_HEIGHT: int = 17

    class ImageFormats:
        """
        Image formats
        """

        MAIN_WINDOW_ICON: str = "resources/Images/CSVision.ico"
        CLEAR_SEARCH_RESULT_ICON = "resources/Images/clear-search-results.png"
        DOWN_ARROW = "resources/Images/down-arrow.png"

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
        FILEHANDLING_FRAME_STICKY: str = "ew"
        SEARCHBAR_FRAME_ROW: int = 1
        SEARCHBAR_FRAME_STICKY: str = "ew"
        SIGNALLIST_FRAME_ROW: int = 2
        SIGNALLIST_FRAME_STICKY: str = "nesw"
        CONFIG_SIGNALLIST_FRAME_ROW: int = 3
        CONFIG_SIGNALLIST_FRAME_STICKY: str = "nesw"

        SEARCHBAR_FRAME_TITLE_FARME_ROW: int = 0
        SEARCHBAR_FRAME_ENTRY_ROW: int = 1
        SEARCHBAR_FRAME_FILTER_FARME_ROW: int = 2
        FILEHANDLING_TITLE_FARME_ROW: int = 0
        FILEHANDLING_ENTRY_ROW: int = 1
        FILEHANDLING_FILTER_FARME_ROW: int = 2
        GENERAL_FRAME_STICKY: str = "ew"

        SIGNAL_FRAME_LABELS_ANCHOR: str = "w"
        ACTION_BUTTON_TEXT_ANCHOR: str = "center"
        STANDART_PAD: Tuple[int, int] = (7, 7)
        ZERO_PAD: Tuple[int, int] = (0, 0)
        LABELS_IN_FRAME_PADX: Tuple[int, int] = (14, 0)
        LABELS_SOLO_PADX: Tuple[int, int] = (20, 7)
        RIGHT_PADX: Tuple[int, int] = (0, 3)
        LEFT_PADX: Tuple[int, int] = (3, 0)

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

    class Colors:
        """
        Colors
        """

        TRANSPARENT = "transparent"
        BUTTON_HOVER = "#3E3E3E"

    class Values:
        """
        Values of different widgets.
        """

        SEARCH_SELECTION_SEGMENTED_BUTTON = ["Signals", "Groups"]
        FILTER_SIGNALS_SEGMENTED_BUTTON = ["All", "Non const. zero", "Non const."]
        FILE_OPTIONMENU = [" "]
        FILE_ACTION_OPTIONMENU = ["OPEN FILE...", "EXPORT to EXCEL"]
