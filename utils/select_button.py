""" Defines a SelectButton class with a custom layout and functionalities.
    This button is similar to a normal button but stays selected or deselected. """

from tkinter import Widget
from typing import Any
from PIL import Image
import customtkinter as ctk
from utils.helper_functions import find_root


class SelectButton(ctk.CTkButton):
    """
    Functionality and layout of the SelectButton.
    """

    def __init__(
        self,
        master: Any,
        width: int = 140,
        height: int = 28,
        corner_radius: int | None = None,
        border_width: int | None = None,
        border_spacing: int = 2,
        bg_color: str | tuple[str, str] = "transparent",
        fg_color: str | tuple[str, str] | None = "#3E3E3E",
        fg_color_off: str | tuple[str, str] | None = "#1F6AA5",
        hover_color: str | tuple[str, str] | None = None,
        border_color: str | tuple[str, str] | None = None,
        text_color: str | tuple[str, str] | None = None,
        text_color_disabled: str | tuple[str, str] | None = None,
        background_corner_colors: tuple[str | tuple[str, str]] | None = None,
        round_width_to_even_numbers: bool = True,
        round_height_to_even_numbers: bool = True,
        text: str = "CTkButton",
        font: tuple | ctk.CTkFont | None = None,
        min_font_size: int = 2,
        textvariable: ctk.Variable | None = None,
        hover: bool = True,
        compound: str = "left",
        anchor: str = "w",
        **kwargs
    ) -> None:
        super().__init__(
            master,
            width,
            height,
            corner_radius,
            border_width,
            border_spacing,
            bg_color,
            fg_color=fg_color,
            hover_color=hover_color,
            border_color=border_color,
            text_color=text_color,
            text_color_disabled=text_color_disabled,
            background_corner_colors=background_corner_colors,
            round_width_to_even_numbers=round_width_to_even_numbers,
            round_height_to_even_numbers=round_height_to_even_numbers,
            text=text,
            font=font,
            textvariable=textvariable,
            image=ctk.CTkImage(
                light_image=Image.open("resources/Images/minus.png"),
                size=(
                    15,
                    15,
                ),
            ),
            state="OFF",
            hover=hover,
            command=self._toggle_button,
            compound=compound,
            anchor=anchor,
            **kwargs
        )

        self.root: ctk.CTk | Widget = find_root(self)
        self.fg_color: str | tuple[str, str] | None = fg_color
        self.fg_color_off: str | tuple[str, str] | None = fg_color_off
        self.text: str = text
        self.font_size: int = font.cget("size")
        self.min_font_size: int = min_font_size

    def _toggle_button(self) -> None:
        """
        Check the current state of this button and toggle it.
        """
        if self.cget("state") == "OFF":
            self.configure(
                image=ctk.CTkImage(
                    light_image=Image.open("resources/Images/plus.png"),
                    size=(
                        15,
                        15,
                    ),
                )
            )
            self.configure(fg_color=self.fg_color_off)
            self.configure(state="ON")
        else:
            self.configure(
                image=ctk.CTkImage(
                    light_image=Image.open("resources/Images/minus.png"),
                    size=(
                        15,
                        15,
                    ),
                )
            )
            self.configure(fg_color=self.fg_color)
            self.configure(state="OFF")

    def _adjust_font_size(self) -> None:
        """
        Trigger the event of toggling the sidebar.
        """
        button_width: int = self.winfo_width()
        new_font_size: int = max(
            self.min_font_size,
            min(int((button_width / len(self.text)) * 1.5), self.font_size),
        )
        self.configure(font=ctk.CTkFont(size=new_font_size))

    def configure(self, require_redraw=False, **kwargs) -> None:
        if "text" in kwargs:
            self.text = kwargs["text"]
            self.update_idletasks()
            self.root.after(35, self._adjust_font_size)
        super().configure(require_redraw, **kwargs)


if __name__ == "__main__":
    root = ctk.CTk()
    ctk.set_appearance_mode("Dark")
    frame = ctk.CTkFrame(root)
    select_button = SelectButton(
        frame,
        text="test",
        font=ctk.CTkFont(family="Kento", size=12, weight="bold"),
        anchor="w",
        fg_color="#3E3E3E",
        fg_color_off="#1F6AA5",
    )
    frame.pack()
    select_button.pack()
    root.mainloop()
