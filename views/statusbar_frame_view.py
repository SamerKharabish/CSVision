""" Defines the StatusbarFrameView class with the statusbar frame layout. """

from __future__ import annotations
from typing import TYPE_CHECKING
import customtkinter as ctk
from views.configurations_view import Config

if TYPE_CHECKING:
    from views.main_view import MainView


class StatusbarFrameView(ctk.CTkFrame):
    """
    Layout of the statusbar frame.
    """

    __slots__ = "filesize_label", "progressbar"

    def __init__(self, master: MainView) -> None:
        super().__init__(
            master,
            corner_radius=Config.General.CORNER_RADIUS,
            height=Config.Dimensions.STATUSBAR_FRAME_HEIGHT,
            border_width=Config.General.FRAME_BORDER_WIDTH,
        )

        self.__initialize_widgets()
        self.__create_layout()

    def __initialize_widgets(self) -> None:
        """
        Initialize widgets.
        """
        self.filesize_label: ctk.CTkLabel = ctk.CTkLabel(
            self,
            text="",
            font=ctk.CTkFont(
                family=Config.Fonts.STATUS_BAR_TEXTS[0],
                size=Config.Fonts.STATUS_BAR_TEXTS[1],
            ),
        )
        self.progressbar: ctk.CTkProgressBar = ctk.CTkProgressBar(self, width=310)

    def __create_layout(self) -> None:
        """
        Create layout.
        """
        self.pack_propagate(False)
        self.filesize_label.pack(
            side=Config.Layout.STATUSBAR_FRAME_LABEL_SIDE,
            padx=Config.Layout.STATUSBAR_FRAME_LABEL_PADX,
            pady=Config.Layout.STATUSBAR_FRAME_LABEL_PADY,
        )
