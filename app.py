"""Entry point of the application."""

import sys
from tkinter import messagebox
import customtkinter as ctk
from configurations.app_config import AppConfig
from controllers.main_controller import MainController
from views.main_view import MainView
from utils.threads import safe_thread_queue


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

        self.initialize_widgets()
        self.create_layout()

    def initialize_widgets(self) -> None:
        """
        Initialize widgets.
        """
        self.main_view: MainView = MainView(self)

    def create_layout(self) -> None:
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

    __slots__ = ("view",)

    def __init__(self) -> None:
        self.view: AppView = AppView()

        self.view.protocol("WM_DELETE_WINDOW", self.close_application)
        self.initialize_controller()

    def initialize_controller(self) -> None:
        """
        Initialize controller.
        """
        MainController(self.view.main_view)

    def close_application(self, _=None) -> None:
        """
        Close the application.
        """
        # TODO: if messagebox.askokcancel(title="Warning", message="Close application?"):
        safe_thread_queue.stop_worker()
        self.view.destroy()
        sys.exit(0)

    def run(self) -> None:
        """
        Start the mainloop.
        """
        self.view.mainloop()


def main() -> None:
    """
    Sets up the main window and event loop.
    """
    ctk.set_appearance_mode("Dark")

    app_controller = AppController()
    app_controller.run()


if __name__ == "__main__":
    main()
