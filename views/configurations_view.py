"""Centralized configuration file."""

from typing import Literal


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

        NAV_TOOLBAR_CORNER_RADIUS: int = 10
        INPUT_ENTRY_BORDER_WIDTH: int = 0
        OUTPUT_ENTRY_BORDER_WIDTH: int = 1

    class Dimensions:
        """
        Dimensions
        """

        ACTION_BUTTON_WIDTH_HEIGHT: int = 10
        ACTION_IMAGE_WIDTH_HEIGHT: int = 17
        TOGGLE_HEADER_FRAME_BUTTON_WIDTH_HEIGHT: int = 20

    class KeyBindings:
        """
        Key bindings
        """

        ESCAPE_KEY: str = "<Escape>"
        CTRL_B_KEY: str = "<Control-b>"

    class ImageFormats:
        """
        Image formats
        """

        APP_ICON: str = "resources/Images/CSVision.ico"
        BACK_PNG: str = "resources/Images/back.png"
        CLEAR_SEARCH_RESULT_PNG: str = "resources/Images/clear-search-results.png"
        DOWN_ARROW_PNG: str = "resources/Images/down-arrow.png"
        EXCEL_PNG: str = "resources/Images/excel.png"
        FORWARD_PNG: str = "resources/Images/forward.png"
        HIDE_SIDEPANEL_PNG: str = "resources/Images/hide-sidepanel.png"
        LEGEND_PNG: str = "resources/Images/legend.png"
        OPEN_FILE_PNG: str = "resources/Images/open-file.png"
        PAN_PNG: str = "resources/Images/pan.png"
        REFRESH_PNG: str = "resources/Images/refresh.png"
        RESET_PNG: str = "resources/Images/reset.png"
        SAVE_PNG: str = "resources/Images/save.png"
        SETTINGS_PNG: str = "resources/Images/settings.png"
        SHOW_SIDEPANEL_PNG: str = "resources/Images/show-sidepanel.png"
        ZOOM_PNG: str = "resources/Images/zoom.png"

    class Fonts:
        """
        Fonts
        """

        FONT: str = "Kento"
        NORMAL_SIZE: int = 12

        FONT_SIZE: tuple[str, int] = ("Kento", 12)
        FONT_SIZE_WEIGHT: tuple[str, int] = ("Kento", 12, "bold")
        BUTTON_TEXTS: tuple[str, int, str] = ("Kento", 12, "bold")

    class Colors:
        """
        Colors
        """

        TRANSPARENT: str = "transparent"
        ONYX: str = "#343638"
        TRANSPARENT_BUTTON_HOVER: str = "#3E3E3E"
        BORDER_COLOR: str = "#6C6C6C"
        COLORED_BUTTON_HOVER: str = "#3D3E40"
        PLOT_FRAME_COLOR: str = "#333333"

    class Layout:
        """
        Layout
        """

        STANDART_PAD: tuple[int, int] = (7, 7)

        NAVIGATION_FRAME_SIDE: str = "left"
        NAVIGATION_FRAME_FILL: str = "y"
        NAVIGATION_FRAME_EXPAND: bool = False

        HEADER_PANEL_SIDE: str = "right"
        HEADER_PANEL_FILL: str = "y"
        HEADER_PANEL_EXPAND: bool = True

        TOGGLE_HEADER_FRAME_BUTTON_SIDE: str = "top"
        TOGGLE_HEADER_FRAME_BUTTON_FILL: str = "x"
        TOGGLE_HEADER_FRAME_BUTTON_EXPAND: bool = False
        TOGGLE_HEADER_FRAME_BUTTON_PAD: tuple[int, int] = (3, 3)

        SETTINGS_BUTTON_SIDE: str = "bottom"
        SETTINGS_BUTTON_FILL: str = "x"
        SETTINGS_BUTTON_EXPAND: bool = False
        SETTINGS_BUTTON_PAD: tuple[int, int] = (3, 3)

        SETTINGS_BUTTON_SIDE: str = "bottom"
        SETTINGS_BUTTON_FILL: str = "x"
        SETTINGS_BUTTON_EXPAND: bool = False
        SETTINGS_BUTTON_PAD: tuple[int, int] = (3, 3)

        FILEHANDLING_FRAME_ROW: int = 0
        SEARCHBAR_FRAME_ROW: int = FILEHANDLING_FRAME_ROW + 1
        HEADER_LIST_FRAME_ROW: int = SEARCHBAR_FRAME_ROW + 1
        CONFIG_HEADER_LIST_FRAME_ROW: int = HEADER_LIST_FRAME_ROW + 1
        PRESET_FRAME_ROW: int = CONFIG_HEADER_LIST_FRAME_ROW + 1
        GENERAL_FRAME_STICKY: str = "nesw"

        SEARCHBAR_TITLE_FARME_ROW: int = 0
        SEARCHBAR_ENTRY_ROW: int = 1
        SEARCHBAR_FILTER_FARME_ROW: int = 2
        FILEHANDLING_TITLE_FARME_ROW: int = 0
        FILEHANDLING_ENTRY_ROW: int = 1
        FILEHANDLING_FILTER_FARME_ROW: int = 2
        GENERAL_INNER_FRAME_STICKY: str = "ew"

        HEADER_FRAME_LABELS_ANCHOR: str = "w"
        ACTION_BUTTON_TEXT_ANCHOR: str = "center"
        ZERO_PAD: tuple[int, int] = (0, 0)
        LABELS_IN_FRAME_PADX: tuple[int, int] = (14, 0)

        HEADER_FRAME_SCROLLABLEFRAME_SIDE: str = "top"
        HEADER_FRAME_SCROLLABLEFRAME_FILL: str = "both"
        HEADER_FRAME_SCROLLABLEFRAME_EXPAND: bool = True
        HEADER_FRAME_SCROLLABLEFRAME_PAD: tuple[int, int] = (1, 1)

        PLOT_FRAME_PLOT_AREA_FRAME_SIDE: str = "top"
        PLOT_FRAME_PLOT_AREA_FRAME_FILL: str = "both"
        PLOT_FRAME_PLOT_AREA_FRAME_EXPAND: bool = True
        PLOT_FRAME_PLOT_AREA_FRAME_PADY: tuple[int, int] = (20, 30)

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
        NAV_TOOLBAR_LEFT_BUTTONS_PADX: tuple[int, int] = (30, 7)
        NAV_TOOLBAR_RIGHT_BUTTONS_PADX: tuple[int, int] = (7, 30)

        CANVAS_SIDE: Literal["left", "right", "top", "bottom"] = "top"
        CANVAS_FILL: Literal["none", "x", "y", "both"] = "both"
        CANVAS_EXPAND: bool = True
        CANVAS_PADY: tuple[int, int] = (2, 2)

    class LabelTexts:
        """
        Label texts
        """

        FILEHANDLING_TEXT: str = "FILE EXPLORER"
        SEARCHBAR_TEXT: str = "SEARCH"
        HEADER_LIST_TEXT: str = f"{'HEADERS':>9}"
        CONFIG_HEADER_LIST_TEXT: str = f"{'CONFIGURATIONS':>16}"

    class Values:
        """
        Values of different widgets.
        """

        SEARCH_SELECTION_SEGMENTED_BUTTON: list[str] = ["Sub-H", "Heading"]
        FILTER_SUBHEADINGS_SEGMENTED_BUTTON: list[str] = [
            "All",
            "Non const. zero",
            "Non const.",
        ]
        PLOT_TYPES: list[str] = [
            "Plot",
            "Scatter",
            "Bar",
            "Stem",
        ]
        COLLECTION_FILEPATH_YAML: str = "resources/yaml-files/file_paths.yaml"
        FILE_TYPE_TO_READ: list[tuple[str, str]] = [("CSV", "*.csv*")]


