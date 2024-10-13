""" Defines the ConfigHeaderListFrameView class with the configuration header list frame layout. """

from __future__ import annotations
from typing import TYPE_CHECKING
import customtkinter as ctk
from views.configurations_view import Config

if TYPE_CHECKING:
    from sidebar_view import SidebarView


class ConfigHeaderListFrameView(ctk.CTkFrame):
    """
    Layout of the configuration header list frame.
    """

    def __init__(self, master: SidebarView) -> None:
        super().__init__(
            master,
            corner_radius=Config.General.CORNER_RADIUS,
            border_width=Config.General.FRAME_BORDER_WIDTH,
        )

        self.__initialize_widgets()
        self.__create_layout()

    def __initialize_widgets(self) -> None:
        """
        Initialize widgets.
        """
        self.header_scrollableframe = ctk.CTkScrollableFrame(
            self,
            fg_color=Config.Colors.TRANSPARENT,
            label_text=Config.LabelTexts.CONFIG_HEADER_LIST_TEXT,
            label_font=ctk.CTkFont(
                family=Config.Fonts.FONT_SIZE_WEIGHT[0],
                size=Config.Fonts.FONT_SIZE_WEIGHT[1],
                weight=Config.Fonts.FONT_SIZE_WEIGHT[2],
            ),
            label_anchor=Config.Layout.HEADER_FRAME_LABELS_ANCHOR,
        )

    def __create_layout(self) -> None:
        """
        Create layout.
        """
        self.pack_propagate(False)
        self.header_scrollableframe.pack(
            side=Config.Layout.HEADER_FRAME_SCROLLABLEFRAME_SIDE,
            fill=Config.Layout.HEADER_FRAME_SCROLLABLEFRAME_FILL,
            expand=Config.Layout.HEADER_FRAME_SCROLLABLEFRAME_EXPAND,
            padx=Config.Layout.HEADER_FRAME_SCROLLABLEFRAME_PAD,
            pady=Config.Layout.HEADER_FRAME_SCROLLABLEFRAME_PAD,
        )
