""" Defines all subscriptable subject classes. """

from __future__ import annotations
from abc import ABC, abstractmethod


class SimplePublisher:
    """
    Represents csv data that is being observed.
    """

    def __init__(self):
        """
        Create an empty observer list.
        """
        self._observers: list[SimpleObserver] = []

    def attach(self, observer: SimpleObserver):
        """
        Attach an observer to the list if not already attached.

        Args:
            observer (SimpleObserver): Observer to be attached.
        """
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: SimpleObserver):
        """
        Detach an observer from the list if attached.

        Args:
            observer (SimpleObserver): Observer to be dettached.
        """
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, modifier: SimpleObserver | None = None):
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
        Receives updates from the CSVManager. Called when the CSVManager's state changes.

        Args:
            simple_publisher (SimplePublisher): Publisher to be attached to.
        """
