""" Defines the MainView class with the main layout. """

import customtkinter as ctk
from views.configurations_view import Config


class MainView(ctk.CTkFrame):
    """
    Layout of the main application.
    """

    def __init__(self, master=None):
        super().__init__(master, corner_radius=Config.Radii.CONTENT_FRAME_RADIUS)
        self.pack_propagate(False)
        self.pack(side="top", fill="both", expand=True, padx=(8, 8), pady=(8, 8))
