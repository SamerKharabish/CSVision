"""Entry point of the application."""

import customtkinter as ctk
from views.configurations_view import Config


def main():
    """
    Sets up the main window and event loop.
    """
    ctk.set_appearance_mode("Dark")
    root = ctk.CTk()
    root.title(Config.Titles.MAIN_WINDOW_TITLE)
    root.iconbitmap(Config.Images.MAIN_WINDOW_ICON)
    root.geometry(
        f"{Config.Dimensions.MAIN_WINDOW_WIDTH}x{Config.Dimensions.MAIN_WINDOW_HEIGHT}+{int(root.winfo_screenwidth() / 2 - Config.Dimensions.MAIN_WINDOW_WIDTH / 2)}+{int(root.winfo_screenheight() / 2 - Config.Dimensions.MAIN_WINDOW_HEIGHT / 2)}"
    )
    root.minsize(Config.Dimensions.MAIN_WINDOW_MIN_WIDTH, Config.Dimensions.MAIN_WINDOW_MIN_HEIGHT)

    root.mainloop()


if __name__ == "__main__":
    main()
