""" Defines the SignalFrameController class with the signal frame functionality. """


class SignalFrameController:
    """
    Functionality of the signal frame.
    """

    def __init__(self, view=None) -> None:
        self.view = view

    def on_resize_signal_frame(self, _=None):
        """
        Bound to the Ctrl + B press event and adjusts the width of the signal frame.
        """
        if self.view.winfo_width() > self.view.min_width:
            self.view.previous_size = self.view.winfo_width()
            self.view.master.master.after(
                0, self.view.configure(width=self.view.min_width)
            )
        else:
            self.view.master.master.after(
                0,
                self.view.configure(width=self.view.previous_size),
            )
