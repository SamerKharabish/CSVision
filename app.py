"""Entry point of the application."""

import sys
import customtkinter as ctk
from views.configurations_view import Config
from controllers.main_controller import MainController


def main():
    """
    Sets up the main window and event loop.
    """
    ctk.set_appearance_mode("Dark")
    root = ctk.CTk()

    def close_application(_=None):
        """
        Close the application.
        """
        root.destroy()
        sys.exit(0)

    # security events
    root.bind("<Escape>", close_application)
    root.protocol("WM_DELETE_WINDOW", close_application)

    root.title(Config.Titles.MAIN_WINDOW_TITLE)
    root.iconbitmap(Config.Images.MAIN_WINDOW_ICON)
    root.geometry(
        f"{Config.Dimensions.MAIN_WINDOW_WIDTH}x{Config.Dimensions.MAIN_WINDOW_HEIGHT}+{int(root.winfo_screenwidth() / 2 - Config.Dimensions.MAIN_WINDOW_WIDTH / 2)}+{int(root.winfo_screenheight() / 2 - Config.Dimensions.MAIN_WINDOW_HEIGHT / 2)}"
    )
    root.minsize(
        Config.Dimensions.MAIN_WINDOW_MIN_WIDTH,
        Config.Dimensions.MAIN_WINDOW_MIN_HEIGHT,
    )

    MainController(root)

    root.mainloop()


if __name__ == "__main__":
    main()
