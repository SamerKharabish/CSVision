""" Defines the StatusbarView class with the statusbar layout. """

from __future__ import annotations
from typing import TYPE_CHECKING
import customtkinter as ctk
from configurations.statusbar_config import StatusbarConfig

if TYPE_CHECKING:
    from .main_view import MainView


class StatusbarView(ctk.CTkFrame):
    """
    Layout of the statusbar.
    """

    __slots__ = "filesize_label", "progressbar", "__progress_label"

    def __init__(self, master: MainView) -> None:
        super().__init__(
            master,
            height=StatusbarConfig.OwnArgs.HEIGHT,
            corner_radius=StatusbarConfig.OwnArgs.CORNER_RADIUS,
            border_width=StatusbarConfig.OwnArgs.BORDER_WIDTH,
            fg_color=StatusbarConfig.OwnArgs.TRANSPARENT,
        )

        self.__initialize_widgets()
        self.__create_layout()

    def __initialize_widgets(self) -> None:
        """
        Initialize widgets.
        """
        self.filesize_label: ctk.CTkLabel = ctk.CTkLabel(
            self,
            text=StatusbarConfig.Widgets.FILESIZE_LABEL["text"],
            font=ctk.CTkFont(
                family=StatusbarConfig.Widgets.FILESIZE_LABEL["family"],
                size=StatusbarConfig.Widgets.FILESIZE_LABEL["size"],
            ),
        )

        self.progressbar: ctk.CTkProgressBar = ctk.CTkProgressBar(
            self, width=StatusbarConfig.Widgets.PROGRESSBAR["width"]
        )

        # TODO: add functionality
        self.__progress_label: ctk.CTkLabel = ctk.CTkLabel(
            self,
            text=StatusbarConfig.Widgets.PROGRESS_LABEL["text"],
            font=ctk.CTkFont(
                family=StatusbarConfig.Widgets.PROGRESS_LABEL["family"],
                size=StatusbarConfig.Widgets.PROGRESS_LABEL["size"],
            ),
        )

    def __create_layout(self) -> None:
        """
        Create layout.
        """
        self.pack_propagate(False)
        self.filesize_label.pack(
            side=StatusbarConfig.Layout.FILESIZE_LABEL["side"],
            padx=StatusbarConfig.Layout.FILESIZE_LABEL["padx"],
            pady=StatusbarConfig.Layout.FILESIZE_LABEL["pady"],
        )
