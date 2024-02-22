""" Defines a CustomOptionMenu class with a custom layout and the functionality from a customtkinter optionmenu. """

from typing import Tuple, Optional, Callable, List
from PIL import Image
import customtkinter as ctk
from utils.helper_functions import find_root, calculate_absolute_position
from views.configurations_view import Config


class CustomOptionMenu(ctk.CTkFrame):
    """
    Functionality and layout of the custom optionmenu.
    """

    DEFAULT_BUTTON_WIDTH: int = 20
    DEFAULT_PADX: int = 4

    def __init__(
        self,
        master: any,
        width: int = 200,
        height: int = 200,
        corner_radius: int = 4,
        border_width: int | None = None,
        border_color: str | Tuple[str, str] | None = None,
        bg_color: str | Tuple[str, str] = "transparent",
        fg_color: str | Tuple[str, str] | None = "#1F6AA5",
        hover_color: str | Tuple[str, str] | None = None,
        text_color: str | Tuple[str, str] | None = None,
        font: tuple | ctk.CTkFont | None = None,
        button_bg_color: str | Tuple[str, str] = "transparent",
        button_fg_color: str | Tuple[str, str] | None = "#1A5A8A",
        button_hover_color: str | Tuple[str, str] | None = None,
        values: list | None = None,
        anchor: str = "center",
        option_button_enable: bool = True,
        **kwargs,
    ):
        super().__init__(
            master,
            width=width,
            height=height,
            corner_radius=0,
            border_width=0,
            bg_color="transparent",
            fg_color="transparent",
            border_color=None,
            background_corner_colors=None,
            overwrite_preferred_drawing_method=None,
            **kwargs,
        )

        self.root = find_root(self)
        self.width: int = width
        self.corner_radius: int = corner_radius
        self.border_width: int | None = border_width
        self.border_color: str | Tuple[str, str] | None = border_color
        self.bg_color: str | Tuple[str, str] = bg_color
        self.fg_color: str | Tuple[str, str] | None = fg_color
        self.hover_color: str | Tuple[str, str] | None = hover_color
        self.text_color: str | Tuple[str, str] | None = text_color
        self.font: tuple | ctk.CTkFont | None = font
        self.button_bg_color: str | Tuple[str, str] = button_bg_color
        self.button_fg_color: str | Tuple[str, str] | None = button_fg_color
        self.button_hover_color: str | Tuple[str, str] | None = button_hover_color
        self.values: list | None = values
        self.anchor: str = anchor
        self.option_button_enable: bool = option_button_enable

        self.optionmenu_window: ctk.CTkToplevel = None

        self.initialize_widgets()
        self.create_layout()

    def initialize_widgets(self) -> None:
        """
        Initialize widgets.
        """
        if self.option_button_enable:
            self.option_button_width: int = self.DEFAULT_BUTTON_WIDTH
            self.padx: int = self.DEFAULT_PADX

            self.option_button = ctk.CTkButton(
                self,
                width=self.option_button_width,
                corner_radius=self.corner_radius,
                bg_color=self.button_bg_color,
                fg_color=self.button_fg_color,
                hover_color=self.button_hover_color,
                text="",
                image=ctk.CTkImage(
                    light_image=Image.open(Config.ImageFormats.DOWN_ARROW),
                    size=(
                        12,
                        12,
                    ),
                ),
                command=self.create_option_menu,
            )
        else:
            self.option_button_width: int = 0
            self.padx: int = 0

        self.action_button = ctk.CTkButton(
            self,
            width=self.width - self.option_button_width,
            corner_radius=self.corner_radius,
            border_width=self.border_width,
            bg_color=self.bg_color,
            fg_color=self.fg_color,
            hover_color=self.hover_color,
            border_color=self.border_color,
            text_color=self.text_color,
            text=self.values[0] if self.values and self.values[0] != "" else " ",
            font=self.font,
            anchor=self.anchor,
        )

    def create_layout(self) -> None:
        """
        Create layout.
        """

        self.action_button.pack(
            side="left", fill="both", expand=True, padx=(0, self.padx)
        )
        if self.option_button_enable:
            self.option_button.pack(side="left", fill="y", expand=False)

    def create_option_menu(self) -> None:
        # Calculate the button's absolute position
        btn_x, btn_y = calculate_absolute_position(self.option_button)

        # Calculate the new window's position
        new_window_x = (
            self.root.winfo_rootx()
            + btn_x
            - self.action_button.winfo_width()
            - self.padx
        )
        new_window_y = (
            self.root.winfo_rooty() + btn_y + self.option_button.winfo_height() + 2
        )

        if self.optionmenu_window is None or not self.optionmenu_window.winfo_exists():
            OptionWindow(
                fg_color=self.fg_color,
                corner_radius=self.corner_radius,
                width=self.action_button.winfo_width(),
                height=len(self.values) * self.action_button.winfo_height(),
                x=new_window_x,
                y=new_window_y,
                values=self.values,
                callbacks=None,
                font=self.font,
            )


class OptionWindow(ctk.CTkToplevel):
    """
    Functionality and layout of the optionmenu window.
    """

    def __init__(
        self,
        *args,
        fg_color: str | Tuple[str, str] | None = None,
        corner_radius: int = 4,
        width: int = 100,
        height: int = 50,
        x: int = 0,
        y: int = 0,
        values: list | None = None,
        font: tuple | ctk.CTkFont | None = None,
        callbacks: Optional[List[Callable[..., None]]] = None,
        **kwargs,
    ):
        super().__init__(*args, fg_color=fg_color, **kwargs)

        self.fg_color: str | Tuple[str, str] | None = fg_color
        self.corner_radius: int = corner_radius
        self.values: list | None = values
        self.font: tuple | ctk.CTkFont | None = font
        self.callbacks: Optional[List[Callable[..., None]]] = callbacks

        self.buttons: List[ctk.CTkButton] = []
        self.pady: int = 2

        self.geometry(f"{width}x{height+(len(values) * self.pady + self.pady)}+{x}+{y}")
        self.overrideredirect(True)
        self.after(10, self.focus_force)

        self.initialize_widgets()
        self.create_layout()
        self.setup_bindings()

    def initialize_widgets(self) -> None:
        """
        Initialize widgets.
        """
        self.option_frame = ctk.CTkFrame(
            self,
            corner_radius=self.corner_radius,
            fg_color=self.fg_color,
        )

        button_callbacks = zip(
            self.values,
            self.callbacks if self.callbacks is not None else [None] * len(self.values),
        )

        for value, callback in button_callbacks:
            self.buttons.append(
                ctk.CTkButton(
                    self.option_frame,
                    corner_radius=self.corner_radius,
                    fg_color=self.fg_color,
                    text=value,
                    font=self.font,
                    command=callback,
                )
            )

    def create_layout(self) -> None:
        """
        Create layout.
        """
        self.option_frame.pack(fill="both", expand=True)

        for button in self.buttons:
            button.pack(
                side="top",
                fill="both",
                expand=True,
                padx=(self.pady, self.pady),
                pady=(self.pady, self.pady),
            )

    def setup_bindings(self) -> None:
        """
        Binding the OptionWindow window to accessibility callback functions.
        """
        self.bind("<FocusOut>", self.on_focus_out)

    def on_focus_out(self, _: None = None) -> None:
        """
        Destroy the window.
        """
        self.destroy()


if __name__ == "__main__":
    app = ctk.CTk()
    app.geometry("300x200")

    custom_option_menu = CustomOptionMenu(app)

    custom_option_menu.pack(fill="both", expand=True, padx=(5, 5), pady=(5, 5))
    app.mainloop()
