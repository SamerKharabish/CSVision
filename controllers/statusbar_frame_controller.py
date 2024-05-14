""" Defines the StatusbarFrameController class with the statusbar frame functionality. """

from views.configurations_view import Config
from views.statusbar_frame_view import StatusbarFrameView
from utils.observer_publisher import (
    SimplePublisher,
    SimpleObserver,
    progress_publisher,
    file_size_publisher,
)


class StatusbarFrameController(SimpleObserver):
    """
    Functionality of the statusbar frame.
    """

    __slots__ = ("__view",)

    def __init__(self, view: StatusbarFrameView) -> None:
        SimpleObserver.__init__(self)
        self.__view: StatusbarFrameView = view

        file_size_publisher.attach(self)
        progress_publisher.attach(self)

    def __run_progress_indeterminate(self):
        """
        Run the progressbar in indeterminate mode.
        """
        self.__view.progressbar.configure(mode="indeterminate")
        self.__view.progressbar.set(0)
        self.__view.progressbar.pack(
            side=Config.Layout.STATUSBAR_FRAME_PROGRESSBAR_SIDE,
            padx=Config.Layout.STATUSBAR_FRAME_PROGRESSBAR_PADX,
            pady=Config.Layout.STANDART_PAD,
        )
        self.__view.progressbar.start()

    def __stop_progress(self):
        """
        Stop the progressbar.
        """
        self.__view.progressbar.set(0)
        self.__view.progressbar.stop()
        self.__view.progressbar.pack_forget()

    def update(self, simple_publisher: SimplePublisher) -> None:
        if simple_publisher == file_size_publisher:
            self.__view.filesize_label.configure(text=file_size_publisher.file_size)
        elif simple_publisher == progress_publisher:
            if simple_publisher.progress == "indeterminate":
                self.__run_progress_indeterminate()
            elif simple_publisher.progress == "stop":
                self.__stop_progress()

    def __del__(self):
        file_size_publisher.detach(self)
        progress_publisher.detach(self)
