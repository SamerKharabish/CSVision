""" Defines the StatusbarFrameView class with the statusbar frame layout. """

import customtkinter as ctk
from views.configurations_view import Config


class StatusbarFrameView(ctk.CTkFrame):
    """
    Layout of the statusbar frame.
    """

    def __init__(self, master: ctk.CTkFrame = None):
        super().__init__(
            master,
            corner_radius=Config.General.CORNER_RADIUS,
            height=Config.Dimensions.STATUSBAR_FRAME_HEIGHT,
            border_width=Config.General.BORDER_WIDTH,
        )
