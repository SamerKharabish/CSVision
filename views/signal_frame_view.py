""" Defines the SignalFrameView class with the signal frame layout. """

from PIL import Image
import customtkinter as ctk
from views.configurations_view import Config
from utils.custom_optionmenu import CustomOptionMenu


class SignalFrameView(ctk.CTkFrame):
    """
    Layout of the signal frame.
    """

    def __init__(self, master: ctk.CTkFrame = None):
        super().__init__(
            master,
            corner_radius=Config.General.CORNER_RADIUS,
            width=Config.Dimensions.SIGNAL_FRAME_WIDTH,
            border_width=Config.General.FRAME_BORDER_WIDTH,
        )
        self.root: ctk.CTk = None

        self.min_width: int = Config.Dimensions.SIGNAL_FRAME_MIN_WIDTH
        self.previous_size: int = self.winfo_width()

        self.initialize_widgets()
        self.create_layout()

    def initialize_widgets(self) -> None:
        """
        Initialize widgets.
        """
        self.filehandling_frame_view: ctk.CTkFrame = FileHandlingFrameView(self)
        self.searchbar_frame_view: ctk.CTkFrame = SearchBarFrameView(self)
        self.signallist_frame_view: ctk.CTkFrame = SignalListFrameView(self)
        self.config_signallist_frame_view: ctk.CTkFrame = ConfigSignalListFrameView(
            self
        )

    def create_layout(self) -> None:
        """
        Create layout.
        """
        self.grid_rowconfigure(
            (
                Config.Layout.SIGNALLIST_FRAME_ROW,
                Config.Layout.CONFIG_SIGNALLIST_FRAME_ROW,
            ),
            weight=1,
        )

        self.filehandling_frame_view.grid(
            row=Config.Layout.FILEHANDLING_FRAME_ROW,
            column=0,
            sticky=Config.Layout.FILEHANDLING_FRAME_STICKY,
        )

        self.searchbar_frame_view.grid(
            row=Config.Layout.SEARCHBAR_FRAME_ROW,
            column=0,
            sticky=Config.Layout.SEARCHBAR_FRAME_STICKY,
        )

        self.signallist_frame_view.grid(
            row=Config.Layout.SIGNALLIST_FRAME_ROW,
            column=0,
            sticky=Config.Layout.SIGNALLIST_FRAME_STICKY,
        )

        self.config_signallist_frame_view.grid(
            row=Config.Layout.CONFIG_SIGNALLIST_FRAME_ROW,
            column=0,
            sticky=Config.Layout.CONFIG_SIGNALLIST_FRAME_STICKY,
        )


