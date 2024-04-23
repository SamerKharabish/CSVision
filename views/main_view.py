""" Defines the MainView class with the main layout. """

from __future__ import annotations
from typing import TYPE_CHECKING
import customtkinter as ctk
from views.configurations_view import Config
from views.statusbar_frame_view import StatusbarFrameView
from views.signal_frame_view import SignalFrameView
from views.plot_frame_view import PlotFrameView


if TYPE_CHECKING:
    from app import AppView


class MainView(ctk.CTkFrame):
    """
    Layout of the main application.
    """

    __slots__ = "root", "statusbar_frame_view", "signal_frame_view", "plot_frame_view"
  
    def __init__(self, master: AppView) -> None:
        super().__init__(master, corner_radius=Config.General.CORNER_RADIUS)
        self.root: AppView

        self.__initialize_widgets()
        self.__create_layout()

    def __initialize_widgets(self) -> None:
        """
        Initialize widgets.
        """
        self.statusbar_frame_view: StatusbarFrameView = StatusbarFrameView(self)
        self.signal_frame_view: SignalFrameView = SignalFrameView(self)
        self.plot_frame_view: PlotFrameView = PlotFrameView(self)

    def __create_layout(self) -> None:
        """
        Create layout.
        """
        self.statusbar_frame_view.pack(
            side=Config.Layout.STATUSBAR_FRAME_SIDE,
            fill=Config.Layout.STATUSBAR_FRAME_FILL,
            expand=Config.Layout.STATUSBAR_FRAME_EXPAND,
        )

        self.signal_frame_view.pack(
            side=Config.Layout.SIGNAL_FRAME_SIDE,
            fill=Config.Layout.SIGNAL_FRAME_FILL,
            expand=Config.Layout.SIGNAL_FRAME_EXPAND,
        )

        self.plot_frame_view.pack(
            side=Config.Layout.PLOT_FRAME_SIDE,
            fill=Config.Layout.PLOT_FRAME_FILL,
            expand=Config.Layout.PLOT_FRAME_EXPAND,
        )
