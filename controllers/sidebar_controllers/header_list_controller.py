"""Defines the HeaderListController class with the header list functionality."""

from collections import defaultdict
from views.sidebar_views.header_list_view import HeaderListView
from views.configurations_view import HeaderListFrameConfig
from models.yaml_manager import YAMLManager
from models.csv_data_manager import csv_data_manager
from utils.observer_publisher import (
    SimpleObserver,
    SimplePublisher,
    file_size_publisher,
    new_settings_publisher,
)
from utils.scrollable_frame_manager import ScrollableFrameManager
from utils.threads import UpdateWidgetThread


class HeaderListController(SimpleObserver):
    """
    Functionality of the header list.
    """

    __slots__ = (
        "view",
        "settings_manager",
        "scrollable_frame_filled",
        "scrollable_frame_manager",
        "header_list",
        "header_separator",
    )

    def __init__(self, view: HeaderListView) -> None:
        self.view: HeaderListView = view

        self.settings_manager = YAMLManager(
            HeaderListFrameConfig.General.USER_SETTINGS_YAML
        )

        file_size_publisher.attach(self)
        new_settings_publisher.attach(self)

        self.scrollable_frame_filled: bool = False

        self.scrollable_frame_manager: ScrollableFrameManager = ScrollableFrameManager(
            self.view.header_scrollableframe, 20, 10
        )
        self.header_list: defaultdict[str, list[int] | list[tuple[str, int]]] = (
            defaultdict(list)
        )
        self.header_separator: str = ""

    def update(self, simple_publisher: SimplePublisher) -> None:
        pass
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

    def re_create_header_list(self) -> None:
        """
        (Re-)create the widgets inside a scrollable frame.
        """
        # Reset the parent canvas view to the top
        # pylint: disable=W0212
        self.view.header_scrollableframe._parent_canvas.yview_moveto(0)

        update_scrollable_frame_thread = UpdateWidgetThread(
            self.scrollable_frame_manager,
            self.header_list,
            self.header_separator,
        )
        update_scrollable_frame_thread.start()

    def get_header_list(self) -> defaultdict[str, list[int] | list[tuple[str, int]]]:
        """
        Get the header list from a csv file.
        """
        header_list: defaultdict[str, list[int] | list[tuple[str, int]]] = defaultdict(
            list
        )

        header_structure_settings = self.settings_manager.open_file()["General"][
            "Header structure"
        ]
        first_header_prefix = header_structure_settings["first_header_prefix"]
        first_header_option = header_structure_settings["first_header_option"]
        first_header_postfix = header_structure_settings["first_header_postfix"]
        second_header_prefix = header_structure_settings["second_header_prefix"]
        second_header_option = header_structure_settings["second_header_option"]
        second_header_postfix = header_structure_settings["second_header_postfix"]

        if (
            first_header_option
            != HeaderListFrameConfig.Values.HEADERSTRUCTURE_OPTIONS[-1]
            and second_header_option
            != HeaderListFrameConfig.Values.HEADERSTRUCTURE_OPTIONS[-1]
        ):
            # Get the seperator between the header and sub-header
            self.header_separator = (
                first_header_postfix if first_header_postfix else ""
            ) + (second_header_prefix if second_header_prefix else "")
            # Get the order which comes first, header or sub-header
            header_structure_order = (
                False
                if first_header_option
                == HeaderListFrameConfig.Values.HEADERSTRUCTURE_OPTIONS[0]
                else True
            )
            # Get the list of headers and subheaders without the time column, pre-, postix and the seperator
            header_list = csv_data_manager.get_classified_headers(
                0,
                first_header_prefix,
                second_header_postfix,
                self.header_separator,
                header_structure_order,
            )
        elif (
            first_header_option
            != HeaderListFrameConfig.Values.HEADERSTRUCTURE_OPTIONS[-1]
        ):
            self.header_separator = ""
            # Get the list of headers and subheaders without the time column, pre-, postix and the seperator
            header_list = csv_data_manager.get_classified_headers(
                0,
                first_header_prefix,
                first_header_postfix,
            )
        else:
            self.header_separator = ""
            # Get the list of headers and subheaders without the time column, pre-, postix and the seperator
            header_list = csv_data_manager.get_classified_headers(
                0,
                second_header_prefix,
                second_header_postfix,
            )

        return header_list

    def __del__(self) -> None:
        file_size_publisher.detach(self)
        new_settings_publisher.detach(self)
