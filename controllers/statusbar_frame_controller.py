""" Defines the StatusbarFrameController class with the statusbar frame functionality. """

import customtkinter as ctk
from utils.observer_publisher import SimplePublisher, SimpleObserver
from controllers.signal_frame_controller import file_size_publisher


class StatusbarFrameController(SimpleObserver):
    """
    Functionality of the statusbar frame.
    """

    def __init__(self, view: ctk.CTkFrame) -> None:
        SimpleObserver.__init__(self)
        self.view: ctk.CTkFrame = view

        self._file_size_publisher: SimplePublisher = file_size_publisher
        self._file_size_publisher.attach(self)

    def update(self, simple_publisher: SimplePublisher) -> None:
        if simple_publisher == self._file_size_publisher:
            self.view.filesize_label.configure(text=self._file_size_publisher.file_size)
