""" Defines all subscriptable publisher classes and the observer interface. """

from __future__ import annotations
from abc import ABC, abstractmethod


class SimplePublisher:
    """
    Represents a simple publisher.
    """

    def __init__(self) -> None:
        """
        Create an empty observer list.
        """
        self._observers: list[SimpleObserver] = []

    def attach(self, observer: SimpleObserver) -> None:
        """
        Attach an observer to the list if not already attached.

        Args:
            observer (SimpleObserver): Observer to be attached.
        """
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: SimpleObserver) -> None:
        """
        Detach an observer from the list if attached.

        Args:
            observer (SimpleObserver): Observer to be dettached.
        """
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, modifier: SimpleObserver | None = None) -> None:
        """
        Notify all registered observers, except the one that might have triggered the update.

        Args:
            modifier (SimpleObserver | None, optional): Observer that triggered the update. Defaults to None.
        """
        for observer in self._observers:
            if observer != modifier:
                observer.update(self)


class ProgressPublisher(SimplePublisher):
    """
    Monitor the progress of the data loading thread.
    """

    def __init__(self) -> None:
        SimplePublisher.__init__(self)

        self.__progress: str

    @property
    def progress(self) -> str:
        """
        Get the progress.

        Returns:
            str: The set progress.
        """
        return self.__progress

    @progress.setter
    def progress(self, progress: str) -> None:
        """
        Set the progress.

        Args:
            progress (str): The progress to set.
        """
        self.__progress = progress
        self.notify()


progress_publisher = ProgressPublisher()


class FileSizePublisher(SimplePublisher):
    """
    Monitor the file size.
    """

    def __init__(self) -> None:
        SimplePublisher.__init__(self)

        self.__file_size: str

    @property
    def file_size(self) -> str:
        """
        Get the file size.

        Returns:
            str: The set file size.
        """
        return self.__file_size

    @file_size.setter
    def file_size(self, file_size: str | None) -> None:
        """
        Set the file size.

        Args:
            file_size (str): The file size to set.
        """
        self.__file_size = (
            f"{file_size:,.0f} kB".replace(",", ".") if file_size else "??"
        )
        self.notify()


file_size_publisher = FileSizePublisher()


class HeaderFrameStatePublisher(SimplePublisher):
    """
    Monitor the state of the header frame.
    """

    def __init__(self) -> None:
        SimplePublisher.__init__(self)

        self.__hide_frame: bool = False

    @property
    def hide_frame(self) -> str:
        """
        Get the state of the header frame.

        Returns:
            str: The set state of the header frame.
        """
        return self.__hide_frame

    @hide_frame.setter
    def hide_frame(self, hide_frame: bool) -> None:
        """
        Set the state of the header frame.

        Args:
            hide_frame (str): The state of the header frame to set.
        """
        self.__hide_frame = hide_frame
        self.notify()


header_frame_state_publisher = HeaderFrameStatePublisher()


class SimpleObserver(ABC):
    """
    Defines the Observer interface.
    """

    @abstractmethod
    def update(self, simple_publisher: SimplePublisher) -> None:
        """
        Receives updates.

        Args:
            simple_publisher (SimplePublisher): Publisher which triggered the update.
        """
