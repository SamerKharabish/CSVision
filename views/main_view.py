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

    def __init__(self, master=None):
        super().__init__(master, corner_radius=Config.Radii.OUTER_RADIUS)
        self.master = master
        self.pack(
            side=Config.Layout.MAIN_VIEW_SIDE,
            fill=Config.Layout.MAIN_VIEW_FILL,
            expand=Config.Layout.MAIN_VIEW_EXPAND,
            padx=Config.Padding.PADX,
            pady=Config.Padding.PADY,
        )

        self.initialize_widgets()
        self.create_layout()

    def initialize_widgets(self):
        """
        Initialize widgets.
        """
        self.statusbar_frame = StatusbarFrameView(self)
        self.signal_frame = SignalFrameView(self)
        self.plot_frame = PlotFrameView(self)

    def create_layout(self):
        """
        Create layout.
        """
        self.statusbar_frame.pack(
            side=Config.Layout.STATUSBAR_FRAME_SIDE,
            fill=Config.Layout.STATUSBAR_FRAME_FILL,
            expand=Config.Layout.STATUSBAR_FRAME_EXPAND,
            padx=Config.Padding.PADX,
            pady=Config.Padding.PADY_TOP_SHORT,
        )
        self.signal_frame.pack(
            side=Config.Layout.SIGNAL_FRAME_SIDE,
            fill=Config.Layout.SIGNAL_FRAME_FILL,
            expand=Config.Layout.SIGNAL_FRAME_EXPAND,
            padx=Config.Padding.PADX_RIGHT_SHORT,
            pady=Config.Padding.PADY_BOTTOM_SHORT,
        )
        self.plot_frame.pack(
            side=Config.Layout.PLOT_FRAME_SIDE,
            fill=Config.Layout.PLOT_FRAME_FILL,
            expand=Config.Layout.PLOT_FRAME_EXPAND,
            padx=Config.Padding.PADX_LEFT_SHORT,
            pady=Config.Padding.PADY_BOTTOM_SHORT,
        )
