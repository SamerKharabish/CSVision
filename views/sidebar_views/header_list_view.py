""" Defines the HeaderListView class with the header list layout. """

from __future__ import annotations
from typing import TYPE_CHECKING
import customtkinter as ctk
from configurations.header_list_config import HeaderListConfig
from utils.select_button import SelectButton

if TYPE_CHECKING:
    from sidebar_view import SidebarView


class HeaderListView(ctk.CTkFrame):
    """
    Layout of the header list.
    """

    __slots__ = (
        "filter_mode_var",
        "filter_mode_segmented_button",
        "header_scrollableframe",
    )

    def __init__(self, master: SidebarView) -> None:
        super().__init__(
            master,
            corner_radius=HeaderListConfig.OwnArgs.CORNER_RADIUS,
            border_width=HeaderListConfig.OwnArgs.BORDER_WIDTH,
            fg_color=HeaderListConfig.OwnArgs.TRANSPARENT,
        )

        self.initialize_widgets()
        self.create_layout()

    def initialize_widgets(self) -> None:
        """
        Initialize widgets.
        """
        self.filter_mode_var: ctk.StringVar = ctk.StringVar(
            value=HeaderListConfig.Texts.FILTER_MODE_OPTIONS[0]
        )
        self.filter_mode_segmented_button: ctk.CTkSegmentedButton = (
            ctk.CTkSegmentedButton(
                self,
                font=ctk.CTkFont(
                    family=HeaderListConfig.Widgets.FILTER_MODE_SEG_BUTTON["family"],  # type: ignore
                    size=HeaderListConfig.Widgets.FILTER_MODE_SEG_BUTTON["size"],  # type: ignore
                    weight=HeaderListConfig.Widgets.FILTER_MODE_SEG_BUTTON["weight"],  # type: ignore
                ),
                values=HeaderListConfig.Texts.FILTER_MODE_OPTIONS,
                variable=self.filter_mode_var,
            )
        )

        self.header_scrollableframe: ctk.CTkScrollableFrame = ctk.CTkScrollableFrame(
            self,
            label_text=HeaderListConfig.Widgets.HEADER_SCROLLABLEFRAME["label_text"],  # type: ignore
            label_font=ctk.CTkFont(
                family=HeaderListConfig.Widgets.HEADER_SCROLLABLEFRAME["family"],  # type: ignore
                size=HeaderListConfig.Widgets.HEADER_SCROLLABLEFRAME["size"],  # type: ignore
                weight=HeaderListConfig.Widgets.HEADER_SCROLLABLEFRAME["weight"],  # type: ignore
            ),
            label_anchor=HeaderListConfig.Widgets.HEADER_SCROLLABLEFRAME[  # type: ignore
                "label_anchor"
            ],
        )

        # Needed so widgets inside use whole width of the scrollable frame
        self.header_scrollableframe.columnconfigure(
            HeaderListConfig.Layout.HEADER_SCROLLABLEFRAME["column"],
            weight=HeaderListConfig.Layout.HEADER_SCROLLABLEFRAME["column_weight"],  # type: ignore
        )

    def create_layout(self) -> None:
        """
        Create layout.
        """
        self.header_scrollableframe.pack(
            side=HeaderListConfig.Layout.HEADER_SCROLLABLEFRAME["side"],
            fill=HeaderListConfig.Layout.HEADER_SCROLLABLEFRAME["fill"],
            expand=HeaderListConfig.Layout.HEADER_SCROLLABLEFRAME["expand"],
            padx=HeaderListConfig.Layout.HEADER_SCROLLABLEFRAME["padx"],
            pady=HeaderListConfig.Layout.HEADER_SCROLLABLEFRAME["pady"],
        )

        self.filter_mode_segmented_button.pack(
            side=HeaderListConfig.Layout.FILTER_MODE_SEG_BUTTON["side"],
            fill=HeaderListConfig.Layout.FILTER_MODE_SEG_BUTTON["fill"],
            expand=HeaderListConfig.Layout.FILTER_MODE_SEG_BUTTON["expand"],
            padx=HeaderListConfig.Layout.FILTER_MODE_SEG_BUTTON["padx"],
            pady=HeaderListConfig.Layout.FILTER_MODE_SEG_BUTTON["pady"],
        )

    def add_label_to_header_scrollableframe(self) -> ctk.CTkLabel:
        """
        Add a group label to the header_scrollableframe.

        Returns:
            ctk.CTkLabel: A group label.
        """
        label = ctk.CTkLabel(
            self.header_scrollableframe,
            anchor=HeaderListConfig.Widgets.HEADER_SCROLLABLEFRAME_WIDGETS["label_anchor"],  # type: ignore
            font=ctk.CTkFont(
                family=HeaderListConfig.Widgets.HEADER_SCROLLABLEFRAME_WIDGETS["family"],  # type: ignore
                size=HeaderListConfig.Widgets.HEADER_SCROLLABLEFRAME_WIDGETS["size"],  # type: ignore
                weight=HeaderListConfig.Widgets.HEADER_SCROLLABLEFRAME_WIDGETS["weight"],  # type: ignore
            ),
        )

        return label

    def manage_label(self, label: ctk.CTkLabel, text: str, index: int) -> None:
        """
        Updates the text and position of a label.

        Args:
            label (ctk.CTkLabel): The label to update and grid.
            text (str): The text that needs to be updated.
            index (int): The index of the label in the grid.
        """
        label.configure(text=text)
        label.grid(
            row=index,
            column=HeaderListConfig.Layout.HEADER_SCROLLABLEFRAME["column"],
            sticky=HeaderListConfig.Layout.HEADER_SCROLLABLEFRAME_WIDGETS["sticky"],
            padx=HeaderListConfig.Layout.HEADER_SCROLLABLEFRAME_WIDGETS["label_padx"],
            pady=HeaderListConfig.Layout.HEADER_SCROLLABLEFRAME_WIDGETS["label_pady"],
        )

    def add_button_to_header_scrollableframe(self) -> SelectButton:
        """
        Add a button to the header_scrollableframe.

        Returns:
            SelectButton: A group label.
        """
        button = SelectButton(
            self.header_scrollableframe,
            height=HeaderListConfig.Widgets.HEADER_SCROLLABLEFRAME_WIDGETS["button_height"],  # type: ignore
            corner_radius=HeaderListConfig.Widgets.HEADER_SCROLLABLEFRAME_WIDGETS["button_corner_radius"],  # type: ignore
            font=ctk.CTkFont(
                family=HeaderListConfig.Widgets.HEADER_SCROLLABLEFRAME_WIDGETS["family"],  # type: ignore
                size=HeaderListConfig.Widgets.HEADER_SCROLLABLEFRAME_WIDGETS["size"],  # type: ignore
            ),
        )

        return button

    def manage_button(self, button: SelectButton, text: str, index: int) -> None:
        """
        Updates the text and position of a button.

        Args:
            button (SelectButton): The button to update and grid.
            text (str): The text that needs to be updated.
            index (int): The index of the button in the grid.
        """
        button.configure(text=text)
        button.grid(
            row=index,
            column=HeaderListConfig.Layout.HEADER_SCROLLABLEFRAME["column"],
            sticky=HeaderListConfig.Layout.HEADER_SCROLLABLEFRAME_WIDGETS["sticky"],
            padx=HeaderListConfig.Layout.HEADER_SCROLLABLEFRAME_WIDGETS["button_padx"],
            pady=HeaderListConfig.Layout.HEADER_SCROLLABLEFRAME_WIDGETS["button_pady"],
        )
