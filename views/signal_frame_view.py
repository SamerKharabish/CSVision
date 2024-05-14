""" Defines the SignalFrameView class with the signal frame layout. """

from PIL import Image
import customtkinter as ctk
from views.configurations_view import Config
from utils.input_entry_list import InputEntryList


class SignalFrameView(ctk.CTkFrame):
    """
    Layout of the signal frame.
    """

    __slots__ = (
        "root",
        "__side_bar_frame",
        "signal_panel",
        "filehandling_frame_view",
        "__searchbar_frame_view",
        "signallist_frame_view",
        "__config_signallist_frame_view",
        "__preset_frame_view",
        "toggle_side_bar_button",
        "__settings_button",
    )

    def __init__(self, master: ctk.CTkFrame) -> None:
        super().__init__(
            master,
            corner_radius=Config.General.CORNER_RADIUS,
            fg_color=Config.Colors.TRANSPARENT,
        )
        self.root: ctk.CTk

        self.__initialize_widgets()
        self.__create_layout()

    def __initialize_widgets(self) -> None:
        """
        Initialize widgets.
        """
        self.__side_bar_frame: ctk.CTkFrame = ctk.CTkFrame(
            self,
            corner_radius=Config.General.CORNER_RADIUS,
            border_width=Config.General.FRAME_BORDER_WIDTH,
            fg_color=Config.Colors.TRANSPARENT,
        )

        self.signal_panel: ctk.CTkFrame = ctk.CTkFrame(
            self,
            corner_radius=Config.General.CORNER_RADIUS,
            fg_color=Config.Colors.TRANSPARENT,
        )
        self.filehandling_frame_view: ctk.CTkFrame = FileHandlingFrameView(
            self.signal_panel
        )
        self.__searchbar_frame_view: ctk.CTkFrame = SearchBarFrameView(
            self.signal_panel
        )
        self.signallist_frame_view: ctk.CTkFrame = SignalListFrameView(
            self.signal_panel
        )
        self.__config_signallist_frame_view: ctk.CTkFrame = ConfigSignalListFrameView(
            self.signal_panel
        )
        self.__preset_frame_view: ctk.CTkFrame = PresetFrameView(self.signal_panel)

        self.toggle_side_bar_button = ctk.CTkButton(
            self.__side_bar_frame,
            width=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            height=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            fg_color=Config.Colors.TRANSPARENT,
            hover_color=Config.Colors.TRANSPARENT_BUTTON_HOVER,
            text="",
            image=ctk.CTkImage(
                light_image=Image.open(
                    Config.ImageFormats.HIDE_HEADER_FRAME_BUTTON_PNG
                ),
                size=(
                    Config.Dimensions.TOGGLE_HEADER_FRAME_BUTTON_WIDTH_HEIGHT,
                    Config.Dimensions.TOGGLE_HEADER_FRAME_BUTTON_WIDTH_HEIGHT,
                ),
            ),
            anchor=Config.Layout.ACTION_BUTTON_TEXT_ANCHOR,
        )

        self.__settings_button = ctk.CTkButton(
            self.__side_bar_frame,
            width=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            height=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            fg_color=Config.Colors.TRANSPARENT,
            hover_color=Config.Colors.TRANSPARENT_BUTTON_HOVER,
            text="",
            image=ctk.CTkImage(
                light_image=Image.open(Config.ImageFormats.SETTINGS_BUTTON_PNG),
                size=(
                    Config.Dimensions.TOGGLE_HEADER_FRAME_BUTTON_WIDTH_HEIGHT,
                    Config.Dimensions.TOGGLE_HEADER_FRAME_BUTTON_WIDTH_HEIGHT,
                ),
            ),
            anchor=Config.Layout.ACTION_BUTTON_TEXT_ANCHOR,
        )

    def __create_layout(self) -> None:
        """
        Create layout.
        """
        self.__side_bar_frame.pack(
            side=Config.Layout.NAVIGATION_FRAME_SIDE,
            fill=Config.Layout.NAVIGATION_FRAME_FILL,
            expand=Config.Layout.NAVIGATION_FRAME_EXPAND,
        )
        self.toggle_side_bar_button.pack(
            side=Config.Layout.TOGGLE_HEADER_FRAME_BUTTON_SIDE,
            fill=Config.Layout.TOGGLE_HEADER_FRAME_BUTTON_FILL,
            expand=Config.Layout.TOGGLE_HEADER_FRAME_BUTTON_EXPAND,
            padx=Config.Layout.TOGGLE_HEADER_FRAME_BUTTON_PAD,
            pady=Config.Layout.STANDART_PAD,
        )

        self.__settings_button.pack(
            side=Config.Layout.SETTINGS_BUTTON_SIDE,
            fill=Config.Layout.SETTINGS_BUTTON_FILL,
            expand=Config.Layout.SETTINGS_BUTTON_EXPAND,
            padx=Config.Layout.SETTINGS_BUTTON_PAD,
            pady=Config.Layout.STANDART_PAD,
        )

        self.signal_panel.pack(
            side=Config.Layout.HEADER_PANEL_SIDE,
            fill=Config.Layout.HEADER_PANEL_FILL,
            expand=Config.Layout.HEADER_PANEL_EXPAND,
        )
        self.signal_panel.grid_rowconfigure(
            (
                Config.Layout.HEADER_LIST_FRAME_ROW,
                Config.Layout.CONFIG_HEADER_LIST_FRAME_ROW,
            ),
            weight=1,
        )
        self.filehandling_frame_view.grid(
            row=Config.Layout.FILEHANDLING_FRAME_ROW,
            column=0,
            sticky=Config.Layout.GENERAL_FRAME_STICKY,
        )
        self.__searchbar_frame_view.grid(
            row=Config.Layout.SEARCHBAR_FRAME_ROW,
            column=0,
            sticky=Config.Layout.GENERAL_FRAME_STICKY,
        )
        self.signallist_frame_view.grid(
            row=Config.Layout.HEADER_LIST_FRAME_ROW,
            column=0,
            sticky=Config.Layout.GENERAL_FRAME_STICKY,
        )
        self.__config_signallist_frame_view.grid(
            row=Config.Layout.CONFIG_HEADER_LIST_FRAME_ROW,
            column=0,
            sticky=Config.Layout.GENERAL_FRAME_STICKY,
        )
        self.__preset_frame_view.grid(
            row=Config.Layout.PRESET_FRAME_ROW,
            column=0,
            sticky=Config.Layout.GENERAL_FRAME_STICKY,
        )


