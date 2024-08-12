""" Defines the StatusbarFrameView class with the statusbar frame layout. """

from __future__ import annotations
from typing import TYPE_CHECKING
import customtkinter as ctk
from .configurations_view import StatusbarConfig

if TYPE_CHECKING:
    from .main_view import MainView


class StatusbarFrameView(ctk.CTkFrame):
    """
    Layout of the statusbar frame.
    """

    __slots__ = "filesize_label", "progressbar"

    def __init__(self, master: MainView) -> None:
        super().__init__(
            master,
            height=StatusbarConfig.Dimensions.HEIGHT,
            corner_radius=StatusbarConfig.General.CORNER_RADIUS,
            border_width=StatusbarConfig.General.FRAME_BORDER_WIDTH,
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
                family=StatusbarConfig.Fonts.FILSIZE_LABEL_FONT,
                size=StatusbarConfig.Fonts.FILSIZE_LABEL_FONT_SIZE,
            ),
        )
        self.progressbar: ctk.CTkProgressBar = ctk.CTkProgressBar(self, width=310)

    def __create_layout(self) -> None:
        """
        Create layout.
        """
        self.pack_propagate(False)
        self.filesize_label.pack(
            side=StatusbarConfig.Layout.FILSIZE_LABEL_SIDE,
            padx=StatusbarConfig.Layout.FILSIZE_LABEL_PADX,
            pady=StatusbarConfig.Layout.FILSIZE_LABEL_PADY,
        )
