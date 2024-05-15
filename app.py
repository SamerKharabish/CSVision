"""Entry point of the application."""

import sys
from tkinter import messagebox
import customtkinter as ctk
from views.configurations_view import AppWindowConfig
from views.main_view import MainView
from controllers.main_controller import MainController


class AppView(ctk.CTk):
    """
    Layout of the main window.
    """

    __slots__ = ("main_view",)

    def __init__(self) -> None:
        super().__init__()

        self.title(AppWindowConfig.General.TITLE)
        self.iconbitmap(AppWindowConfig.General.ICON)
        self.geometry(
            f"{AppWindowConfig.Dimensions.WIDTH}x{AppWindowConfig.Dimensions.HEIGHT}+{int(self.winfo_screenwidth() / 2 - AppWindowConfig.Dimensions.WIDTH / 2)}+{int(self.winfo_screenheight() / 2 - AppWindowConfig.Dimensions.HEIGHT / 2)}"
        )
        self.minsize(
            AppWindowConfig.Dimensions.MIN_WIDTH,
            AppWindowConfig.Dimensions.MIN_HEIGHT,
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
            side=AppWindowConfig.Layout.MAINVIEW_SIDE,
            fill=AppWindowConfig.Layout.MAINVIEW_FILL,
            expand=AppWindowConfig.Layout.MAINVIEW_EXPAND,
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
        Binding the application to accessibility callback functions.
        """
        self.__view.bind(
            AppWindowConfig.KeyBindings.CLOSE_APPLICATION, self.__close_application
        )
        self.__view.protocol("WM_DELETE_WINDOW", self.__close_application)

    def __close_application(self, _=None) -> None:
        """
        Close the application.
        """
        if messagebox.askokcancel(title="Warning", message="Close application?"):
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
