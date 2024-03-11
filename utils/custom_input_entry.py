""" Defines a CustomInputEntry class with a custom layout and functionalities. """

from typing import Any, Tuple, List
import customtkinter as ctk
from utils.helper_functions import find_root, calculate_absolute_position
from functools import partial


class CustomInputEntry(ctk.CTkEntry):
    """
    Functionality and layout of the CustomInputEntry.
    """

    def __init__(
        self,
        master: Any,
        width: int = 140,
        height: int = 28,
        corner_radius: int | None = None,
        border_width: int | None = None,
        bg_color: str | Tuple[str, str] = "transparent",
        fg_color: str | Tuple[str, str] | None = None,
        border_color: str | Tuple[str, str] | None = None,
        text_color: str | Tuple[str, str] | None = None,
        placeholder_text_color: str | Tuple[str, str] | None = None,
        textvariable: ctk.Variable | None = None,
        placeholder_text: str | None = None,
        font: tuple | ctk.CTkFont | None = None,
        state: str = ctk.NORMAL,
        **kwargs,
    ):
        super().__init__(
            master,
            width,
            height,
            corner_radius,
            border_width,
            bg_color,
            fg_color,
            border_color,
            text_color,
            placeholder_text_color,
            textvariable,
            placeholder_text,
            font,
            state,
            **kwargs,
        )

        self.corner_radius: int = corner_radius
        self.border_width: int | None = border_width
        self.border_color: str | Tuple[str, str] | None = border_color
        self.font: tuple | ctk.CTkFont | None = font
        self.fg_color: str | Tuple[str, str] | None = fg_color

        self.root = find_root(self)
        self.file_option_window: ctk.CTkToplevel = None

        self.setup_bindings()

    def setup_bindings(self) -> None:
        """
        Binding the AppController widgets to accessibility callback functions.
        """
        self.bind(
            "<Button-1>", lambda _: self.root.after(10, self.on_file_option_window)
        )

    def on_file_option_window(self, _: None = None) -> None:
        """
        Creates and positions a file option window relative to the action button.
        """
        # Calculate the entries's absolute position
        entry_x, entry_y = calculate_absolute_position(self)

        # Calculate the new window's position
        new_window_x = self.root.winfo_rootx() + entry_x
        new_window_y = self.root.winfo_rooty() + entry_y + self.winfo_height() + 2

        self.file_option_window = FileOptionWindow(
            fg_color=self.fg_color,
            corner_radius=self.corner_radius,
            border_width=self.border_width,
            border_color=self.border_color,
            width=self.winfo_width(),
            height=2 * self.winfo_height(),
            x=new_window_x,
            y=new_window_y,
            file_list=["test", "test2"],
            font=self.font,
        )


class FileOptionWindow(ctk.CTkToplevel):
    """
    Functionality and layout of a file option window.
    """

    def __init__(
        self,
        *args,
        fg_color: str | Tuple[str, str] | None = None,
        corner_radius: int | None = None,
        border_width: int | None = None,
        border_color: str | Tuple[str, str] | None = None,
        width: int = 140,
        height: int = 28,
        x: int = 0,
        y: int = 0,
        font: tuple | ctk.CTkFont | None = None,
        file_list: List[str] = None,
        **kwargs,
    ):
        super().__init__(*args, fg_color=fg_color, **kwargs)

        self.fg_color: str | Tuple[str, str] | None = fg_color
        self.corner_radius: int = corner_radius
        self.border_width: int | None = border_width
        self.border_color: str | Tuple[str, str] | None = border_color
        self.font: tuple | ctk.CTkFont | None = font
        self.file_list: List[str] = file_list

        self.buttons: List[ctk.CTkButton] = []
        self.pad: int = 2

        self.geometry(f"{width}x{height+(2 * self.pad * 2)}+{x}+{y}")
        self.overrideredirect(True)
        self.after(10, self.focus_force)

        self._initialize_widgets()
        self._create_layout()
        self._setup_bindings()

    def _initialize_widgets(self) -> None:
        """
        Initialize widgets.
        """
        self.file_option_frame = ctk.CTkFrame(
            self,
            corner_radius=self.corner_radius,
            border_width=self.border_width,
            border_color=self.border_color,
            fg_color=self.fg_color,
        )

        for file in self.file_list:
            button = ctk.CTkButton(
                self.file_option_frame,
                corner_radius=self.corner_radius,
                fg_color=self.fg_color,
                hover_color=self.fg_color,
                text=file,
                font=self.font,
                anchor="w",
            )

            button.bind("<Enter>", partial(self.on_enter, button))
            button.bind("<Leave>", partial(self.on_leave, button))

            self.buttons.append(
                button
            )

    def _create_layout(self) -> None:
        """
        Create layout.
        """
        self.file_option_frame.pack(
            fill="both",
            expand=True,
        )

        for button in self.buttons:
            button.pack(
                side="top",
                fill="both",
                expand=True,
                padx=(self.pad, self.pad),
                pady=(self.pad, self.pad),
            )

    def _setup_bindings(self) -> None:
        """
        Binding the FileOptionWindow window to accessibility callback functions.
        """
        self.bind("<FocusOut>", self._on_focus_out)

    def _on_focus_out(self, _: None = None) -> None:
        """
        Destroy the window.
        """
        self.destroy()

    def on_enter(self, button, _):
        button.configure(text_color="#9DA2A9")

    def on_leave(self, button, _):
        button.configure(text_color="#DCE4EE")
