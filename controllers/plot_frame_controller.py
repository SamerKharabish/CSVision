""" Defines the PlotFrameController class with the plot frame functionality. """

import customtkinter as ctk


class PlotFrameController:
    """
    Functionality of the plot frame.
    """

    def __init__(self, view: ctk.CTkFrame) -> None:
        self.__view: ctk.CTkFrame = view
