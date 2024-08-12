"""Entry point of the application."""

import sys
from tkinter import messagebox
import customtkinter as ctk
from configurations.app_config import AppConfig
from controllers.main_controller import MainController
from views.main_view import MainView


class AppView(ctk.CTk):
    """
    Layout of the main window.
    """

    __slots__ = ("main_view",)

    def __init__(self) -> None:
        super().__init__()

        self.title(AppConfig.General.TITLE)
        self.iconbitmap(AppConfig.General.ICON)
        self.geometry(
            f"{AppConfig.Dimensions.WIDTH}x{AppConfig.Dimensions.HEIGHT}+{int(self.winfo_screenwidth() / 2 - AppConfig.Dimensions.WIDTH / 2)}+{int(self.winfo_screenheight() / 2 - AppConfig.Dimensions.HEIGHT / 2)}"
        )
        self.minsize(
            AppConfig.Dimensions.MIN_WIDTH,
            AppConfig.Dimensions.MIN_HEIGHT,
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
            side=AppConfig.Layout.MAIN_VIEW["side"],
            fill=AppConfig.Layout.MAIN_VIEW["fill"],
            expand=AppConfig.Layout.MAIN_VIEW["expand"],
        )


class AppController:
    """
    Functionality of the main window.
    """

    __slots__ = ("__view",)

    def __init__(self, view: AppView) -> None:
        self.__view: AppView = view

        self.__view.protocol("WM_DELETE_WINDOW", self.__close_application)
        self.__initialize_controller()

    def __initialize_controller(self) -> None:
        """
        Initialize controller.
        """
        MainController(self.__view.main_view)

    def __close_application(self, _=None) -> None:
        """
        Close the application.
        """
        # TODO: if messagebox.askokcancel(title="Warning", message="Close application?"):
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
