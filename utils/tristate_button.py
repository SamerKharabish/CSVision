""" Defines a TriStateButton class with a custom layout and functionalities.
    This button is similar to a checkbox but with three option to choose from. """

from typing import Callable
import customtkinter as ctk


class TriStateButton(ctk.CTkButton):
    """
    Functionality and layout of the TriStateButton.
    """

    def __init__(
        self,
        master: any,
        width: int = 17,
        height: int = 17,
        corner_radius: int | None = None,
        border_width: int | None = 2,
        border_spacing: int = 0,
        bg_color: str | tuple[str] = "transparent",
        fg_color: str | tuple[str] | None = None,
        hover_color: str | tuple[str] | None = None,
        border_color: str | tuple[str] | None = None,
        text_color: str | tuple[str] | None = None,
        text_color_disabled: str | tuple[str] | None = None,
        background_corner_colors: tuple[str | tuple[str]] | None = None,
        round_width_to_even_numbers: bool = True,
        round_height_to_even_numbers: bool = True,
        states: list[str] | None = None,
        font: tuple | ctk.CTkFont | None = None,
        textvariable: ctk.Variable | None = None,
        state: str = "normal",
        hover: bool = True,
        user_command: Callable[[], any] | None = None,
        compound: str = "left",
        anchor: str = "center",
    ) -> None:
        super().__init__(
            master=master,
            width=width,
            height=height,
            corner_radius=corner_radius,
            border_width=border_width,
            border_spacing=border_spacing,
            bg_color=bg_color,
            fg_color=fg_color,
            hover_color=hover_color,
            border_color=border_color,
            text_color=text_color,
            text_color_disabled=text_color_disabled,
            background_corner_colors=background_corner_colors,
            round_width_to_even_numbers=round_width_to_even_numbers,
            round_height_to_even_numbers=round_height_to_even_numbers,
            font=font,
            textvariable=textvariable,
            state=state,
            hover=hover,
            compound=compound,
            anchor=anchor,
        )

        if states:
            self.states = states
        else:
            self.states = ["L", "R", "_"]
        self.configure(text=self.states[0])
        self.current_state = 0  # Start with the first state

        if fg_color is None:
            self.configure(fg_color=master._fg_color)

        if hover_color is None:
            self.configure(hover_color=master._fg_color)

        self.user_command: Callable[[], any] | None = user_command
        self.configure(command=self.command)

    def advance_state(self) -> None:
        """Advance to the next state."""
        self.current_state = (self.current_state + 1) % len(self.states)
        self.configure(text=self.states[self.current_state])

    def command(self) -> None:
        """
        Call the advance_state method and the user's command.
        """
        self.advance_state()
        if self.user_command is not None:
            self.user_command()


if __name__ == "__main__":
    root = ctk.CTk()
    ctk.set_appearance_mode("Dark")
    frame = ctk.CTkFrame(root)
    label = ctk.CTkLabel(
        frame,
        text="test",
        font=ctk.CTkFont(family="Kento", size=12),
    )
    option_button = TriStateButton(
        frame, font=ctk.CTkFont(family="Kento", size=8, weight="bold")
    )
    frame.pack()
    label.pack(side="left")
    option_button.pack(side="right")
    root.mainloop()
