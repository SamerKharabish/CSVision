""" Defines the SignalFrameView class with the signal frame layout. """

import customtkinter as ctk
from views.configurations_view import Config


class SignalFrameView(ctk.CTkFrame):
    """
    Layout of the signal frame.
    """

    def __init__(self, master=None):
        super().__init__(
            master,
            corner_radius=Config.Radii.INNER_RADIUS,
            width=Config.Dimensions.SIGNAL_FRAME_WIDTH,
        )
