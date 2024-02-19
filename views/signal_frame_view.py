""" Defines the SignalFrameView class with the signal frame layout. """

import customtkinter as ctk
from views.configurations_view import Config


class SignalFrameView(ctk.CTkFrame):
    """
    Layout of the signal frame.
    """

    def __init__(self, master: ctk.CTkFrame = None):
        super().__init__(
            master,
            corner_radius=Config.General.CORNER_RADIUS,
            width=Config.Dimensions.SIGNAL_FRAME_WIDTH,
            border_width=Config.General.BORDER_WIDTH,
        )
        self.root: ctk.CTk = master.master

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
            (Config.Layout.SIGNALLIST_ROW, Config.Layout.CONFIG_SIGNALLIST_ROW),
            weight=1,
        )

        self.filehandling_frame_view.grid(
            row=Config.Layout.FILEHANDLING_ROW,
            column=0,
            sticky=Config.Layout.FILEHANDLING_STICKY,
        )

        self.searchbar_frame_view.grid(
            row=Config.Layout.SEARCHBAR_ROW,
            column=0,
            sticky=Config.Layout.SEARCHBAR_STICKY,
        )

        self.signallist_frame_view.grid(
            row=Config.Layout.SIGNALLIST_ROW,
            column=0,
            sticky=Config.Layout.SIGNALLIST_STICKY,
        )

        self.config_signallist_frame_view.grid(
            row=Config.Layout.CONFIG_SIGNALLIST_ROW,
            column=0,
            sticky=Config.Layout.CONFIG_SIGNALLIST_STICKY,
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
            border_width=Config.General.BORDER_WIDTH,
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

    def create_layout(self) -> None:
        """
        Create layout.
        """

        self.pack_propagate(False)
        self.title_label.pack(
            side=Config.Layout.SIGNAL_FRAME_LABELS_SIDE,
            fill=Config.Layout.SIGNAL_FRAME_LABELS_FILL,
            expand=Config.Layout.SIGNAL_FRAME_LABELS_EXPAND,
            padx=Config.Layout.SIGNAL_FRAME_LABELS_PADX,
            pady=Config.Layout.SIGNAL_FRAME_LABELS_PADy,
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
            border_width=Config.General.BORDER_WIDTH,
        )

        self.initialize_widgets()
        self.create_layout()

    def initialize_widgets(self) -> None:
        """
        Initialize widgets.
        """
        self.title_label = ctk.CTkLabel(
            self,
            text=Config.LabelTexts.SEARCHBAR_TEXT,
            font=ctk.CTkFont(
                family=Config.Fonts.LABEL_TEXTS[0], size=Config.Fonts.LABEL_TEXTS[1]
            ),
            anchor=Config.Layout.SIGNAL_FRAME_LABELS_ANCHOR,
        )

    def create_layout(self) -> None:
        """
        Create layout.
        """

        self.pack_propagate(False)
        self.title_label.pack(
            side=Config.Layout.SIGNAL_FRAME_LABELS_SIDE,
            fill=Config.Layout.SIGNAL_FRAME_LABELS_FILL,
            expand=Config.Layout.SIGNAL_FRAME_LABELS_EXPAND,
            padx=Config.Layout.SIGNAL_FRAME_LABELS_PADX,
            pady=Config.Layout.SIGNAL_FRAME_LABELS_PADy,
        )


class SignalListFrameView(ctk.CTkFrame):
    """
    Layout of the signal list.
    """

    def __init__(self, master: ctk.CTkFrame = None):
        super().__init__(
            master,
            corner_radius=Config.General.CORNER_RADIUS,
            border_width=Config.General.BORDER_WIDTH,
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
            pady=Config.Layout.SIGNAL_FRAME_SCROLLABLEFRAME_PADy,
        )


class ConfigSignalListFrameView(ctk.CTkFrame):
    """
    Layout of the signal configuration list.
    """

    def __init__(self, master: ctk.CTkFrame = None):
        super().__init__(
            master,
            corner_radius=Config.General.CORNER_RADIUS,
            border_width=Config.General.BORDER_WIDTH,
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
            pady=Config.Layout.SIGNAL_FRAME_SCROLLABLEFRAME_PADy,
        )
