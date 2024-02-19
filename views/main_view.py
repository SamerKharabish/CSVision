""" Defines the MainView class with the main layout. """

import customtkinter as ctk
from views.configurations_view import Config
from views.statusbar_frame_view import StatusbarFrameView
from views.signal_frame_view import SignalFrameView
from views.plot_frame_view import PlotFrameView


class MainView(ctk.CTkFrame):
    """
    Layout of the main application.
    """

    def __init__(self, master: ctk.CTk = None) -> None:
        super().__init__(master, corner_radius=Config.General.CORNER_RADIUS)
        self.master: ctk.CTk = master

        self.initialize_widgets()
        self.create_layout()

    def initialize_widgets(self) -> None:
        """
        Initialize widgets.
        """
        self.statusbar_frame_view: ctk.CTkFrame = StatusbarFrameView(self)
        self.signal_frame_view: ctk.CTkFrame = SignalFrameView(self)
        self.plot_frame_view: ctk.CTkFrame = PlotFrameView(self)

    def create_layout(self) -> None:
        """
        Create layout.
        """
        self.pack(
            side=Config.Layout.MAIN_VIEW_SIDE,
            fill=Config.Layout.MAIN_VIEW_FILL,
            expand=Config.Layout.MAIN_VIEW_EXPAND,
        )

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
