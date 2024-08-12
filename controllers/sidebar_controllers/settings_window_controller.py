""" Defines the NavigationFrameController class with the navigation frame functionality. """

import customtkinter as ctk
from views.configurations_view import SettingsWindowConfig
from views.configurations_view import HeaderStructureConfig
from views.sidebar_views.settings_window_view import (
    SettingsWindowView,
    HeaderStructureFrameView,
)
from utils.helper_functions import find_root
from models.yaml_manager import YAMLManager


class SettingsWindowController:
    """
    Functionality of the settings window view.
    """

    __slots__ = "__view", "__settings_manager", "__header_structure_frame_controller"

    def __init__(self, view: SettingsWindowView) -> None:
        self.__view: SettingsWindowView = view

        self.__view.root = find_root(self.__view)

        self.__settings_manager = YAMLManager(
            HeaderStructureConfig.General.USER_SETTINGS_YAML
        )

        self.__setup_bindings()
        self.__initialize_controller()

        self.__set_settings()

        self.__view.apply_button.configure(command=self.__on_apply)
        self.__view.ok_button.configure(command=self.__on_ok)
        self.__view.cancel_button.configure(command=self.__on_cancel)

    def __initialize_controller(self) -> None:
        """
        Initialize controller.
        """
        self.__header_structure_frame_controller: HeaderStructureFrameController = (
            HeaderStructureFrameController(self.__view.header_structure_frame_view)
        )

    def __setup_bindings(self) -> None:
        """
        Binding the settings window to accessibility callback functions.
        """
        self.__view.bind(
            SettingsWindowConfig.KeyBindings.CLOSE_SETTINGS,
            self.__view.withdraw,
        )
        self.__view.protocol("WM_DELETE_WINDOW", self.__view.withdraw)

    def __set_settings(self) -> None:
        """
        Set the initial settings from the YAML file.
        """
        header_structure_settings = self.__settings_manager.open_file()["General"][
            "Header structure"
        ]
        self.__header_structure_frame_controller.set_header_structure(
            header_structure_settings
        )

    def __on_apply(self) -> None:
        """
        Apply changes.
        """
        header_structure = {
            "Header structure": self.__header_structure_frame_controller.get_header_structure()
        }
        settings = {"General": header_structure}
        self.__settings_manager.dump_yaml_file(settings)

    def __on_ok(self) -> None:
        """
        Confirm and apply changes, and then withdraws the settings window.
        """
        header_structure = {
            "Header structure": self.__header_structure_frame_controller.get_header_structure()
        }
        settings = {"General": header_structure}
        self.__settings_manager.dump_yaml_file(settings)
        self.__view.withdraw()

    def __on_cancel(self) -> None:
        """
        Discard any changes and withdraws the settings window.
        """
        self.__set_settings()
        self.__view.withdraw()

    def update_settings_geometries(self) -> None:
        """
        Update geometries of the settings window.
        """
        pos_x = (
            self.__view.root.winfo_x()
            + self.__view.root.winfo_width() // 2
            - SettingsWindowConfig.Dimensions.WIDTH // 2
        )
        pos_y = (
            self.__view.root.winfo_y()
            + self.__view.root.winfo_height() // 2
            - SettingsWindowConfig.Dimensions.HEIGHT // 2
        )

        self.__view.geometry(
            f"{SettingsWindowConfig.Dimensions.WIDTH}x{SettingsWindowConfig.Dimensions.HEIGHT}+{pos_x}+{pos_y}"
        )
        self.__view.deiconify()
        self.__view.focus()


