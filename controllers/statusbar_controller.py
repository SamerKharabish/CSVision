"""Defines the StatusbarController class with the statusbar functionality."""

from typing import Literal
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

        self._mode: Literal["determinate", "indeterminate"]
        self._value: float = 0.0

        file_state_publisher.attach(self)
        progress_state_publisher.attach(self)

    def start_progressbar(self) -> None:
        """
        Start the progressbar in a specified mode.
        """
        self.view.progressbar.configure(mode=self._mode)
        self.view.progressbar.set(0)
        self.view.progressbar.pack(
            side=StatusbarConfig.Layout.PROGRESSBAR["side"],
            padx=StatusbarConfig.Layout.PROGRESSBAR["padx"],
            pady=StatusbarConfig.Layout.PROGRESSBAR["pady"],
        )

        if self._mode == "indeterminate":
            self.view.progressbar.start()
        else:
            self.view.progress_label.configure(text=f"{int(self._value)} %")
            self.view.progress_label.pack(
                side=StatusbarConfig.Layout.PROGRESS_LABEL["side"],
                padx=StatusbarConfig.Layout.PROGRESS_LABEL["padx"],
                pady=StatusbarConfig.Layout.PROGRESS_LABEL["pady"],
            )

    def determinate_progress(self) -> None:
        """
        Set the value of the progressbar in determinate mode.
        """
        self.view.progress_label.configure(text=f"{int(self._value)} %")
        self.view.progressbar.set(self._value / 100)

    def stop_progressbar(self) -> None:
        """
        Stop the progressbar.
        """
        if self._mode == "determinate":
            self.view.progress_label.configure(text=f"{int(self._value)} %")
            self.view.progress_label.pack_forget()
        self.view.progressbar.pack_forget()
        self.view.progressbar.set(0)
        self.view.progressbar.stop()

    def update(self, simple_publisher: SimplePublisher) -> None:
        if simple_publisher == progress_state_publisher:
            self._mode = progress_state_publisher.mode
            self._value = progress_state_publisher.value

            if self._value == ProgressStatePublisher.START_PROGRESSBAR:
                self.start_progressbar()
            elif self._value == ProgressStatePublisher.STOP_PROGRESSBAR:
                self.stop_progressbar()
            else:
                self.view.root.after(
                    0,
                    self.determinate_progress,
                )
        elif simple_publisher == file_state_publisher:
            self.view.filesize_label.configure(text="--")
            if file_state_publisher.is_open is True:
                filesize_label_text: str = (
                    f"{float(file_state_publisher.file_size):,.0f} kB".replace(",", ".")
                )
                file_state_publisher.set_is_open(False, self)
                self.view.filesize_label.configure(text=filesize_label_text)

    def __del__(self) -> None:
        file_state_publisher.detach(self)
        progress_state_publisher.detach(self)
