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
