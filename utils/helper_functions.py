""" Defines helper funtions. """

from typing import Tuple
import tkinter as tk
import customtkinter as ctk


def find_root(widget: tk.Widget) -> ctk.CTk:
    """
    Recursively traverse the widget hierarchy to find the root widget.

    Args:
        widget (tk.Widget): The widget from where to start the search.

    Returns:
        ctk.CTk: The root widget of the widget hierarchy.
    """
    parent_id = widget.winfo_parent()

    # If there is no parent, this widget is the root
    if not parent_id:
        return widget

    # Otherwise, get the actual parent widget
    parent_widget = widget.nametowidget(parent_id)

    # Recursively call this function to find the root
    return find_root(parent_widget)


def calculate_absolute_position(widget: tk.Widget) -> Tuple[int, int]:
    """
    Function to calculate the absolute position of a widget relative to the root window.

    Args:
        widget (tk.Widget): The widget from where to start the calculation.

    Returns:
        Tuple[int, int]: The absolute position of the widget.
    """
    x, y = widget.winfo_x(), widget.winfo_y()

    parent = widget.winfo_parent()
    if parent == ".":
        # Base case: the root window
        return x, y

    parent_widget = widget.nametowidget(parent)
    parent_x, parent_y = calculate_absolute_position(parent_widget)

    # The absolute position is the widget's position plus its parent's absolute position
    return x + parent_x, y + parent_y
