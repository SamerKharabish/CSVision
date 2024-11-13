""" Defines a ScrollableFrameManager class. """

from collections import defaultdict, OrderedDict
import customtkinter as ctk
from utils.select_button import SelectButton

# from utils.trie import Trie
from views.configurations_view import HeaderListFrameConfig
from views.configurations_view import SearchbarConfig
# from utils.observer_publisher import progress_publisher


class ScrollableFrameManager:
    """
    Class to manage widgets inside a scrollable frame and search or
    filter them based on user inputs.
    """

    __slots__ = "__root", "__label_widgets", "__button_widgets"

    def __init__(
        self,
        root: ctk.CTkScrollableFrame,
        initial_groups: int = 10,
        initial_buttons_per_group: int = 10,
    ) -> None:
        self.__root: ctk.CTkScrollableFrame = root
        self.__label_widgets: dict[str, ctk.CTkLabel] = {}
        self.__button_widgets: defaultdict[str, list[SelectButton]] = defaultdict(list)

        self.__create_initial_widget_pool(initial_groups, initial_buttons_per_group)

        # self.__search_mode: str = SearchbarConfig.Values.SEARCH_MODE_SEGMENTED_BUTTON[0]
        # self.__filter_mode: str = (
        #     HeaderListFrameConfig.Values.FILTER_MODE_SEGMENTED_BUTTON[0]
        # )
        # self.__entries: defaultdict[str, list[int] | list[tuple[str, int]]] = defaultdict(
        #     list
        # )
        # self.__display_order: OrderedDict[str:None] = OrderedDict()
        # self.__trie: Trie = Trie()

    # @property
    # def search_mode(self) -> str:
    #     """
    #     Get the current search mode.

    #     Returns:
    #         str: The set current search mode.
    #     """
    #     return self.__search_mode

    # @search_mode.setter
    # def search_mode(self, search_mode: str) -> None:
    #     """
    #     Set the current search mode.

    #     Args:
    #         search_mode (str): The current search mode to set.
    #     """
    #     self.__search_mode = search_mode

    # @property
    # def filter_mode(self) -> str:
    #     """
    #     Get the current filter mode.

    #     Returns:
    #         str: The set current filter mode.
    #     """
    #     return self.__filter_mode

    # @filter_mode.setter
    # def filter_mode(self, filter_mode: str) -> None:
    #     """
    #     Set the current filter mode.

    #     Args:
    #         filter_mode (str): The current filter mode to set.
    #     """
    #     self.__filter_mode = filter_mode

    def __create_initial_widget_pool(
        self, initial_groups: int, initial_buttons_per_group: int
    ) -> None:
        """
        Creates an initial pool of labels and buttons to be reused.

        Args:
            initial_groups (int): The initial number of group labels to create.
            initial_buttons_per_group (int): The initial number of buttons per group to create.
        """
        for i in range(initial_groups):
            group_key: str = f"group_{i}"

            self.__label_widgets[group_key] = ctk.CTkLabel(
                self.__root,
                anchor="w",
                font=ctk.CTkFont(
                    family="Kento",
                    size=12,
                    weight="bold",
                ),
            )

            self.__button_widgets[group_key] = [
                SelectButton(
                    self.__root,
                    height=25,
                    corner_radius=7,
                    font=ctk.CTkFont(
                        family="Kento",
                        size=12,
                    ),
                )
                for _ in range(initial_buttons_per_group)
            ]

    def __update_or_create_label(
        self, group_index: int, label_index: int, text: str
    ) -> None:
        """
        Updates the text and position of an existing label or creates a new one
        if it doesn't exist and positions it.

        Args:
            group_index (int): The index of the group.
            label_index (int): The index of the label in the scrollable frame.
            text (str): The text of the group label.
        """
        group_key: str = f"group_{group_index}"
        if group_key not in self.__label_widgets:
            self.__label_widgets[group_key] = ctk.CTkLabel(
                self.__root,
                anchor="w",
                font=ctk.CTkFont(
                    family="Kento",
                    size=12,
                    weight="bold",
                ),
            )

        self.__label_widgets[group_key].configure(text=text.upper())
        self.__label_widgets[group_key].grid(
            row=label_index, column=0, sticky="nesw", padx=(7, 7), pady=(1, 1)
        )

    def __update_or_create_button(
        self,
        group_of_buttons: list[SelectButton],
        len_group_of_buttons: int,
        button_index_sf: int,
        button_index_g: int,
        text: str,
    ) -> None:
        """
        Updates the text and position of an existing button or creates a new one
        if it doesn't exist and positions it.

        Args:
            group_of_buttons (list[SelectButton]): The group of buttons.
            len_group_of_buttons (int): Number of groups of buttons.
            button_index_sf (int): The index of the button in the scrollable frame.
            button_index_g (int): The index of the button in the group.
            text (str): The text of the button.
        """
        if button_index_g < len_group_of_buttons:
            button = group_of_buttons[button_index_g]
        else:
            button = SelectButton(
                self.__root,
                height=25,
                corner_radius=7,
                font=ctk.CTkFont(
                    family="Kento",
                    size=12,
                ),
            )
            group_of_buttons.append(button)

        button.configure(text=text)
        button.grid(
            row=button_index_sf,
            column=0,
            sticky="nesw",
            padx=(2, 2),
            pady=(0, 3),
        )

    def update_scrollable_frame(
        self,
        entries: defaultdict[str, list[int] | list[tuple[str, int]]],
        seperator: str = "",
        progress: int = 0,
    ) -> None:
        """
        Update the scrollable frame with new entries, either splitting them into labels
        and buttons or just using buttons.

        Args:
            entries (defaultdict[str, list[int] | list[tuple[str, int]]]): Mapped entries to display.
            seperator (str, optional): Seperator between the header and sub-header. Defaults to "".
        """
        current_row: int = 0
        len_group_of_buttons: int = 0

        entries_key_list: list[str] = list(entries.keys())
        group_of_buttons: list[SelectButton] = self.__button_widgets[f"group_{0}"]
        len_of_buttons: int = len(group_of_buttons)

        index: int = 0
        number_of_buttons: int = 0
        if seperator != "":
            # Iterate over the entries to create or update labels and buttons
            for index, (key, value) in enumerate(entries.items()):
                self.__update_or_create_label(index, current_row, key)

                current_row += 1

                group_of_buttons: list[SelectButton] = self.__button_widgets[
                    f"group_{index}"
                ]
                len_group_of_buttons = len(group_of_buttons)
                # Iterate over the values to create or update the buttons
                i: int = 0
                for i, (subheader, _) in enumerate(value):
                    self.__update_or_create_button(
                        group_of_buttons,
                        len_group_of_buttons,
                        current_row,
                        i,
                        subheader,
                    )

                    current_row += 1

                    # progress_publisher.progress = number_of_buttons * (1 / progress)
                    # progress_publisher.progress_mode = "determinate"

                    number_of_buttons += 1

                # Iterate over the rest of unused buttons in the list
                # of buttons in the same group to hide them
                len_group_of_buttons = len(group_of_buttons)
                if (i + 1) <= len_group_of_buttons:
                    for j in range((i + 1), len_group_of_buttons):
                        group_of_buttons[j].grid_forget()

            # Iterate over the rest of unused labels in the list of labels to hide them
            if (index + 1) < len(self.__label_widgets):
                for l in range((index + 1), len(self.__label_widgets)):
                    group_index: str = f"group_{l}"
                    self.__label_widgets[group_index].grid_forget()

                    # Hide all (unused) buttons of unused labels
                    for button in self.__button_widgets[group_index]:
                        button.grid_forget()
        else:
            # Iterate over the entries to create or update buttons in the first group
            for index, key in enumerate(entries_key_list):
                self.__update_or_create_button(
                    group_of_buttons, len_of_buttons, index, index, key
                )

                # progress_publisher.progress = number_of_buttons * (1 / progress)
                # progress_publisher.progress_mode = "determinate"

                number_of_buttons += 1

            # Iterate over the rest of unused buttons in the list
            # of buttons in the same group to hide them
            len_of_buttons = len(group_of_buttons)
            if (index + 1) <= len_of_buttons:
                for j in range((index + 1), len_of_buttons):
                    group_of_buttons[j].grid_forget()

            # Iterate over all labels in the list of labels to hide them
            for all_labels_index, labels in enumerate(self.__label_widgets.values()):
                labels.grid_forget()

                if all_labels_index > 0:
                    # Hide all (unused) buttons of unused labels
                    group_index: str = f"group_{all_labels_index}"
                    for button in self.__button_widgets[group_index]:
                        button.grid_forget()
