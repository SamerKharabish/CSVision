""" Defines the StatusbarFrameController class with the statusbar frame functionality. """

import customtkinter as ctk


class StatusbarFrameController:
    """
    Functionality of the statusbar frame.
    """

    def __init__(self, view: ctk.CTkFrame) -> None:
        self.view: ctk.CTkFrame = view