class FileHandlingFrameView(ctk.CTkFrame):
    """
    Layout of the file handling frame.
    """

    def __init__(self, master: ctk.CTkFrame) -> None:
        super().__init__(
            master,
            corner_radius=Config.General.CORNER_RADIUS,
            border_width=Config.General.FRAME_BORDER_WIDTH,
        )
        self.root: ctk.CTk

        self.initialize_widgets()
        self.create_layout()

    def initialize_widgets(self) -> None:
        """
        Initialize widgets.
        """
        self.title_frame = ctk.CTkFrame(
            self,
            corner_radius=Config.General.CORNER_RADIUS,
            fg_color=Config.Colors.TRANSPARENT,
        )

        self.title_label = ctk.CTkLabel(
            self.title_frame,
            text=Config.LabelTexts.FILEHANDLING_TEXT,
            font=ctk.CTkFont(
                family=Config.Fonts.LABEL_TEXTS[0], size=Config.Fonts.LABEL_TEXTS[1]
            ),
            anchor=Config.Layout.HEADER_FRAME_LABELS_ANCHOR,
        )

        self.open_file_button = ctk.CTkButton(
            self.title_frame,
            width=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            height=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            fg_color=Config.Colors.TRANSPARENT,
            hover_color=Config.Colors.TRANSPARENT_BUTTON_HOVER,
            text="",
            image=ctk.CTkImage(
                light_image=Image.open(Config.ImageFormats.OPEN_FILE_PNG),
                size=(
                    Config.Dimensions.ACTION_IMAGE_WIDTH_HEIGHT,
                    Config.Dimensions.ACTION_IMAGE_WIDTH_HEIGHT,
                ),
            ),
            anchor=Config.Layout.ACTION_BUTTON_TEXT_ANCHOR,
        )

        self.export_to_excel = ctk.CTkButton(
            self.title_frame,
            width=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            height=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            fg_color=Config.Colors.TRANSPARENT,
            hover_color=Config.Colors.TRANSPARENT_BUTTON_HOVER,
            text="",
            image=ctk.CTkImage(
                light_image=Image.open(Config.ImageFormats.EXCEL_PNG),
                size=(
                    Config.Dimensions.ACTION_IMAGE_WIDTH_HEIGHT,
                    Config.Dimensions.ACTION_IMAGE_WIDTH_HEIGHT,
                ),
            ),
            anchor=Config.Layout.ACTION_BUTTON_TEXT_ANCHOR,
        )

        self.selected_file_path = ctk.StringVar()
        self.file_entry = InputEntryList(
            self,
            width=320,
            border_width=Config.General.OUTPUT_ENTRY_BORDER_WIDTH,
            fg_color=Config.Colors.ONYX,
            border_color=Config.Colors.BORDER_COLOR,
            selected_file_path=self.selected_file_path,
            font=ctk.CTkFont(
                family=Config.Fonts.LABEL_TEXTS[0], size=Config.Fonts.LABEL_TEXTS[1]
            ),
            state="readonly",
            collection_filepath_yaml=Config.Values.COLLECTION_FILEPATH_YAML,
        )

    def create_layout(self) -> None:
        """
        Create layout.
        """
        self.rowconfigure(
            (
                Config.Layout.FILEHANDLING_TITLE_FARME_ROW,
                Config.Layout.FILEHANDLING_ENTRY_ROW,
                Config.Layout.FILEHANDLING_FILTER_FARME_ROW,
            ),
            weight=1,
        )

        self.title_frame.grid(
            row=Config.Layout.FILEHANDLING_TITLE_FARME_ROW,
            column=0,
            sticky=Config.Layout.GENERAL_INNER_FRAME_STICKY,
            padx=Config.Layout.STANDART_PAD,
            pady=(3, 0),
        )
        self.title_frame.columnconfigure(0, weight=50)
        self.title_frame.columnconfigure((1, 2), weight=1)
        self.title_label.grid(
            row=0,
            column=0,
            sticky="w",
            padx=Config.Layout.LABELS_IN_FRAME_PADX,
            pady=Config.Layout.ZERO_PAD,
        )
        self.open_file_button.grid(
            row=0,
            column=1,
            sticky="e",
            padx=Config.Layout.ZERO_PAD,
            pady=Config.Layout.ZERO_PAD,
        )
        self.export_to_excel.grid(
            row=0,
            column=2,
            sticky="e",
            padx=Config.Layout.ZERO_PAD,
            pady=Config.Layout.ZERO_PAD,
        )

        self.file_entry.grid(
            row=Config.Layout.FILEHANDLING_ENTRY_ROW,
            column=0,
            sticky=Config.Layout.GENERAL_INNER_FRAME_STICKY,
            padx=Config.Layout.STANDART_PAD,
            pady=(0, 7),
        )


