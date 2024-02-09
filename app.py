"""Entry point of the application."""

import sys
import customtkinter as ctk
from views.configurations_view import Config
from controllers.main_controller import MainController


class AppView(ctk.CTk):
    """
    Layout of the main application.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title(Config.Titles.APP_WINDOW_TITLE)
        self.iconbitmap(Config.Images.MAIN_WINDOW_ICON)
        self.geometry(
            f"{Config.Dimensions.APP_WINDOW_WIDTH}x{Config.Dimensions.APP_WINDOW_HEIGHT}+{int(self.winfo_screenwidth() / 2 - Config.Dimensions.APP_WINDOW_WIDTH / 2)}+{int(self.winfo_screenheight() / 2 - Config.Dimensions.APP_WINDOW_HEIGHT / 2)}"
        )
        self.minsize(
            Config.Dimensions.APP_WINDOW_MIN_WIDTH,
            Config.Dimensions.APP_WINDOW_MIN_HEIGHT,
        )


class AppController:
    """
    Functionality of the main application.
    """

    def __init__(self, view=None) -> None:
        self.view = view

        # accessibility events
        self.view.bind("<Escape>", self.close_application)
        self.view.protocol("WM_DELETE_WINDOW", self.close_application)

    def close_application(self, _=None):
        """
        Close the application.
        """
        self.view.destroy()
        sys.exit(0)


def main():
    """
    Sets up the main window and event loop.
    """
    ctk.set_appearance_mode("Dark")

    app_view = AppView()
    app = AppController(app_view)
    MainController(app.view)
    app.view.mainloop()


if __name__ == "__main__":
    main()
