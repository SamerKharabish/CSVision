"""Defines the PlotFrameController class with the plot frame functionality."""

import customtkinter as ctk


class PlotController:
    """
    Functionality of the plot frame.
    """

    def __init__(self, view: ctk.CTkFrame) -> None:
        self.__view: ctk.CTkFrame = view