class SearchBarFrameView(ctk.CTkFrame):
    """
    Layout of the search bar.
    """

    def __init__(self, master: ctk.CTkFrame) -> None:
        super().__init__(
            master,
            corner_radius=Config.General.CORNER_RADIUS,
            border_width=Config.General.FRAME_BORDER_WIDTH,
        )

        self.initialize_widgets()
        self.create_layout()

    def initialize_widgets(self) -> None:
        """
        Initialize widgets.
        """
        self.title_frame = ctk.CTkFrame(
            self,
            corner_radius=Config.General.CORNER_RADIUS,
            fg_color=Config.Colors.TRANSPARENT,
        )

        self.title_label = ctk.CTkLabel(
            self.title_frame,
            text=Config.LabelTexts.SEARCHBAR_TEXT,
            font=ctk.CTkFont(
                family=Config.Fonts.LABEL_TEXTS[0], size=Config.Fonts.LABEL_TEXTS[1]
            ),
            anchor=Config.Layout.HEADER_FRAME_LABELS_ANCHOR,
        )

        self.clear_search_result_button = ctk.CTkButton(
            self.title_frame,
            width=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            height=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            fg_color=Config.Colors.TRANSPARENT,
            hover_color=Config.Colors.TRANSPARENT_BUTTON_HOVER,
            text="",
            image=ctk.CTkImage(
                light_image=Image.open(Config.ImageFormats.CLEAR_SEARCH_RESULT_PNG),
                size=(
                    Config.Dimensions.ACTION_IMAGE_WIDTH_HEIGHT,
                    Config.Dimensions.ACTION_IMAGE_WIDTH_HEIGHT,
                ),
            ),
            anchor=Config.Layout.ACTION_BUTTON_TEXT_ANCHOR,
        )

        self.entry_frame = ctk.CTkFrame(
            self,
            corner_radius=Config.General.CORNER_RADIUS,
            fg_color=Config.Colors.TRANSPARENT,
        )

        self.search_entry = ctk.CTkEntry(
            self.entry_frame,
            width=204,
            border_width=Config.General.INPUT_ENTRY_BORDER_WIDTH,
            font=ctk.CTkFont(
                family=Config.Fonts.LABEL_TEXTS[0], size=Config.Fonts.LABEL_TEXTS[1]
            ),
        )

        self.search_selection_segmented_button_var = ctk.StringVar(
            value=Config.Values.SEARCH_SELECTION_SEGMENTED_BUTTON[0]
        )
        self.search_selection_segmented_button = ctk.CTkSegmentedButton(
            self.entry_frame,
            font=ctk.CTkFont(
                family=Config.Fonts.LABEL_TEXTS[0], size=Config.Fonts.LABEL_TEXTS[1]
            ),
            values=Config.Values.SEARCH_SELECTION_SEGMENTED_BUTTON,
            variable=self.search_selection_segmented_button_var,
        )

        self.filter_signals_segmented_button_var = ctk.StringVar(
            value=Config.Values.FILTER_SUBHEADINGS_SEGMENTED_BUTTON[0]
        )
        self.filter_signals_segmented_button = ctk.CTkSegmentedButton(
            self,
            font=ctk.CTkFont(
                family=Config.Fonts.LABEL_TEXTS[0], size=Config.Fonts.LABEL_TEXTS[1]
            ),
            values=Config.Values.FILTER_SUBHEADINGS_SEGMENTED_BUTTON,
            variable=self.filter_signals_segmented_button_var,
        )

    def create_layout(self) -> None:
        """
        Create layout.
        """
        self.rowconfigure(
            (
                Config.Layout.SEARCHBAR_TITLE_FARME_ROW,
                Config.Layout.SEARCHBAR_ENTRY_ROW,
                Config.Layout.SEARCHBAR_FILTER_FARME_ROW,
            ),
            weight=1,
        )

        self.title_frame.grid(
            row=Config.Layout.SEARCHBAR_TITLE_FARME_ROW,
            column=0,
            sticky=Config.Layout.GENERAL_INNER_FRAME_STICKY,
            padx=Config.Layout.STANDART_PAD,
            pady=(3, 0),
        )
        self.title_frame.columnconfigure((0, 1), weight=1)
        self.title_label.grid(
            row=0,
            column=0,
            sticky="w",
            padx=Config.Layout.LABELS_IN_FRAME_PADX,
            pady=Config.Layout.ZERO_PAD,
        )
        self.clear_search_result_button.grid(
            row=0,
            column=1,
            sticky="e",
            padx=Config.Layout.ZERO_PAD,
            pady=Config.Layout.ZERO_PAD,
        )

        self.entry_frame.grid(
            row=Config.Layout.SEARCHBAR_ENTRY_ROW,
            column=0,
            sticky=Config.Layout.GENERAL_INNER_FRAME_STICKY,
            padx=Config.Layout.STANDART_PAD,
            pady=Config.Layout.ZERO_PAD,
        )
        self.entry_frame.columnconfigure(0, weight=2)
        self.entry_frame.columnconfigure(1, weight=1)
        self.search_entry.grid(
            row=0,
            column=0,
            sticky="w",
            padx=(0, 3),
            pady=Config.Layout.ZERO_PAD,
        )

        self.search_selection_segmented_button.grid(
            row=0,
            column=1,
            sticky="e",
            padx=(3, 0),
            pady=Config.Layout.ZERO_PAD,
        )

        self.filter_signals_segmented_button.grid(
            row=Config.Layout.SEARCHBAR_FILTER_FARME_ROW,
            column=0,
            sticky=Config.Layout.GENERAL_INNER_FRAME_STICKY,
            padx=Config.Layout.STANDART_PAD,
            pady=Config.Layout.STANDART_PAD,
        )