class FileHandlingFrameView(ctk.CTkFrame):
    """
    Layout of the file handling frame.
    """

    def __init__(self, master: ctk.CTkFrame = None):
        super().__init__(
            master,
            corner_radius=Config.General.CORNER_RADIUS,
            height=Config.Dimensions.FILEHANDLING_FRAME_HEIGHT,
            border_width=Config.General.FRAME_BORDER_WIDTH,
        )

        self.initialize_widgets()
        self.create_layout()

    def initialize_widgets(self) -> None:
        """
        Initialize widgets.
        """

        self.title_label = ctk.CTkLabel(
            self,
            text=Config.LabelTexts.FILEHANDLING_TEXT,
            font=ctk.CTkFont(
                family=Config.Fonts.LABEL_TEXTS[0], size=Config.Fonts.LABEL_TEXTS[1]
            ),
            anchor=Config.Layout.SIGNAL_FRAME_LABELS_ANCHOR,
        )

        self.file_optionmenu = CustomOptionMenu(
            self,
            width=316,
            border_width=1,
            border_color="#6C6C6C",
            hover_color="#3D3E40",
            fg_color="#343638",
            font=ctk.CTkFont(
                family=Config.Fonts.LABEL_TEXTS[0], size=Config.Fonts.LABEL_TEXTS[1]
            ),
            values=Config.Values.FILE_OPTIONMENU,
            option_button_enable=False,
        )

        self.file_action_optionmenu = CustomOptionMenu(
            self,
            font=ctk.CTkFont(
                family=Config.Fonts.LABEL_TEXTS[0],
                size=Config.Fonts.LABEL_TEXTS[1],
                weight="bold",
            ),
            values=Config.Values.FILE_ACTION_OPTIONMENU,
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

        self.title_label.grid(
            row=Config.Layout.FILEHANDLING_TITLE_FARME_ROW,
            column=0,
            sticky=Config.Layout.GENERAL_FRAME_STICKY,
            padx=Config.Layout.LABELS_SOLO_PADX,
            pady=Config.Layout.STANDART_PAD,
        )

        self.file_optionmenu.grid(
            row=Config.Layout.FILEHANDLING_ENTRY_ROW,
            column=0,
            sticky=Config.Layout.GENERAL_FRAME_STICKY,
            padx=Config.Layout.STANDART_PAD,
            pady=Config.Layout.ZERO_PAD,
        )

        self.file_action_optionmenu.grid(
            row=Config.Layout.FILEHANDLING_FILTER_FARME_ROW,
            column=0,
            sticky=Config.Layout.GENERAL_FRAME_STICKY,
            padx=Config.Layout.STANDART_PAD,
            pady=Config.Layout.STANDART_PAD,
        )


class SearchBarFrameView(ctk.CTkFrame):
    """
    Layout of the search bar.
    """

    def __init__(self, master: ctk.CTkFrame = None):
        super().__init__(
            master,
            corner_radius=Config.General.CORNER_RADIUS,
            height=Config.Dimensions.SEARCHBAR_FRAME_HEIGHT,
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
            anchor=Config.Layout.SIGNAL_FRAME_LABELS_ANCHOR,
        )

        self.clear_search_result_button = ctk.CTkButton(
            self.title_frame,
            width=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            height=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            fg_color=Config.Colors.TRANSPARENT,
            hover_color=Config.Colors.BUTTON_HOVER,
            text="",
            image=ctk.CTkImage(
                light_image=Image.open(Config.ImageFormats.CLEAR_SEARCH_RESULT_ICON),
                size=(
                    Config.Dimensions.ACTION_IMAGE_WIDTH_HEIGHT,
                    Config.Dimensions.ACTION_IMAGE_WIDTH_HEIGHT,
                ),
            ),
            anchor=Config.Layout.ACTION_BUTTON_TEXT_ANCHOR,
        )

        self.search_entry = ctk.CTkEntry(
            self,
            border_width=Config.General.ENTRY_BORDER_WIDTH,
            font=ctk.CTkFont(
                family=Config.Fonts.LABEL_TEXTS[0], size=Config.Fonts.LABEL_TEXTS[1]
            ),
        )

        self.filter_frame = ctk.CTkFrame(
            self,
            corner_radius=Config.General.CORNER_RADIUS,
            fg_color=Config.Colors.TRANSPARENT,
        )

        self.search_selection_segmented_btn = ctk.CTkSegmentedButton(
            self.filter_frame,
            font=ctk.CTkFont(
                family=Config.Fonts.LABEL_TEXTS[0], size=Config.Fonts.LABEL_TEXTS[1]
            ),
            values=Config.Values.SEARCH_SELECTION_SEGMENTED_BUTTON,
        )

        self.filter_signals_segmented_btn = ctk.CTkSegmentedButton(
            self.filter_frame,
            font=ctk.CTkFont(
                family=Config.Fonts.LABEL_TEXTS[0], size=Config.Fonts.LABEL_TEXTS[1]
            ),
            values=Config.Values.FILTER_SIGNALS_SEGMENTED_BUTTON,
        )

    def create_layout(self) -> None:
        """
        Create layout.
        """

        self.rowconfigure(
            (
                Config.Layout.SEARCHBAR_FRAME_TITLE_FARME_ROW,
                Config.Layout.SEARCHBAR_FRAME_ENTRY_ROW,
                Config.Layout.SEARCHBAR_FRAME_FILTER_FARME_ROW,
            ),
            weight=1,
        )

        self.title_frame.grid(
            row=Config.Layout.SEARCHBAR_FRAME_TITLE_FARME_ROW,
            column=0,
            sticky=Config.Layout.GENERAL_FRAME_STICKY,
            padx=Config.Layout.STANDART_PAD,
            pady=Config.Layout.STANDART_PAD,
        )
        self.title_frame.columnconfigure(0, weight=1)
        self.title_frame.columnconfigure(1, weight=1)
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

        self.search_entry.grid(
            row=Config.Layout.SEARCHBAR_FRAME_ENTRY_ROW,
            column=0,
            sticky=Config.Layout.GENERAL_FRAME_STICKY,
            padx=Config.Layout.STANDART_PAD,
            pady=Config.Layout.ZERO_PAD,
        )

        self.filter_frame.grid(
            row=Config.Layout.SEARCHBAR_FRAME_FILTER_FARME_ROW,
            column=0,
            sticky=Config.Layout.GENERAL_FRAME_STICKY,
            padx=Config.Layout.STANDART_PAD,
            pady=Config.Layout.STANDART_PAD,
        )
        self.filter_frame.columnconfigure(0, weight=1)
        self.filter_frame.columnconfigure(1, weight=2)
        self.search_selection_segmented_btn.grid(
            row=0,
            column=0,
            sticky="w",
            padx=Config.Layout.RIGHT_PADX,
            pady=Config.Layout.ZERO_PAD,
        )
        self.filter_signals_segmented_btn.grid(
            row=0,
            column=1,
            sticky="e",
            padx=Config.Layout.LEFT_PADX,
            pady=Config.Layout.ZERO_PAD,
        )


class SignalListFrameView(ctk.CTkFrame):
    """
    Layout of the signal list.
    """

    def __init__(self, master: ctk.CTkFrame = None):
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
            fg_color="transparent",
            label_text=Config.LabelTexts.SIGNALLIST_TEXT,
            label_font=ctk.CTkFont(
                family=Config.Fonts.LABEL_TEXTS[0], size=Config.Fonts.LABEL_TEXTS[1]
            ),
            label_anchor=Config.Layout.SIGNAL_FRAME_LABELS_ANCHOR,
        )

    def create_layout(self) -> None:
        """
        Create layout.
        """

        self.pack_propagate(False)
        self.signal_scrollableframe.pack(
            side=Config.Layout.SIGNAL_FRAME_SCROLLABLEFRAME_SIDE,
            fill=Config.Layout.SIGNAL_FRAME_SCROLLABLEFRAME_FILL,
            expand=Config.Layout.SIGNAL_FRAME_SCROLLABLEFRAME_EXPAND,
            padx=Config.Layout.SIGNAL_FRAME_SCROLLABLEFRAME_PADX,
            pady=Config.Layout.SIGNAL_FRAME_SCROLLABLEFRAME_PADY,
        )


class ConfigSignalListFrameView(ctk.CTkFrame):
    """
    Layout of the signal configuration list.
    """

    def __init__(self, master: ctk.CTkFrame = None):
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
            fg_color="transparent",
            label_text=Config.LabelTexts.CONFIG_SIGNALLIST_TEXT,
            label_font=ctk.CTkFont(
                family=Config.Fonts.LABEL_TEXTS[0], size=Config.Fonts.LABEL_TEXTS[1]
            ),
            label_anchor=Config.Layout.SIGNAL_FRAME_LABELS_ANCHOR,
        )

    def create_layout(self) -> None:
        """
        Create layout.
        """

        self.pack_propagate(False)
        self.signal_scrollableframe.pack(
            side=Config.Layout.SIGNAL_FRAME_SCROLLABLEFRAME_SIDE,
            fill=Config.Layout.SIGNAL_FRAME_SCROLLABLEFRAME_FILL,
            expand=Config.Layout.SIGNAL_FRAME_SCROLLABLEFRAME_EXPAND,
            padx=Config.Layout.SIGNAL_FRAME_SCROLLABLEFRAME_PADX,
            pady=Config.Layout.SIGNAL_FRAME_SCROLLABLEFRAME_PADY,
        )
