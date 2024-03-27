""" Defines the StatusbarFrameController class with the statusbar frame functionality. """

import customtkinter as ctk
from views.configurations_view import Config
from utils.observer_publisher import SimplePublisher, SimpleObserver
from controllers.signal_frame_controller import file_size_publisher, progress_publisher


class StatusbarFrameController(SimpleObserver):
    """
    Functionality of the statusbar frame.
    """

    def __init__(self, view: ctk.CTkFrame) -> None:
        SimpleObserver.__init__(self)
        self.view: ctk.CTkFrame = view

        self._file_size_publisher: SimplePublisher = file_size_publisher
        self._file_size_publisher.attach(self)

        self._progress_publisher: SimplePublisher = progress_publisher
        self._progress_publisher.attach(self)

    def run_progress_indeterminate(self):
        """
        Run the progressbar in indeterminate mode.
        """
        self.view.progressbar.configure(mode="indeterminate")
        self.view.progressbar.set(0)
        self.view.progressbar.pack(
            side=Config.Layout.STATUSBAR_FRAME_PROGRESSBAR_SIDE,
            padx=Config.Layout.STATUSBAR_FRAME_PROGRESSBAR_PADX,
            pady=Config.Layout.STANDART_PAD,
        )
        self.view.progressbar.start()

    def stop_progress(self):
        """
        Stop the progressbar.
        """
        self.view.progressbar.set(0)
        self.view.progressbar.stop()
        self.view.progressbar.pack_forget()

    def update(self, simple_publisher: SimplePublisher) -> None:
        if simple_publisher == self._file_size_publisher:
            self.view.filesize_label.configure(text=self._file_size_publisher.file_size)
        elif simple_publisher == self._progress_publisher:
            if simple_publisher.progress == "indeterminate":
                self.run_progress_indeterminate()
            elif simple_publisher.progress == "stop":
                self.stop_progress()