class SignalListFrameView(ctk.CTkFrame):
    """
    Layout of the signal list.
    """

    def __init__(self, master: ctk.CTkFrame) -> None:
        super().__init__(
            master,
            corner_radius=Config.General.CORNER_RADIUS,
            border_width=Config.General.FRAME_BORDER_WIDTH,
        )

        self.initialize_widgets()
        self.create_layout()

    def initialize_widgets(self) -> None:
        """
        Initialize widgets.
        """
        self.signal_scrollableframe = ctk.CTkScrollableFrame(
            self,
            fg_color=Config.Colors.TRANSPARENT,
            label_text=Config.LabelTexts.HEADER_LIST_TEXT,
            label_font=ctk.CTkFont(
                family=Config.Fonts.LABEL_TEXTS[0], size=Config.Fonts.LABEL_TEXTS[1]
            ),
            label_anchor=Config.Layout.HEADER_FRAME_LABELS_ANCHOR,
        )

    def create_layout(self) -> None:
        """
        Create layout.
        """
        self.pack_propagate(False)
        self.signal_scrollableframe.pack(
            side=Config.Layout.HEADER_FRAME_SCROLLABLEFRAME_SIDE,
            fill=Config.Layout.HEADER_FRAME_SCROLLABLEFRAME_FILL,
            expand=Config.Layout.HEADER_FRAME_SCROLLABLEFRAME_EXPAND,
            padx=Config.Layout.HEADER_FRAME_SCROLLABLEFRAME_PAD,
            pady=Config.Layout.HEADER_FRAME_SCROLLABLEFRAME_PAD,
        )


