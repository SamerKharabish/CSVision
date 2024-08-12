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
        ERROR: str = "resources/Images/error.png"
        EXCEL_PNG: str = "resources/Images/excel.png"
        FORWARD_PNG: str = "resources/Images/forward.png"
        HIDE_SIDEPANEL_PNG: str = "resources/Images/hide-sidepanel.png"
        INFO_PNG: str = "resources/Images/info.png"
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
        WEIGHT_BOLD: str = "bold"

        FONT_SIZE: tuple[str, int] = ("Kento", 12)
        FONT_SIZE_WEIGHT: tuple[str, int] = ("Kento", 12, "bold")
        BUTTON_TEXTS: tuple[str, int, str] = ("Kento", 12, "bold")

    class Colors:
        """
        Colors
        """

        TRANSPARENT: str = "transparent"
        DIM_GRAY: str = "#6C6C6C"
        ONYX: str = "#343638"
        ONYX_LIGHT: str = "#3D3E40"
        ALICE_BLUE: str = "#DCE4EE"
        ERROR: str = "#C91C1C"
        WARNING: str = "#C6A11D"

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
        USER_SETTINGS_YAML: str = "resources/yaml-files/user_settings.yaml"
        FILE_TYPE_TO_READ: list[tuple[str, str]] = [("CSV", "*.csv*")]


class MainConfig:
    """
    Contains classes that define the configurations of the settings window.
    """

    class General:
        """
        General configurations.
        """

        CORNER_RADIUS: int = Config.General.CORNER_RADIUS

    class KeyBindings:
        """
        Key bindings.
        """

        RESIZE_HEADER_FRAME: str = Config.KeyBindings.CTRL_B_KEY

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

        CORNER_RADIUS: int = 5

    class KeyBindings:
        """
        Key bindings.
        """

        CLOSE_SETTINGS: str = Config.KeyBindings.ESCAPE_KEY

    class Dimensions:
        """
        Dimensions.
        """

        WIDTH: int = 700
        HEIGHT: int = 330

        RESIZABLE_WIDTH: bool = False
        RESIZABLE_HEIGHT: bool = False

        MANAGE_BUTTON_WIDTH: int = 80

    class Layout:
        """
        Layout.
        """

        STANDART_PAD: tuple[int, int] = Config.Layout.STANDART_PAD

        CATEGORY_SEGMENTED_BUTTON_X: int = 20
        CATEGORY_SEGMENTED_BUTTON_Y: int = 7
        CATEGORY_SEGMENTED_BUTTON_ANCHOR: str = "nw"

        CATEGORY_FRAME_SIDE: str = "top"
        CATEGORY_FRAME_FILL: str = "both"
        CATEGORY_FRAME_EXPAND: bool = True
        CATEGORY_FRAME_PADY: tuple[int, int] = (20, 3)

        HEADER_STRUCTURE_FRAME_SIDE: str = "top"
        HEADER_STRUCTURE_FRAME_FILL: str = "x"
        HEADER_STRUCTURE_FRAME_EXPAND: bool = False
        HEADER_STRUCTURE_FRAME_PADY: tuple[int, int] = (15, 3)

        MANAGE_SETTINGS_FRAME_SIDE: str = "top"
        MANAGE_SETTINGS_FRAME_FILL: str = "x"
        MANAGE_SETTINGS_FRAME_EXPAND: bool = False
        MANAGE_SETTINGS_FRAME_PADY: tuple[int, int] = (3, 7)

        MANAGE_BUTTON_SIDE: str = "right"
        MANAGE_BUTTON_FILL: str = None
        MANAGE_BUTTON_EXPAND: bool = False
        MANAGE_BUTTON_PADY: tuple[int, int] = (5, 5)

    class Fonts:
        """
        Fonts.
        """

        FONT: str = Config.Fonts.FONT
        FONT_SIZE: int = Config.Fonts.NORMAL_SIZE
        FONT_WEIGHT_BOLD: str = Config.Fonts.WEIGHT_BOLD

    class Values:
        """
        Values of different widgets.
        """

        CATEGORIES: list[str] = ["General"]


class HeaderStructureConfig:
    """
    Contains classes that define the configurations of the header structure.
    """

    class General:
        """
        General configurations.
        """

        TITLE: str = "Header structure"
        CORNER_RADIUS: int = SettingsWindowConfig.General.CORNER_RADIUS
        USER_SETTINGS_YAML: str = Config.Values.USER_SETTINGS_YAML

    class Dimensions:
        """
        Dimensions.
        """

        HEADER_STRUCTURE_ENTRIES_WIDTH: int = 50

    class Colors:
        """
        Colors
        """

        ERROR: str = Config.Colors.ERROR
        NORMAL: str = Config.Colors.ONYX
        DISABLED: str = Config.Colors.ONYX_LIGHT
        TEXT: str = Config.Colors.ALICE_BLUE
        WARNING: str = Config.Colors.WARNING

    class Layout:
        """
        Layout.
        """
        TITLE_ROW: int = 0
        LABEL_ROW: int = 1
        INPUT_ROW: int = 2
        INFO_ROW: int = 3
        ERROR_ROW: int = 4

        FIRST_HEADER_PREFIX_COL: int = 0
        FIRST_HEADER_OPTION_COL: int = 1
        FIRST_HEADER_POSTFIX_COL: int = 2
        SECOND_HEADER_PREFIX_COL: int = 3
        SECOND_HEADER_OPTION_COL: int = 4
        SECOND_HEADER_POSTFIX_COL: int = 5
        COL_WEIGHTS: list[int] = [1, 2]

    class Fonts:
        """
        Fonts.
        """

        FONT: str = Config.Fonts.FONT
        FONT_SIZE: int = Config.Fonts.NORMAL_SIZE
        FONT_WEIGHT_BOLD: str = Config.Fonts.WEIGHT_BOLD

    class ImageFormats:
        """
        Image formats
        """

        ERROR: str = Config.ImageFormats.ERROR
        INFO_PNG: str = Config.ImageFormats.INFO_PNG

    class Values:
        """
        Values of different widgets.
        """

        HEADERSTRUCTURE_LABELS: list[str] = [
            "Prefix",
            "Category",
            "Postfix",
            "Prefix",
            "Category",
            "Postfix",
        ]
        HEADERSTRUCTURE_OPTIONS: list[str] = ["Sub-Header", "Header", "N/A"]
