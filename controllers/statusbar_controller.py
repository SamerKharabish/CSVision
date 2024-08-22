""" Defines the StatusbarFrameController class with the statusbar frame functionality. """


from configurations.statusbar_config import StatusbarConfig
from views.statusbar_view import StatusbarView
from utils.helper_functions import find_root
from utils.observer_publisher import (
    SimplePublisher,
    SimpleObserver,
    progress_publisher,
    file_size_publisher,
)


class StatusbarController(SimpleObserver):
    """
    Functionality of the statusbar.
    """

    __slots__ = ("__view",)

    def __init__(self, view: StatusbarView) -> None:
        SimpleObserver.__init__(self)
        self.__view: StatusbarView = view

        self.__view.root = find_root(self.__view)

        file_size_publisher.attach(self)
        progress_publisher.attach(self)

    def __run_progress_determinate(self) -> None:
        """
        Run the progressbar in determinate mode.
        """
        self.__view.progressbar.configure(mode="determinate")
        self.__view.progressbar.set(0)
        self.__view.progressbar.pack(
            side=StatusbarConfig.Layout.PROGRESSBAR["side"],
            padx=StatusbarConfig.Layout.PROGRESSBAR["padx"],
            pady=StatusbarConfig.Layout.PROGRESSBAR["pady"],
        )

    def __run_progress_indeterminate(self) -> None:
        """
        Run the progressbar in indeterminate mode.
        """
        self.__view.progressbar.configure(mode="indeterminate")
        self.__view.progressbar.set(0)
        self.__view.progressbar.pack(
            side=StatusbarConfig.Layout.PROGRESSBAR["side"],
            padx=StatusbarConfig.Layout.PROGRESSBAR["padx"],
            pady=StatusbarConfig.Layout.PROGRESSBAR["pady"],
        )
        self.__view.progressbar.start()

    def __stop_progress(self) -> None:
        """
        Stop the progressbar.
        """
        self.__view.progressbar.set(0)
        self.__view.progressbar.stop()
        self.__view.progressbar.pack_forget()

    def update(self, simple_publisher: SimplePublisher) -> None:
        if simple_publisher == file_size_publisher:
            self.__view.filesize_label.configure(
                text=(
                    f"{file_size_publisher.file_size:,.0f} kB".replace(",", ".")
                    if file_size_publisher.file_size
                    else "??"
                )
            )
        elif simple_publisher == progress_publisher:
            if progress_publisher.progress_mode == "indeterminate":
                self.__run_progress_indeterminate()
            elif progress_publisher.progress_mode == "determinate":
                if progress_publisher.progress == 0:
                    self.__run_progress_determinate()
                self.__view.root.after(
                    0, self.__view.progressbar.set(progress_publisher.progress)
                )
            elif progress_publisher.progress_mode == "stop":
                self.__stop_progress()

    def __del__(self) -> None:
        file_size_publisher.detach(self)
        progress_publisher.detach(self)