class ConfigSignalListFrameView(ctk.CTkFrame):
    """
    Layout of the signal configuration list.
    """

    def __init__(self, master: ctk.CTkFrame) -> None:
        super().__init__(
            master,
            corner_radius=Config.General.CORNER_RADIUS,
            border_width=Config.General.FRAME_BORDER_WIDTH,
        )

        self.initialize_widgets()
        self.create_layout()

    def initialize_widgets(self) -> None:
        """
        Initialize widgets.
        """
        self.signal_scrollableframe = ctk.CTkScrollableFrame(
            self,
            fg_color=Config.Colors.TRANSPARENT,
            label_text=Config.LabelTexts.CONFIG_HEADER_LIST_TEXT,
            label_font=ctk.CTkFont(
                family=Config.Fonts.LABEL_TEXTS[0], size=Config.Fonts.LABEL_TEXTS[1]
            ),
            label_anchor=Config.Layout.HEADER_FRAME_LABELS_ANCHOR,
        )

    def create_layout(self) -> None:
        """
        Create layout.
        """
        self.pack_propagate(False)
        self.signal_scrollableframe.pack(
            side=Config.Layout.HEADER_FRAME_SCROLLABLEFRAME_SIDE,
            fill=Config.Layout.HEADER_FRAME_SCROLLABLEFRAME_FILL,
            expand=Config.Layout.HEADER_FRAME_SCROLLABLEFRAME_EXPAND,
            padx=Config.Layout.HEADER_FRAME_SCROLLABLEFRAME_PAD,
            pady=Config.Layout.HEADER_FRAME_SCROLLABLEFRAME_PAD,
        )


