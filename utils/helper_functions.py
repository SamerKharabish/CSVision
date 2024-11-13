""" Defines helper functions. """

import re
import tkinter as tk
import customtkinter as ctk


def find_root(widget: tk.Widget) -> ctk.CTk | tk.Widget:
    """
    Recursively traverse the widget hierarchy to find the root widget.

    Args:
        widget (tk.Widget): The widget from where to start the search.

    Returns:
        ctk.CTk: The root widget of the widget hierarchy.
    """
    parent_id: str = widget.winfo_parent()

    # If there is no parent, this widget is the root
    if not parent_id:
        return widget

    # Otherwise, get the actual parent widget
    parent_widget = widget.nametowidget(parent_id)

    # Recursively call this function to find the root
    return find_root(parent_widget)


def calculate_absolute_position(widget: tk.Widget) -> tuple[int, int]:
    """
    Function to calculate the absolute position of a widget relative to the root window.

    Args:
        widget (tk.Widget): The widget from where to start the calculation.

    Returns:
        tuple[int, int]: The absolute position of the widget.
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


def search_substring(
    header: str, prefix: str | None = None, postfix: str | None = None
) -> str:
    """
    Searches for a substring within a header based on what comes before or after the target
    substring. If `prefix` is not specified, the match will start from the beginning. If `postfix`
    is not specified, the match will end at the last character.

    Parameters:
        - header (str): The longer string in which to search for the substring.
        - prefix (str, optional): The string that comes before the target substring. Defaults to None.
        - postfix (str, optional): The string that comes after the target substring. Defaults to None.
    Returns:
        - str: The matched substring if found, otherwise the original header`.
    """
    # Build regex pattern based on the presence of 'prefix' and 'postfix'
    if prefix is None and postfix is None:
        return header

    prefix_escaped: str | None = None
    postfix_escaped: str | None = None

    # Escape inputs for regex safety
    if prefix:
        prefix_escaped = re.escape(prefix)
    if postfix:
        postfix_escaped = re.escape(postfix)

    # Try to match both prefix and postfix
    if prefix and postfix:
        pattern: str = f"{prefix_escaped}(.*?){postfix_escaped}"
        match: re.Match[str] | None = re.search(pattern, header)
        if match:
            return match.group(1)

    # Try to match prefix only
    if prefix:
        pattern = f"{prefix_escaped}(.*)"
        match = re.search(pattern, header)
        if match:
            return match.group(1)

    # Try to match postfix only
    if postfix:
        pattern = f"(.*?){postfix_escaped}"
        match = re.search(pattern, header)
        if match:
            return match.group(1)

    # If no matches, return the original header
    return header