class AppWindowConfig:
    """
    Contains classes that define the configurations of the app window.
    """

    class General:
        """
        General configurations.
        """

        TITLE: str = "CSVision"
        ICON: str = Config.ImageFormats.APP_ICON

    class Dimensions:
        """
        Dimensions.
        """

        WIDTH: int = 1150
        HEIGHT: int = 666

        MIN_WIDTH: int = WIDTH - 200
        MIN_HEIGHT: int = HEIGHT - 200

    class Layout:
        """
        Layout.
        """

        MAINVIEW_SIDE: str = "top"
        MAINVIEW_FILL: str = "both"
        MAINVIEW_EXPAND: bool = True

    class KeyBindings:
        """
        Key bindings.
        """

        CLOSE_APPLICATION: str = Config.KeyBindings.ESCAPE_KEY


class MainConfig:
    """
    Contains classes that define the configurations of the settings window.
    """

    class General:
        """
        General configurations.
        """

        CORNER_RADIUS: int = Config.General.CORNER_RADIUS

    class Layout:
        """
        Layout.
        """

        STATUSBARVIEW_SIDE: str = "bottom"
        STATUSBARVIEW_FILL: str = "x"
        STATUSBARVIEW_EXPAND: bool = False

        SIDEBARVIEW_SIDE: str = "left"
        SIDEBARVIEW_FILL: str = "y"
        SIDEBARVIEW_EXPAND: bool = False

        PLOTVIEW_SIDE: str = "right"
        PLOTVIEW_FILL: str = "both"
        PLOTVIEW_EXPAND: bool = True

    class KeyBindings:
        """
        Key bindings.
        """

        RESIZE_HEADER_FRAME: str = Config.KeyBindings.CTRL_B_KEY


class StatusbarConfig:
    """
    Contains classes that define the configurations of the statusbar.
    """

    class General:
        """
        General configurations.
        """

        CORNER_RADIUS: int = Config.General.CORNER_RADIUS
        FRAME_BORDER_WIDTH: int = Config.General.FRAME_BORDER_WIDTH

    class KeyBindings:
        """
        Key bindings.
        """

        CLOSE_APPLICATION: str = Config.KeyBindings.ESCAPE_KEY

    class Dimensions:
        """
        Dimensions.
        """

        HEIGHT: int = 20

    class Layout:
        """
        Layout.
        """

        STANDART_PAD: tuple[int, int] = Config.Layout.STANDART_PAD

        FILSIZE_LABEL_SIDE: str = "left"
        FILSIZE_LABEL_PADX: tuple[int, int] = (50, 10)
        FILSIZE_LABEL_PADY: tuple[int, int] = (1, 1)

        PROGRESSBAR_SIDE: str = "left"
        PROGRESSBAR_PADX: tuple[int, int] = (10, 10)

    class Fonts:
        """
        Fonts.
        """

        FILSIZE_LABEL_FONT: str = Config.Fonts.FONT
        FILSIZE_LABEL_FONT_SIZE: int = Config.Fonts.NORMAL_SIZE


class SettingsWindowConfig:
    """
    Contains classes that define the configurations of the settings window.
    """

    class General:
        """
        General configurations.
        """

        TITLE: str = "Settings"
        ICON: str = Config.ImageFormats.APP_ICON

    class Dimensions:
        """
        Dimensions.
        """

        WIDTH: int = 500
        HEIGHT: int = 200

        RESIZABLE_WIDTH: bool = False
        RESIZABLE_HEIGHT: bool = False

    class KeyBindings:
        """
        Key bindings.
        """

        CLOSE_SETTINGS: str = Config.KeyBindings.ESCAPE_KEY