class PresetFrameView(ctk.CTkFrame):
    """
    Layout of the signal configuration list.
    """

    def __init__(self, master: ctk.CTkFrame) -> None:
        super().__init__(
            master,
            height=40,
            corner_radius=Config.General.CORNER_RADIUS,
            border_width=Config.General.FRAME_BORDER_WIDTH,
        )

        self.initialize_widgets()
        self.create_layout()

    def initialize_widgets(self) -> None:
        """
        Initialize widgets.
        """
        self.preset_entry = ctk.CTkEntry(
            self,
            border_width=Config.General.OUTPUT_ENTRY_BORDER_WIDTH,
            border_color=Config.Colors.BORDER_COLOR,
            fg_color=Config.Colors.ONYX,
            font=ctk.CTkFont(
                family=Config.Fonts.LABEL_TEXTS[0], size=Config.Fonts.LABEL_TEXTS[1]
            ),
        )

        self.save_preset_button = ctk.CTkButton(
            self,
            width=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            height=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            fg_color=Config.Colors.TRANSPARENT,
            hover_color=Config.Colors.TRANSPARENT_BUTTON_HOVER,
            text="",
            image=ctk.CTkImage(
                light_image=Image.open(Config.ImageFormats.OPEN_FILE_PNG),
                size=(
                    Config.Dimensions.ACTION_IMAGE_WIDTH_HEIGHT,
                    Config.Dimensions.ACTION_IMAGE_WIDTH_HEIGHT,
                ),
            ),
            anchor=Config.Layout.ACTION_BUTTON_TEXT_ANCHOR,
        )

        self.load_preset_button = ctk.CTkButton(
            self,
            width=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            height=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            fg_color=Config.Colors.TRANSPARENT,
            hover_color=Config.Colors.TRANSPARENT_BUTTON_HOVER,
            text="",
            image=ctk.CTkImage(
                light_image=Image.open(Config.ImageFormats.REFRESH_PNG),
                size=(
                    Config.Dimensions.ACTION_IMAGE_WIDTH_HEIGHT,
                    Config.Dimensions.ACTION_IMAGE_WIDTH_HEIGHT,
                ),
            ),
            anchor=Config.Layout.ACTION_BUTTON_TEXT_ANCHOR,
        )

    def create_layout(self) -> None:
        """
        Create layout.
        """
        self.pack_propagate(False)
        self.preset_entry.pack(
            side="left",
            fill="x",
            expand=True,
            padx=Config.Layout.STANDART_PAD,
            pady=Config.Layout.STANDART_PAD,
        )
        self.load_preset_button.pack(
            side="left",
            fill="y",
            expand=False,
            padx=Config.Layout.ZERO_PAD,
            pady=Config.Layout.STANDART_PAD,
        )
        self.save_preset_button.pack(
            side="left",
            fill="y",
            expand=False,
            padx=(0, 7),
            pady=Config.Layout.STANDART_PAD,
        )
