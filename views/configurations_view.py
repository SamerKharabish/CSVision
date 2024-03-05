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
        NAV_TOOLBAR_CORNER_RADIUS: int = 10
        FRAME_BORDER_WIDTH: int = 1
        INPUT_ENTRY_BORDER_WIDTH: int = 0
        OUTPUT_ENTRY_BORDER_WIDTH: int = 1
        SIGNAL_FRAME_MINIMIZED: bool = False

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
        APP_WINDOW_MIN_WIDTH: int = APP_WINDOW_WIDTH - 200
        APP_WINDOW_HEIGHT: int = 666
        APP_WINDOW_MIN_HEIGHT: int = APP_WINDOW_HEIGHT - 200

        STATUSBAR_FRAME_HEIGHT: int = 20

        ACTION_BUTTON_WIDTH_HEIGHT: int = 10
        ACTION_IMAGE_WIDTH_HEIGHT: int = 17
        TOGGLE_SIDEPANEL_BUTTON_WIDTH_HEIGHT: int = 20

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
        HIDE_SIDEPANEL_BUTTON_PNG: str = "resources/Images/hide-sidepanel.png"
        SHOW_SIDEPANEL_BUTTON_PNG: str = "resources/Images/show-sidepanel.png"
        RESET_BUTTON_PNG: str = "resources/Images/reset.png"
        BACK_BUTTON_PNG: str = "resources/Images/back.png"
        PAN_BUTTON_PNG: str = "resources/Images/pan.png"
        SAVE_BUTTON_PNG: str = "resources/Images/save.png"
        FORWARD_BUTTON_PNG: str = "resources/Images/forward.png"
        ZOOM_BUTTON_PNG: str = "resources/Images/zoom.png"
        LEGEND_BUTTON_PNG: str = "resources/Images/legend.png"

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

        SIDE_BAR_FRAME_SIDE: str = "left"
        SIDE_BAR_FRAME_FILL: str = "y"
        SIDE_BAR_FRAME_EXPAND: bool = False

        SIGNAL_PANEL_SIDE: str = "right"
        SIGNAL_PANEL_FILL: str = "y"
        SIGNAL_PANEL_EXPAND: bool = True

        TOGGLE_SIDE_BAR_BUTTON_SIDE: str = "top"
        TOGGLE_SIDE_BAR_BUTTON_FILL: str = "x"
        TOGGLE_SIDE_BAR_BUTTON_EXPAND: bool = False
        TOGGLE_SIDE_BAR_BUTTON_PAD: Tuple[int, int] = (3, 3)

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
        GENERAL_INNER_FRAME_STICKY: str = "ew"

        SIGNAL_FRAME_LABELS_ANCHOR: str = "w"
        ACTION_BUTTON_TEXT_ANCHOR: str = "center"
        STANDART_PAD: Tuple[int, int] = (7, 7)
        ZERO_PAD: Tuple[int, int] = (0, 0)
        LABELS_IN_FRAME_PADX: Tuple[int, int] = (14, 0)

        SIGNAL_FRAME_SCROLLABLEFRAME_SIDE: str = "top"
        SIGNAL_FRAME_SCROLLABLEFRAME_FILL: str = "both"
        SIGNAL_FRAME_SCROLLABLEFRAME_EXPAND: bool = True
        SIGNAL_FRAME_SCROLLABLEFRAME_PAD: Tuple[int, int] = (1, 1)

        PLOT_FRAME_PLOT_AREA_FRAME_SIDE: str = "top"
        PLOT_FRAME_PLOT_AREA_FRAME_FILL: str = "both"
        PLOT_FRAME_PLOT_AREA_FRAME_EXPAND: bool = True
        PLOT_FRAME_PLOT_AREA_FRAME_PADY: Tuple[int, int] = (20, 30)

        PLOT_FRAME_SEGMENTED_BUTTON_X: int = 40
        PLOT_FRAME_SEGMENTED_BUTTON_Y: int = 7
        PLOT_FRAME_SEGMENTED_BUTTON_ANCHOR: str = "nw"

        PLOT_FRAME_NAV_TOOLBAR_FRAME_RELX: float = 0.5
        PLOT_FRAME_NAV_TOOLBAR_FRAME_RELY: float = 1.0
        PLOT_FRAME_NAV_TOOLBAR_FRAME_X: int = 10
        PLOT_FRAME_NAV_TOOLBAR_FRAME_Y: int = -7
        PLOT_FRAME_NAV_TOOLBAR_FRAME_ANCHOR: str = "s"

        NAV_TOOLBAR_BUTTONS_SIDE: str = "left"
        NAV_TOOLBAR_BUTTONS_EXPAND: bool = True
        NAV_TOOLBAR_LEFT_BUTTONS_PADX: Tuple[int, int] = (30, 7)
        NAV_TOOLBAR_RIGHT_BUTTONS_PADX: Tuple[int, int] = (7, 30)

        CANVAS_SIDE: str = "top"
        CANVAS_FILL: str = "both"
        CANVAS_EXPAND: bool = True

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

        FILEHANDLING_TEXT: str = "FILE EXPLORER"
        SEARCHBAR_TEXT: str = "SEARCH"
        SIGNALLIST_TEXT: str = f"{'SIGNALS':>9}"
        CONFIG_SIGNALLIST_TEXT: str = f"{'CONFIGURATIONS':>16}"

    class Fonts:
        """
        Fonts
        """

        LABEL_TEXTS: Tuple[str, int] = ("Kento", 12)
        BUTTON_TEXTS: Tuple[str, int, str] = ("Kento", 12, "bold")

    class Colors:
        """
        Colors
        """

        TRANSPARENT: str = "transparent"
        ONYX: str = "#343638"
        TRANSPARENT_BUTTON_HOVER: str = "#3E3E3E"
        BORDER_COLOR: str = "#6C6C6C"
        COLORED_BUTTON_HOVER: str = "#3D3E40"
        PLOT_FRAME_COLOR: str = "#F8F8FF"

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
        PLOT_TYPES: List[str] = [
            "Plot",
            "Scatter",
            "Bar",
            "Stem",
        ]