class HeaderStructureFrameController:
    """
    Functionality of the header structure frame.
    """

    __slots__ = (
        "__view",
        "__first_header_prefix_var",
        "__first_header_option_var",
        "__first_header_postfix_var",
        "__second_header_prefix_var",
        "__second_header_option_var",
        "__second_header_postfix_var",
    )

    def __init__(self, view: HeaderStructureFrameView) -> None:
        self.__view: HeaderStructureFrameView = view

        self.__first_header_prefix_var: ctk.StringVar = ctk.StringVar()
        self.__first_header_option_var: ctk.StringVar = ctk.StringVar()
        self.__first_header_postfix_var: ctk.StringVar = ctk.StringVar()

        self.__second_header_prefix_var: ctk.StringVar = ctk.StringVar()
        self.__second_header_option_var: ctk.StringVar = ctk.StringVar()
        self.__second_header_postfix_var: ctk.StringVar = ctk.StringVar()

    def set_header_structure(self, header_structure_settings: dict) -> None:
        """
        Set the header structure.

        Args:
            header_structure_settings (dict): Header structure to set.
        """
        # First header configurations
        first_header_prefix = header_structure_settings["first_header_prefix"]
        self.__first_header_prefix_var.set(
            value=first_header_prefix if first_header_prefix is not None else ""
        )
        self.__view.header_entries[0].configure(
            textvariable=self.__first_header_prefix_var
        )
        self.__first_header_prefix_var.trace_add("write", self.__header_option_callback)

        self.__first_header_option_var.set(
            value=header_structure_settings["first_header_option"]
        )
        self.__view.first_header_option.configure(
            variable=self.__first_header_option_var
        )
        self.__first_header_option_var.trace_add("write", self.__header_option_callback)

        first_header_postfix = header_structure_settings["first_header_postfix"]
        self.__first_header_postfix_var.set(
            value=first_header_postfix if first_header_postfix is not None else ""
        )
        self.__view.header_entries[1].configure(
            textvariable=self.__first_header_postfix_var
        )
        self.__first_header_postfix_var.trace_add(
            "write", self.__header_option_callback
        )

        # Second header configurations
        second_header_prefix = header_structure_settings["second_header_prefix"]
        self.__second_header_prefix_var.set(
            value=second_header_prefix if second_header_prefix is not None else ""
        )
        self.__view.header_entries[2].configure(
            textvariable=self.__second_header_prefix_var
        )
        self.__second_header_prefix_var.trace_add(
            "write", self.__header_option_callback
        )

        self.__second_header_option_var.set(
            value=header_structure_settings["second_header_option"]
        )
        self.__view.second_header_option.configure(
            variable=self.__second_header_option_var
        )
        self.__second_header_option_var.trace_add(
            "write", self.__header_option_callback
        )

        second_header_postfix = header_structure_settings["second_header_postfix"]
        self.__second_header_postfix_var.set(
            value=second_header_postfix if second_header_postfix is not None else ""
        )
        self.__view.header_entries[3].configure(
            textvariable=self.__second_header_postfix_var
        )
        self.__second_header_postfix_var.trace_add(
            "write", self.__header_option_callback
        )

        self.__header_entries_callback()

    def __header_entries_callback(self) -> tuple[str, str]:
        """
        Get the option the user selected and either diable ot enable the entries.

        Returns:
            tuple[str, str]: The user options.
        """
        first_header_option = self.__first_header_option_var.get()
        second_header_option = self.__second_header_option_var.get()

        def configure_based_on_option(indexes: str, option: str) -> None:
            """
            Configure the entries based on the user option.

            Args:
                indexes (str): Index of the header.
                option (str): The option of the enties.
            """
            # If the user option is N/A, disable the entries
            if option == HeaderStructureConfig.Values.HEADERSTRUCTURE_OPTIONS[-1]:
                for i in indexes:
                    self.__view.header_entries[i].configure(
                        text_color=HeaderStructureConfig.Colors.DISABLED,
                        fg_color=HeaderStructureConfig.Colors.DISABLED,
                        state="disabled",
                    )
            # If the user option is not N/A, enable the entries
            else:
                for i in indexes:
                    self.__view.header_entries[i].configure(
                        text_color=HeaderStructureConfig.Colors.TEXT,
                        fg_color=HeaderStructureConfig.Colors.NORMAL,
                        state="normal",
                    )

        configure_based_on_option(indexes=[0, 1], option=first_header_option)
        configure_based_on_option(indexes=[2, 3], option=second_header_option)

        return first_header_option, second_header_option

    def __header_option_callback(self, *_: any) -> None:
        """
        Depending on the user inputs, show a specific error message.
        """
        first_header_option, second_header_option = self.__header_entries_callback()

        first_header_postfix = self.__first_header_postfix_var.get()
        second_header_prefix = self.__second_header_prefix_var.get()

        error_message = ""

        if (
            first_header_option
            != HeaderStructureConfig.Values.HEADERSTRUCTURE_OPTIONS[0]
            and second_header_option
            != HeaderStructureConfig.Values.HEADERSTRUCTURE_OPTIONS[0]
        ):
            error_message = f"One category must be {HeaderStructureConfig.Values.HEADERSTRUCTURE_OPTIONS[0]}!"
        elif first_header_option == second_header_option:
            error_message = "The categories cannot be the same!"
        elif (
            first_header_option
            != HeaderStructureConfig.Values.HEADERSTRUCTURE_OPTIONS[-1]
            and second_header_option
            != HeaderStructureConfig.Values.HEADERSTRUCTURE_OPTIONS[-1]
            and first_header_postfix == ""
            and second_header_prefix == ""
        ):
            error_message = f"To be able to differntiate the categories, the {first_header_option} postfix and / or the {second_header_option} prefix must be non-empty!"

        self.__toggle_error_indicator(error_message)

    def __toggle_error_indicator(self, error_message: str) -> None:
        """
        Indicate an error with a specific error message if necessary.

        Args:
            error_text (str): Error message.
        """
        error_text_len = len(error_message)
        if error_text_len == 0:
            self.__view.error_label.grid_forget()
            self.__view.error_box.grid_forget()
        else:
            self.__view.error_box.configure(
                height=30 + ((error_text_len - 1) // 100) * 15
            )

            self.__view.error_box.configure(state="normal")
            self.__view.error_box.delete("0.0", ctk.END)
            self.__view.error_box.insert("0.0", error_message)
            self.__view.error_box.configure(state="disabled")

            self.__view.error_label.grid(
                row=HeaderStructureConfig.Layout.ERROR_ROW,
                column=0,
                sticky="news",
                padx=(25, 0),
                pady=(0, 7),
            )
            self.__view.error_box.grid(
                row=HeaderStructureConfig.Layout.ERROR_ROW,
                column=1,
                columnspan=5,
                sticky="news",
                padx=(30, 30),
                pady=(0, 7),
            )

    def get_header_structure(self) -> dict[str, str | None]:
        """
        Retrieve the header structure settings from the user input.

        Returns:
            dict[str, str | None]: The header structure settings.
        """
        first_header_prefix = self.__first_header_prefix_var.get()
        first_header_option = self.__first_header_option_var.get()
        first_header_postfix = self.__first_header_postfix_var.get()
        second_header_prefix = self.__second_header_prefix_var.get()
        second_header_option = self.__second_header_option_var.get()
        second_header_postfix = self.__second_header_postfix_var.get()

        header_structure_settings = {
            "first_header_prefix": (
                first_header_prefix
                if first_header_prefix != ""
                and first_header_option
                != HeaderStructureConfig.Values.HEADERSTRUCTURE_OPTIONS[-1]
                else None
            ),
            "first_header_option": first_header_option,
            "first_header_postfix": (
                first_header_postfix
                if first_header_postfix != ""
                and first_header_option
                != HeaderStructureConfig.Values.HEADERSTRUCTURE_OPTIONS[-1]
                else None
            ),
            "second_header_prefix": (
                second_header_prefix
                if second_header_prefix != ""
                and second_header_option
                != HeaderStructureConfig.Values.HEADERSTRUCTURE_OPTIONS[-1]
                else None
            ),
            "second_header_option": second_header_option,
            "second_header_postfix": (
                second_header_postfix
                if second_header_postfix != ""
                and second_header_option
                != HeaderStructureConfig.Values.HEADERSTRUCTURE_OPTIONS[-1]
                else None
            ),
        }

        return header_structure_settings
