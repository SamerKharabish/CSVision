"""Defines all subscriptable publisher classes and the observer interface."""

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
            observer (SimpleObserver): Observer to be detached.
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


class SidebarStatePublisher(SimplePublisher):
    """
    Monitor the visibility of the sidebar.
    """

    __slots__ = ("visible",)

    def __init__(self) -> None:
        SimplePublisher.__init__(self)

        self.visible: bool = True

    def get_visibility(self) -> bool:
        """
        Get the visibility of the sidebar.

        Returns:
            bool: The visibility of the sidebar.
        """
        return self.visible

    def toggle_sidebar_visibility(self, modifier: SimpleObserver | None = None) -> None:
        """
        Toggle the visibility of the sidebar and notify all observer.

        Args:
            modifier (SimpleObserver | None, optional): Observer that triggered the update. Defaults to None.
        """
        self.visible = not self.visible
        self.notify(modifier)


sidebar_state_publisher = SidebarStatePublisher()


class ProgressStatePublisher(SimplePublisher):
    """
    Monitor the progress of the data loading thread.
    """

    START_PROGRESSBAR: float = 0.0
    STOP_PROGRESSBAR: float = 100.0

    __slots__ = "_mode", "_value"

    def __init__(self) -> None:
        SimplePublisher.__init__(self)

        self._mode: str = "indeterminate"
        self._value: float = 0.0

    @property
    def mode(self) -> str:
        """
        Get the mode of the progressbar.

        Returns:
            str: The mode of the progressbar.
        """
        return self._mode

    @mode.setter
    def mode(self, mode: str = "determinate") -> None:
        """
        Set the mode of the progressbar.

        Args:
            mode (str, optional): The mode of the progressbar to set. Defaults to determinate.
        """
        self._mode = mode

    @property
    def value(self) -> float:
        """
        Get the value of the progressbar.

        Returns:
            float: The value of the progressbar.
        """
        return self._value

    @value.setter
    def value(self, value: float = 0.0, modifier: SimpleObserver | None = None) -> None:
        """
        Set the value of the progressbar.

        Args:
            value (float, optional): The value of the progressbar to set. Defaults to 0.0.
            modifier (SimpleObserver | None, optional): Observer that triggered the update. Defaults to None.
        """
        self._value = value
        self.notify(modifier)


progress_state_publisher = ProgressStatePublisher()


class FileStatePublisher(SimplePublisher):
    """
    Monitor the file size.
    """

    __slots__ = ("_file_size", "_is_open")

    def __init__(self) -> None:
        SimplePublisher.__init__(self)

        self._file_size: str
        self._is_open: bool = False

    @property
    def file_size(self) -> str:
        """
        Get the file size.

        Returns:
            str: The file size.
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size: str) -> None:
        """
        Set the file size.

        Args:
            file_size (str): The file size to set.
        """
        self._file_size = file_size

    @property
    def is_open(self) -> bool:
        """
        Get the file status.

        Returns:
            bool: The file status.
        """
        return self._is_open

    def set_is_open(
        self, is_open: bool, modifier: SimpleObserver | None = None
    ) -> None:
        """
        Set the file status.

        Args:
            is_open (bool): The file status to set.
            modifier (SimpleObserver | None, optional): Observer that triggered the update. Defaults to None.
        """
        self._is_open = is_open
        self.notify(modifier)

        if is_open:
            self._is_open = False


file_state_publisher = FileStatePublisher()


class NewSettingsPublisher(SimplePublisher):
    """
    Monitor if new settings were saved.
    """

    __slots__ = ("__new_settings_saved",)

    def __init__(self) -> None:
        SimplePublisher.__init__(self)

        self.__new_settings_saved: bool = False

    @property
    def new_settings_saved(self) -> bool:
        """
        Get the state of the settings.

        Returns:
            str: The set state of the settings.
        """
        return self.__new_settings_saved

    @new_settings_saved.setter
    def new_settings_saved(self, new_settings_saved: str | None) -> None:
        """
        Set the state of the settings.

        Args:
            new_settings_saved (str): The state of the settings to set.
        """
        self.__new_settings_saved = new_settings_saved
        self.notify()


new_settings_publisher = NewSettingsPublisher()
