"""Defines the StatusbarController class with the statusbar functionality."""

from configurations.statusbar_config import StatusbarConfig
from views.statusbar_view import StatusbarView
from utils.observer_publisher import (
    SimplePublisher,
    SimpleObserver,
    file_state_publisher,
    ProgressStatePublisher,
    progress_state_publisher,
)


class StatusbarController(SimpleObserver):
    """
    Functionality of the statusbar.
    """

    __slots__ = ("view",)

    def __init__(self, view: StatusbarView) -> None:
        SimpleObserver.__init__(self)
        self.view: StatusbarView = view

        file_state_publisher.attach(self)
        progress_state_publisher.attach(self)

    def start_progressbar(self, mode: str) -> None:
        """
        Start the progressbar in a specified mode.

        Args:
            mode (str): The specified mode.
        """
        self.view.progressbar.configure(mode=mode)
        self.view.progressbar.set(0)
        self.view.progressbar.pack(
            side=StatusbarConfig.Layout.PROGRESSBAR["side"],
            padx=StatusbarConfig.Layout.PROGRESSBAR["padx"],
            pady=StatusbarConfig.Layout.PROGRESSBAR["pady"],
        )

        if mode == "indeterminate":
            self.view.progressbar.start()
        else:
            self.view.progress_label.configure(text="0 %")

    def stop_progressbar(self) -> None:
        """
        Stop the progressbar.
        """
        self.view.progressbar.set(0)
        self.view.progressbar.pack_forget()
        self.view.progressbar.stop()

    def update(self, simple_publisher: SimplePublisher) -> None:
        if simple_publisher == progress_state_publisher:
            if (
                progress_state_publisher.value
                == ProgressStatePublisher.START_PROGRESSBAR
            ):
                self.start_progressbar(progress_state_publisher.mode)
            elif (
                progress_state_publisher.value
                == ProgressStatePublisher.STOP_PROGRESSBAR
            ):
                self.stop_progressbar()
            else:
                self.view.root.after(
                    0, self.view.progressbar.set(progress_state_publisher.value)
                )
        elif simple_publisher == file_state_publisher:
            if file_state_publisher.is_open is True:
                filesize_label_text: str = (
                    f"{float(file_state_publisher.file_size):,.0f} kB".replace(",", ".")
                )
                file_state_publisher.set_is_open(False, self)
            else:
                filesize_label_text: str = "--"
            self.view.filesize_label.configure(text=filesize_label_text)

    def __del__(self) -> None:
        file_state_publisher.detach(self)
        progress_state_publisher.detach(self)
