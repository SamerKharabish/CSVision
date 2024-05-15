""" Defines the NavigationFrameController class with the navigation frame functionality. """

from views.configurations_view import SettingsWindowConfig
from views.sidebar_views.settings_window_view import SettingsWindowView
from utils.helper_functions import find_root


class SettingsWindowController:
    """
    Functionality of the settings window view.
    """

    __slots__ = ("__view",)

    def __init__(self, view: SettingsWindowView) -> None:
        self.__view: SettingsWindowView = view

        self.__view.root = find_root(self.__view)

        self.__setup_bindings()

    def __setup_bindings(self) -> None:
        """
        Binding the settings window to accessibility callback functions.
        """
        self.__view.bind(
            SettingsWindowConfig.General.CLOSE_APPLICATION_KEYBIND,
            self.__close_application,
        )
        self.__view.protocol("WM_DELETE_WINDOW", self.__close_application)

        self.__view.bind(
            "<Map>",
            self.on_deiconify,
        )

    def __close_application(self, _=None) -> None:
        """
        Withdraw the settings window instead of closing it.
        """
        self.__view.withdraw()

    def on_deiconify(self, _=None) -> None:
        """
        Update geometry of the settings window when deiconifying it.
        """
        pos_x = (
            self.__view.root.winfo_x()
            + self.__view.root.winfo_width() // 2
            - SettingsWindowConfig.Dimensions.WIDTH // 2
        )
        pos_y = (
            self.__view.root.winfo_y()
            + self.__view.root.winfo_height() // 2
            - SettingsWindowConfig.Dimensions.HEIGHT // 2
        )

        self.__view.geometry(
            f"{SettingsWindowConfig.Dimensions.WIDTH}x{SettingsWindowConfig.Dimensions.HEIGHT}+{pos_x}+{pos_y}"
        )
