""" Defines the MainController class with the main functionality. """
from views.main_view import MainView


class MainController:
    """
    Functionality of the main application.
    """

    def __init__(self, master=None) -> None:
        self.view = MainView(master)
