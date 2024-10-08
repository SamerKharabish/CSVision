""" Defines a InputEntryList class with a custom layout and functionalities. """

from typing import Callable
from functools import partial
import customtkinter as ctk
from utils.helper_functions import find_root, calculate_absolute_position
from models.yaml_manager import YAMLManager


class InputEntryList(ctk.CTkEntry):
    """
    Functionality and layout of the InputEntryList.
    """

    def __init__(
        self,
        master: any,
        selected_file_path: ctk.StringVar,
        collection_filepath_yaml: str,
        width: int = 140,
        height: int = 28,
        corner_radius: int | None = None,
        border_width: int | None = None,
        bg_color: str | tuple[str, str] = "transparent",
        fg_color: str | tuple[str, str] | None = None,
        border_color: str | tuple[str, str] | None = None,
        text_color: str | tuple[str, str] | None = None,
        placeholder_text_color: str | tuple[str, str] | None = None,
        textvariable: ctk.Variable | None = None,
        placeholder_text: str | None = None,
        font: tuple | ctk.CTkFont | None = None,
        state: str = "readonly",
        max_elements: int = 4,
    ) -> None:
        super().__init__(
            master=master,
            width=width,
            height=height,
            corner_radius=corner_radius,
            border_width=border_width,
            bg_color=bg_color,
            fg_color=fg_color,
            border_color=border_color,
            text_color=text_color,
            placeholder_text_color=placeholder_text_color,
            textvariable=textvariable,
            placeholder_text=placeholder_text,
            font=font,
            state=state,
        )

        self.corner_radius: int | None = corner_radius
        self.border_width: int | None = border_width
        self.fg_color: str | tuple[str, str] | None = fg_color
        self.border_color: str | tuple[str, str] | None = border_color
        self.font: tuple | ctk.CTkFont | None = font
        self.max_elements: int = max_elements
        self.selected_file_path: ctk.StringVar = selected_file_path

        self.root = find_root(self)
        self.file_option_window: ctk.CTkToplevel

        self.file_manager = YAMLManager(collection_filepath_yaml, 10)

        self.setup_bindings()

    def setup_bindings(self) -> None:
        """
        Binding the CustomInputEntry widgets to callback functions.
        """
        self.bind(
            "<Button-1>", lambda _: self.root.after(10, self.on_file_option_window)
        )

    def on_file_option_window(self, _: None = None) -> None:
        """
        Creates and positions a file option window relative to this CustomInputEntry.
        """
        if self.cget("state") == "normal" or self.cget("state") == "readonly":
            self.configure(state="readonly")
            file_dict = self.file_manager.open_file()
            newest_files = list(file_dict.values())[-self.max_elements :]

            nr_files = (
                self.max_elements
                if self.max_elements < len(newest_files)
                else len(newest_files)
            )

            # Calculate the entries's absolute position
            entry_x, entry_y = calculate_absolute_position(self)

            # Calculate the new window's position
            new_window_x = self.root.winfo_rootx() + entry_x
            new_window_y = self.root.winfo_rooty() + entry_y + self.winfo_height() + 2

            self.file_option_window = FileOptionWindow(
                width=self.winfo_width(),
                height=nr_files * self.winfo_height(),
                x=new_window_x,
                y=new_window_y,
                corner_radius=self.corner_radius,
                border_width=self.border_width,
                fg_color=self.fg_color,
                border_color=self.border_color,
                font=self.font,
                file_list=newest_files,
                callback=self.enter_file,
            )

    def enter_file(self, filepath: str) -> None:
        """
        Update the selected file path and the entry text.

        Args:
            filepath (str): Selected file path.
        """
        self.selected_file_path.set(filepath)
        super().configure(False, state="normal")
        self.delete(0, ctk.END)
        self.insert(0, filepath.rsplit("/", 1)[1])
        self.configure(state="readonly")

    def configure(self, require_redraw=False, **kwargs):
        if "state" in kwargs and kwargs["state"] == "normal":
            return super().configure(False, state="readonly")
        else:
            return super().configure(require_redraw, **kwargs)


class FileOptionWindow(ctk.CTkToplevel):
    """
    Functionality and layout of a file option window.
    """

    BUTTON_HOVER_COLOR = "#9DA2A9"
    BUTTON_PAD: int = 2

    def __init__(
        self,
        file_list: list[str],
        callback: Callable[[str], None],
        width: int = 140,
        height: int = 28,
        x: int = 0,
        y: int = 0,
        corner_radius: int | None = None,
        border_width: int | None = None,
        fg_color: str | tuple[str, str] | None = None,
        border_color: str | tuple[str, str] | None = None,
        font: tuple | ctk.CTkFont | None = None,
    ) -> None:
        super().__init__(fg_color=fg_color)

        self.corner_radius: int | None = corner_radius
        self.border_width: int | None = border_width
        self.fg_color: str | tuple[str, str] | None = fg_color
        self.border_color: str | tuple[str, str] | None = border_color
        self.font: tuple | ctk.CTkFont | None = font
        self.file_list: list[str] = file_list
        self.callback = callback

        self.buttons: list[ctk.CTkButton] = []
        self.button_color: str | None = None

        self.geometry(
            f"{width}x{height+(len(file_list * self.BUTTON_PAD * 2))}+{x}+{y}"
        )
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
                text=file.rsplit("/", 1)[1],
                font=self.font,
                anchor="w",
                command=partial(self.file_entered, file),
            )

            button.bind("<Enter>", partial(self.on_enter, button))
            button.bind("<Leave>", partial(self.on_leave, button))

            self.buttons.append(button)

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
                padx=(self.BUTTON_PAD, self.BUTTON_PAD),
                pady=(self.BUTTON_PAD, self.BUTTON_PAD),
            )

    def _setup_bindings(self) -> None:
        """
        Binding the FileOptionWindow window to a callback function.
        """
        self.bind("<FocusOut>", self._on_focus_out)

    def _on_focus_out(self, _=None) -> None:
        """
        Destroy the window.
        """
        self.destroy()

    def on_enter(self, button: ctk.CTkButton, _=None) -> None:
        """
        Changes the button text color to indicate hovering over it.

        Args:
            button (ctk.CTkButton): The button which text color to change.
            _ (None, optional): The event. Defaults to None.
        """
        self.button_color = button.cget("text_color")
        button.configure(text_color=self.BUTTON_HOVER_COLOR)

    def on_leave(self, button: ctk.CTkButton, _=None) -> None:
        """
        Changes the button text color to to turn back after it got hovered over.

        Args:
            button (ctk.CTkButton): The button which text color to change.
            _ (None, optional): The event. Defaults to None.
        """
        button.configure(text_color=self.button_color)

    def file_entered(self, file: str) -> None:
        """
        Call a callback function and destroy the window.

        Args:
            file (str): A selected file path.
        """
        self.callback(file)
        self.destroy()
