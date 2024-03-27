""" Defines the StatusbarFrameView class with the statusbar frame layout. """

import customtkinter as ctk
from views.configurations_view import Config


class StatusbarFrameView(ctk.CTkFrame):
    """
    Layout of the statusbar frame.
    """

    def __init__(self, master: ctk.CTkFrame) -> None:
        super().__init__(
            master,
            corner_radius=Config.General.CORNER_RADIUS,
            height=Config.Dimensions.STATUSBAR_FRAME_HEIGHT,
            border_width=Config.General.FRAME_BORDER_WIDTH,
        )

        self.initialize_widgets()
        self.create_layout()

    def initialize_widgets(self) -> None:
        """
        Initialize widgets.
        """
        self.filesize_label = ctk.CTkLabel(
            self,
            text="0.0 kB",
            font=ctk.CTkFont(
                family=Config.Fonts.STATUS_BAR_TEXTS[0],
                size=Config.Fonts.STATUS_BAR_TEXTS[1],
            ),
        )
        self.progressbar = ctk.CTkProgressBar(self, width=310)

    def create_layout(self) -> None:
        """
        Create layout.
        """
        self.filesize_label.pack(side="left", padx=(50, 10), pady=(1, 1))

        self.progressbar.pack(
            side="left", padx=(10, 10), pady=Config.Layout.STANDART_PAD
        )
