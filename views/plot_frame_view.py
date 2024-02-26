""" Defines the PlotFrameView class with the plot frame layout. """

import customtkinter as ctk
from views.configurations_view import Config


class PlotFrameView(ctk.CTkFrame):
    """
    Layout of the plot frame.
    """

    def __init__(self, master: ctk.CTkFrame = None):
        super().__init__(
            master,
            corner_radius=Config.General.CORNER_RADIUS,
            border_width=Config.General.FRAME_BORDER_WIDTH,
        )

        self.initialize_widgets()
        self.create_layout()

    def initialize_widgets(self) -> None:
        """
        Initialize widgets.
        """

    def create_layout(self) -> None:
        """
        Create layout.
        """
