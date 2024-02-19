""" Defines the SignalFrameController class with the signal frame functionality. """

import customtkinter as ctk


class SignalFrameController:
    """
    Functionality of the signal frame.
    """

    def __init__(self, view: ctk.CTkFrame = None) -> None:
        self.view: ctk.CTkFrame = view

    def on_resize_signal_frame(self, _: None = None) -> None:
        """
        Bound to the Ctrl + B press event and adjusts the width of the signal frame.
        """
        if self.view.winfo_width() > self.view.min_width:
            self.view.previous_size = self.view.winfo_width()
            self.view.root.after(0, self.view.configure(width=self.view.min_width))
        else:
            self.view.root.after(
                0,
                self.view.configure(width=self.view.previous_size),
            )
