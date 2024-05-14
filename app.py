"""Entry point of the application."""

import sys
import customtkinter as ctk
from views.configurations_view import Config
from views.main_view import MainView
from controllers.main_controller import MainController


class AppView(ctk.CTk):
    """
    Layout of the main window.
    """

    __slots__ = ("main_view",)

    def __init__(self) -> None:
        super().__init__()

        self.title(Config.WindowTitles.APP_WINDOW_TITLE)
        self.iconbitmap(Config.ImageFormats.MAIN_WINDOW_ICO)
        self.geometry(
            f"{Config.Dimensions.APP_WINDOW_WIDTH}x{Config.Dimensions.APP_WINDOW_HEIGHT}+{int(self.winfo_screenwidth() / 2 - Config.Dimensions.APP_WINDOW_WIDTH / 2)}+{int(self.winfo_screenheight() / 2 - Config.Dimensions.APP_WINDOW_HEIGHT / 2)}"
        )
        self.minsize(
            Config.Dimensions.APP_WINDOW_MIN_WIDTH,
            Config.Dimensions.APP_WINDOW_MIN_HEIGHT,
        )

        self.__initialize_widgets()
        self.__create_layout()

    def __initialize_widgets(self) -> None:
        """
        Initialize widgets.
        """
        self.main_view: MainView = MainView(self)

    def __create_layout(self) -> None:
        """
        Create layout.
        """
        self.main_view.pack(
            side=Config.Layout.MAIN_VIEW_SIDE,
            fill=Config.Layout.MAIN_VIEW_FILL,
            expand=Config.Layout.MAIN_VIEW_EXPAND,
        )


class AppController:
    """
    Functionality of the main window.
    """

    __slots__ = ("__view",)

    def __init__(self, view: AppView) -> None:
        self.__view: AppView = view

        self.__initialize_controller()
        self.__setup_bindings()

    def __initialize_controller(self) -> None:
        """
        Initialize controller.
        """
        MainController(self.__view.main_view)

    def __setup_bindings(self) -> None:
        """
        Binding the AppController widgets to accessibility callback functions.
        """
        self.__view.bind(Config.KeyBindings.CLOSE_APPLICATION, self.__close_application)
        self.__view.protocol("WM_DELETE_WINDOW", self.__close_application)

    def __close_application(self, _=None) -> None:
        """
        Close the application.
        """
        self.__view.destroy()
        sys.exit(0)


def main() -> None:
    """
    Sets up the main window and event loop.
    """
    ctk.set_appearance_mode("Dark")

    app_view = AppView()
    AppController(app_view)

    app_view.mainloop()


if __name__ == "__main__":
    main()
