"""Defines the HeaderListController class with the header list functionality."""

from collections import defaultdict
import customtkinter as ctk
from configurations.header_list_config import HeaderListConfig
from views.sidebar_views.header_list_view import HeaderListView
from views.configurations_view import HeaderListFrameConfig
from models.yaml_manager import YAMLManager
from models.csv_data_manager import csv_data_manager
from utils.observer_publisher import (
    SimpleObserver,
    SimplePublisher,
    file_state_publisher,
    new_settings_publisher,
)

# from utils.scrollable_frame_manager import ScrollableFrameManager
from utils.select_button import SelectButton
from utils.threads import safe_thread_queue


class HeaderListController(SimpleObserver):
    """
    Functionality of the header list.
    """

    __slots__ = (
        "view",
        "settings_manager",
        # "scrollable_frame_filled",
        # "scrollable_frame_manager",
        "header_list",
        "header_separator",
    )

    def __init__(self, view: HeaderListView) -> None:
        self.view: HeaderListView = view

        self.label_widgets: dict[str, ctk.CTkLabel] = {}
        self.button_widgets: defaultdict[str, list[SelectButton]] = defaultdict(list)

        self.header_list: defaultdict[str, list[int] | list[tuple[str, int]]] = (
            defaultdict(list)
        )
        self.header_separator: str = ""

        self.settings_manager = YAMLManager(HeaderListConfig.OwnArgs.USER_SETTINGS)

        self.create_initial_widget_pool()

        file_state_publisher.attach(self)
        new_settings_publisher.attach(self)

        # self.scrollable_frame_filled: bool = False

        # self.scrollable_frame_manager: ScrollableFrameManager = ScrollableFrameManager(
        #     self.view.header_scrollableframe, 20, 10
        # )

    def create_initial_widget_pool(self) -> None:
        """
        Creates an initial pool of labels and buttons to be reused in the header_scrollableframe.
        """
        for group_nr in range(HeaderListConfig.OwnArgs.INITIAL_NR_OF_GROUPS):
            group_key: str = f"group_{group_nr}"

            self.label_widgets[group_key] = (
                self.view.add_label_to_header_scrollableframe()
            )

            self.button_widgets[group_key] = [
                self.view.add_button_to_header_scrollableframe()
                for _ in range(HeaderListConfig.OwnArgs.INITIAL_NR_OF_BUTTONS_PER_GROUP)
            ]

    def update(self, simple_publisher: SimplePublisher) -> None:
        if (
            simple_publisher == file_state_publisher
            and file_state_publisher.is_open is True
        ):  # A CSV file got successfully opened
            header_list: defaultdict[str, list[int] | list[tuple[str, int]]] = (
                self.get_header_list()
            )

            if header_list != self.header_list:  # The file has new values
                self.header_list = header_list
                self.start_update_header_scrollableframe_thread()

        # if (
        #     simple_publisher == file_size_publisher
        #     and file_size_publisher.file_size is not None
        # ):
        #     if self.scrollable_frame_filled is False:
        #         self.scrollable_frame_filled = True

        #     header_list = self.get_header_list()
        #     if dict(header_list) != dict(self.header_list):
        #         self.header_list = header_list
        #         self.re_create_header_list()
        #     new_settings_publisher.new_settings_saved = False
        # elif (
        #     simple_publisher == new_settings_publisher
        #     and new_settings_publisher.new_settings_saved is True
        # ):
        #     if self.scrollable_frame_filled is True:
        #         header_list = self.get_header_list()
        #         if dict(header_list) != dict(self.header_list):
        #             self.header_list = header_list
        #             self.re_create_header_list()
        #         new_settings_publisher.new_settings_saved = False

    def get_header_list(self) -> defaultdict[str, list[int] | list[tuple[str, int]]]:
        """
        Get the classified headers from a CSV file based on the user selected header structure from a csv file.

        Returns:
            defaultdict[str, list[int] | list[tuple[str, int]]]: The classified header list.
        """
        header_structure_settings: dict[str, str | None] = (
            self.settings_manager.open_file()["General"]["Header structure"]
        )

        header_prefix: str | None = header_structure_settings["first_header_prefix"]
        first_header_option: str | None = header_structure_settings[
            "first_header_option"
        ]
        first_header_postfix: str | None = header_structure_settings[
            "first_header_postfix"
        ]
        second_header_prefix: str | None = header_structure_settings[
            "second_header_prefix"
        ]
        second_header_option: str | None = header_structure_settings[
            "second_header_option"
        ]
        header_postfix: str | None = header_structure_settings["second_header_postfix"]

        self.header_separator = ""
        header_structure_order: bool = True

        # first_header_option: N/A and second_header_option : N/A
        if (
            first_header_option
            != HeaderListFrameConfig.Values.HEADER_STRUCTURE_OPTIONS[-1]
            and second_header_option
            != HeaderListFrameConfig.Values.HEADER_STRUCTURE_OPTIONS[-1]
        ):
            # Get the separator between the header and sub-header
            self.header_separator = (
                first_header_postfix if first_header_postfix else ""
            ) + (second_header_prefix if second_header_prefix else "")

            # Get the order which comes first, header or sub-header
            header_structure_order = (
                first_header_option
                == HeaderListFrameConfig.Values.HEADER_STRUCTURE_OPTIONS[0]
            )
        # Only first_header_option: N/A
        elif (
            first_header_option
            != HeaderListFrameConfig.Values.HEADER_STRUCTURE_OPTIONS[-1]
        ):
            header_postfix = first_header_postfix
        # Only second_header_option: N/A
        else:
            header_prefix = second_header_prefix

        # Get the list of headers and sub-headers without the time column, pre-, postfix and the separator
        return csv_data_manager.get_classified_headers(
            0,
            header_prefix,
            header_postfix,
            self.header_separator,
            header_structure_order,
        )

    def start_update_header_scrollableframe_thread(self) -> None:
        """
        Start the thread to update the widgets in the header_scrollableframe.
        """
        # Reset the parent canvas view to the top
        # pylint: disable=W0212
        self.view.header_scrollableframe._parent_canvas.yview_moveto(0)
        safe_thread_queue.add_task(self.manage_widgets_in_header_scrollableframe)

    def manage_widgets_in_header_scrollableframe(self) -> None:
        if self.header_separator == "":
            self.manage_widgets_for_headers_only()
        else:
            self.manage_widgets_for_headers_and_sub_headers()

    def manage_widgets_for_headers_only(self) -> None:
        """
        Distributes the headers across the button groups to ensure an even and balanced layout.

        This function dynamically adjusts the number of button groups and the number of buttons
        within each group based on the total number of headers. If there are more headers than
        the current button groups can accommodate, additional groups or buttons are added as needed.
        Unused buttons in each group are hidden.
        """
        headers = list(self.header_list.keys())

        # 1. Calculate the required number of groups based on the total number of headers
        total_nr_header: int = len(headers)
        required_groups: int = (
            total_nr_header + HeaderListConfig.OwnArgs.MAX_BUTTONS_PER_GROUP - 1
        ) // HeaderListConfig.OwnArgs.MAX_BUTTONS_PER_GROUP

        # 2. Dynamically add extra groups if the existing ones are insufficient
        total_nr_of_groups: int = len(self.button_widgets)
        for extra_group_index in range(total_nr_of_groups, required_groups):
            self.button_widgets[f"group_{extra_group_index}"] = [
                self.view.add_button_to_header_scrollableframe()
                for _ in range(HeaderListConfig.OwnArgs.INITIAL_NR_OF_BUTTONS_PER_GROUP)
            ]  # Add a group of buttons

        # 3. Calculate buttons per group after adjustments
        button_groups = list(self.button_widgets.values())
        total_nr_of_groups = len(button_groups)
        buttons_per_group: int = (
            total_nr_header + total_nr_of_groups - 1
        ) // total_nr_of_groups

        # 4. Adjust each button group with headers
        header_count: int = 0  # Track string index
        for button_group in button_groups:

            # Determine the number of buttons needed or already are in this group
            nr_of_buttons: int = max(buttons_per_group, len(button_group))

            for button_index in range(nr_of_buttons):
                # Only set the button if there are still buttons in the group and headers left
                if button_index < buttons_per_group and header_count < total_nr_header:
                    header: str = headers[header_count]
                    self.manage_buttons_in_header_scrollableframe(
                        button_group,
                        len(button_group),
                        button_index,
                        header_count,
                        header,
                    )
                    header_count += 1
                else:  # Hide any extra buttons that are not needed
                    try:
                        button_group[button_index].grid_forget()
                    except IndexError:
                        button_group.append(
                            self.view.add_button_to_header_scrollableframe()
                        )

    def manage_buttons_in_header_scrollableframe(
        self,
        group_of_buttons: list[SelectButton],
        len_group_of_buttons: int,
        button_index: int,
        row_index: int,
        text: str,
    ) -> None:
        """
        Updates the text and position of an existing button or creates a new one
        if it doesn't exist and positions it.

        Args:
            group_of_buttons (list[SelectButton]): The group of buttons.
            len_group_of_buttons (int): Number of groups of buttons.
            button_index (int): The index of the button in group.
            row_index (int): The index of the button in the scrollable frame.
            text (str): The text of the button.
        """
        if button_index < len_group_of_buttons:
            button: SelectButton = group_of_buttons[button_index]
        else:
            button = self.view.add_button_to_header_scrollableframe()
            group_of_buttons.append(button)

        self.view.manage_button(button, text, row_index)

    def manage_widgets_for_headers_and_sub_headers(self):
        pass

    def manage_label_in_header_scrollableframe(
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
        if group_key not in self.label_widgets:
            self.label_widgets[group_key] = (
                self.view.add_label_to_header_scrollableframe()
            )

        self.view.manage_label(self.label_widgets[group_key], text.upper(), label_index)

    def __del__(self) -> None:
        file_state_publisher.detach(self)
        new_settings_publisher.detach(self)
