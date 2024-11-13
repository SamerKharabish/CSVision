""" Defines the SettingsWindowView class with the settings toplevel window layout. """

from sys import platform
from PIL import Image
import customtkinter as ctk
from views.configurations_view import SettingsWindowConfig
from views.configurations_view import HeaderStructureFrameConfig


class SettingsWindowView(ctk.CTkToplevel):
    """
    Layout of the settings toplevel window.
    """

    __slots__ = (
        "root",
        "__general_frame",
        "__category_segemented_button",
        "header_structure_frame_view",
        "__manage_settings_frame",
        "ok_button",
        "cancel_button",
        "apply_button",
    )

    def __init__(self, master: ctk.CTk) -> None:
        super().__init__(master)

        self.title(SettingsWindowConfig.General.TITLE)
        self.iconbitmap(SettingsWindowConfig.General.ICON)
        # Because CTkToplevel currently is bugged on windows and doesn't check if a user
        # specified icon is set we need to set the icon again after 200ms
        if platform.startswith("win"):
            self.after(200, lambda: self.iconbitmap(SettingsWindowConfig.General.ICON))

        self.resizable(
            SettingsWindowConfig.Dimensions.RESIZABLE_WIDTH,
            SettingsWindowConfig.Dimensions.RESIZABLE_HEIGHT,
        )

        self.root: ctk.CTk

        self.__initialize_widgets()
        self.__create_layout()

        self.withdraw()

    def __initialize_widgets(self) -> None:
        """
        Initialize widgets.
        """
        self.__general_frame: ctk.CTkScrollableFrame = ctk.CTkScrollableFrame(
            self,
        )

        print(SettingsWindowConfig.Values.CATEGORIES)
        self.__category_segemented_button: ctk.CTkSegmentedButton = (
            ctk.CTkSegmentedButton(
                self,
                corner_radius=SettingsWindowConfig.General.CORNER_RADIUS,
                font=ctk.CTkFont(
                    family=SettingsWindowConfig.Fonts.FONT,
                    size=SettingsWindowConfig.Fonts.FONT_SIZE,
                ),
                values=SettingsWindowConfig.Values.CATEGORIES,
            )
        )
        self.__category_segemented_button.set(SettingsWindowConfig.Values.CATEGORIES[0])

        self.header_structure_frame_view: HeaderStructureFrameView = (
            HeaderStructureFrameView(self.__general_frame)
        )

        self.__manage_settings_frame: ctk.CTkFrame = ctk.CTkFrame(
            self,
            corner_radius=SettingsWindowConfig.General.CORNER_RADIUS,
        )

        self.ok_button: ctk.CTkButton = ctk.CTkButton(
            self.__manage_settings_frame,
            width=SettingsWindowConfig.Dimensions.MANAGE_BUTTON_WIDTH,
            text="OK",
            font=ctk.CTkFont(
                family=SettingsWindowConfig.Fonts.FONT,
                size=SettingsWindowConfig.Fonts.FONT_SIZE,
            ),
        )

        self.cancel_button: ctk.CTkButton = ctk.CTkButton(
            self.__manage_settings_frame,
            width=SettingsWindowConfig.Dimensions.MANAGE_BUTTON_WIDTH,
            text="Cancel",
            font=ctk.CTkFont(
                family=SettingsWindowConfig.Fonts.FONT,
                size=SettingsWindowConfig.Fonts.FONT_SIZE,
            ),
        )
        self.apply_button: ctk.CTkButton = ctk.CTkButton(
            self.__manage_settings_frame,
            width=SettingsWindowConfig.Dimensions.MANAGE_BUTTON_WIDTH,
            text="Apply",
            font=ctk.CTkFont(
                family=SettingsWindowConfig.Fonts.FONT,
                size=SettingsWindowConfig.Fonts.FONT_SIZE,
            ),
        )

    def __create_layout(self) -> None:
        """
        Create layout.
        """
        self.__category_segemented_button.place(
            x=SettingsWindowConfig.Layout.CATEGORY_SEGMENTED_BUTTON_X,
            y=SettingsWindowConfig.Layout.CATEGORY_SEGMENTED_BUTTON_Y,
            anchor=SettingsWindowConfig.Layout.CATEGORY_SEGMENTED_BUTTON_ANCHOR,
        )

        self.__general_frame.pack(
            side=SettingsWindowConfig.Layout.CATEGORY_FRAME_SIDE,
            fill=SettingsWindowConfig.Layout.CATEGORY_FRAME_FILL,
            expand=SettingsWindowConfig.Layout.CATEGORY_FRAME_EXPAND,
            padx=SettingsWindowConfig.Layout.STANDARD_PAD,
            pady=SettingsWindowConfig.Layout.CATEGORY_FRAME_PADY,
        )

        self.header_structure_frame_view.pack(
            side=SettingsWindowConfig.Layout.HEADER_STRUCTURE_FRAME_SIDE,
            fill=SettingsWindowConfig.Layout.HEADER_STRUCTURE_FRAME_FILL,
            expand=SettingsWindowConfig.Layout.HEADER_STRUCTURE_FRAME_EXPAND,
            padx=SettingsWindowConfig.Layout.STANDARD_PAD,
            pady=SettingsWindowConfig.Layout.HEADER_STRUCTURE_FRAME_PADY,
        )

        self.__manage_settings_frame.pack(
            side=SettingsWindowConfig.Layout.MANAGE_SETTINGS_FRAME_SIDE,
            fill=SettingsWindowConfig.Layout.MANAGE_SETTINGS_FRAME_FILL,
            expand=SettingsWindowConfig.Layout.MANAGE_SETTINGS_FRAME_EXPAND,
            padx=SettingsWindowConfig.Layout.STANDARD_PAD,
            pady=SettingsWindowConfig.Layout.MANAGE_SETTINGS_FRAME_PADY,
        )

        self.apply_button.pack(
            side=SettingsWindowConfig.Layout.MANAGE_BUTTON_SIDE,
            fill=SettingsWindowConfig.Layout.MANAGE_BUTTON_FILL,
            expand=SettingsWindowConfig.Layout.MANAGE_BUTTON_EXPAND,
            padx=SettingsWindowConfig.Layout.STANDARD_PAD,
            pady=SettingsWindowConfig.Layout.MANAGE_BUTTON_PADY,
        )
        self.cancel_button.pack(
            side=SettingsWindowConfig.Layout.MANAGE_BUTTON_SIDE,
            fill=SettingsWindowConfig.Layout.MANAGE_BUTTON_FILL,
            expand=SettingsWindowConfig.Layout.MANAGE_BUTTON_EXPAND,
            padx=SettingsWindowConfig.Layout.STANDARD_PAD,
            pady=SettingsWindowConfig.Layout.MANAGE_BUTTON_PADY,
        )
        self.ok_button.pack(
            side=SettingsWindowConfig.Layout.MANAGE_BUTTON_SIDE,
            fill=SettingsWindowConfig.Layout.MANAGE_BUTTON_FILL,
            expand=SettingsWindowConfig.Layout.MANAGE_BUTTON_EXPAND,
            padx=SettingsWindowConfig.Layout.STANDARD_PAD,
            pady=SettingsWindowConfig.Layout.MANAGE_BUTTON_PADY,
        )


class HeaderStructureFrameView(ctk.CTkFrame):
    """
    Layout of the header structure frame.
    """

    __slots__ = (
        "__title",
        "__labels",
        "header_entries",
        "first_header_option",
        "second_header_option",
        "__info_label",
        "__info_box",
        "error_label",
        "error_box",
    )

    def __init__(self, master: ctk.CTkFrame) -> None:
        super().__init__(master, border_width=2)

        self.__initialize_widgets()
        self.__create_layout()

    def __initialize_widgets(self) -> None:
        """
        Initialize widgets.
        """
        self.__title: ctk.CTkSegmentedButton = ctk.CTkSegmentedButton(
            self,
            corner_radius=HeaderStructureFrameConfig.General.CORNER_RADIUS,
            text_color_disabled=HeaderStructureFrameConfig.Colors.TEXT,
            font=ctk.CTkFont(
                family=HeaderStructureFrameConfig.Fonts.FONT,
                size=HeaderStructureFrameConfig.Fonts.FONT_SIZE,
                weight=HeaderStructureFrameConfig.Fonts.FONT_WEIGHT,
            ),
            values=[HeaderStructureFrameConfig.General.TITLE.upper()],
            state="disabled",
        )

        self.grid_rowconfigure((0, 1), weight=1)
        self.grid_rowconfigure((2, 3), weight=3)
        self.grid_columnconfigure(
            (
                HeaderStructureFrameConfig.Layout.FIRST_HEADER_PREFIX_COL,
                HeaderStructureFrameConfig.Layout.FIRST_HEADER_POSTFIX_COL,
                HeaderStructureFrameConfig.Layout.SECOND_HEADER_PREFIX_COL,
                HeaderStructureFrameConfig.Layout.SECOND_HEADER_POSTFIX_COL,
            ),
            weight=HeaderStructureFrameConfig.Layout.COL_WEIGHTS[0],
        )
        self.grid_columnconfigure(
            (
                HeaderStructureFrameConfig.Layout.FIRST_HEADER_OPTION_COL,
                HeaderStructureFrameConfig.Layout.SECOND_HEADER_OPTION_COL,
            ),
            weight=HeaderStructureFrameConfig.Layout.COL_WEIGHTS[1],
        )

        self.__labels: list[ctk.CTkLabel] = []
        for labels in HeaderStructureFrameConfig.Values.HEADER_STRUCTURE_LABELS:
            self.__labels.append(
                ctk.CTkLabel(
                    self,
                    text=labels,
                    font=ctk.CTkFont(
                        family=HeaderStructureFrameConfig.Fonts.FONT,
                        size=HeaderStructureFrameConfig.Fonts.FONT_SIZE,
                    ),
                )
            )

        self.header_entries: list[ctk.CTkEntry] = []
        for _ in range(4):
            self.header_entries.append(
                ctk.CTkEntry(
                    self,
                    width=HeaderStructureFrameConfig.Dimensions.HEADER_STRUCTURE_ENTRIES_WIDTH,
                    font=ctk.CTkFont(
                        family=HeaderStructureFrameConfig.Fonts.FONT,
                        size=HeaderStructureFrameConfig.Fonts.FONT_SIZE,
                    ),
                )
            )

        self.first_header_option: ctk.CTkOptionMenu = ctk.CTkOptionMenu(
            self,
            font=ctk.CTkFont(
                family=HeaderStructureFrameConfig.Fonts.FONT,
                size=HeaderStructureFrameConfig.Fonts.FONT_SIZE,
            ),
            values=HeaderStructureFrameConfig.Values.HEADER_STRUCTURE_OPTIONS,
        )

        self.second_header_option: ctk.CTkOptionMenu = ctk.CTkOptionMenu(
            self,
            font=ctk.CTkFont(
                family=HeaderStructureFrameConfig.Fonts.FONT,
                size=HeaderStructureFrameConfig.Fonts.FONT_SIZE,
            ),
            values=HeaderStructureFrameConfig.Values.HEADER_STRUCTURE_OPTIONS,
        )

        self.__info_label: ctk.CTkLabel = ctk.CTkLabel(
            self,
            text="",
            image=ctk.CTkImage(
                light_image=Image.open(
                    HeaderStructureFrameConfig.ImageFormats.INFO_PNG
                ),
                size=(
                    30,
                    30,
                ),
            ),
        )

        self.__info_box: ctk.CTkTextbox = ctk.CTkTextbox(
            self,
            height=60,
            font=ctk.CTkFont(
                family=HeaderStructureFrameConfig.Fonts.FONT,
                size=HeaderStructureFrameConfig.Fonts.FONT_SIZE - 1,
                weight=HeaderStructureFrameConfig.Fonts.FONT_WEIGHT,
            ),
            activate_scrollbars=False,
        )
        self.__info_box.insert(
            "0.0",
            'PREFIX:\t\tText and / or symbol placed before the "Header" / "Sub-Header".\nCATEGORY:\t\tOption to recognize the text as "Header" or "Sub-Header".\nPOSTFIX:\t\tText and / or symbol placed after the "Header" / "Sub-Header".',
        )

        self.__info_box.configure(state="disabled")

        self.error_label: ctk.CTkLabel = ctk.CTkLabel(
            self,
            text="",
            image=ctk.CTkImage(
                light_image=Image.open(HeaderStructureFrameConfig.ImageFormats.ERROR),
                size=(
                    30,
                    30,
                ),
            ),
        )

        self.error_box: ctk.CTkTextbox = ctk.CTkTextbox(
            self,
            height=45,
            fg_color=HeaderStructureFrameConfig.Colors.ERROR,
            font=ctk.CTkFont(
                family=HeaderStructureFrameConfig.Fonts.FONT,
                size=HeaderStructureFrameConfig.Fonts.FONT_SIZE - 1,
                weight=HeaderStructureFrameConfig.Fonts.FONT_WEIGHT,
            ),
            activate_scrollbars=False,
            wrap="word",
        )

    def __create_layout(self) -> None:
        """
        Create layout.
        """
        self.__title.grid(
            row=HeaderStructureFrameConfig.Layout.TITLE_ROW,
            column=0,
            columnspan=6,
            sticky="news",
            padx=(150, 150),
            pady=(7, 0),
        )

        labels_settings = [
            (HeaderStructureFrameConfig.Layout.FIRST_HEADER_PREFIX_COL, (7, 2)),
            (HeaderStructureFrameConfig.Layout.FIRST_HEADER_OPTION_COL, (2, 2)),
            (HeaderStructureFrameConfig.Layout.FIRST_HEADER_POSTFIX_COL, (2, 2)),
            (HeaderStructureFrameConfig.Layout.SECOND_HEADER_PREFIX_COL, (2, 2)),
            (HeaderStructureFrameConfig.Layout.SECOND_HEADER_OPTION_COL, (2, 2)),
            (HeaderStructureFrameConfig.Layout.SECOND_HEADER_POSTFIX_COL, (2, 7)),
        ]

        for i, (column, padx) in enumerate(labels_settings):
            self.__labels[i].grid(
                row=HeaderStructureFrameConfig.Layout.LABEL_ROW,
                column=column,
                sticky="news",
                padx=padx,
                pady=(0, 0),
            )

        header_entries_settings = [
            (
                HeaderStructureFrameConfig.Layout.FIRST_HEADER_PREFIX_COL,
                self.header_entries[0],
                (7, 2),
            ),
            (
                HeaderStructureFrameConfig.Layout.FIRST_HEADER_OPTION_COL,
                self.first_header_option,
                (2, 2),
            ),
            (
                HeaderStructureFrameConfig.Layout.FIRST_HEADER_POSTFIX_COL,
                self.header_entries[1],
                (2, 2),
            ),
            (
                HeaderStructureFrameConfig.Layout.SECOND_HEADER_PREFIX_COL,
                self.header_entries[2],
                (2, 2),
            ),
            (
                HeaderStructureFrameConfig.Layout.SECOND_HEADER_OPTION_COL,
                self.second_header_option,
                (2, 2),
            ),
            (
                HeaderStructureFrameConfig.Layout.SECOND_HEADER_POSTFIX_COL,
                self.header_entries[3],
                (2, 7),
            ),
        ]

        for column, widget, padx in header_entries_settings:
            widget.grid(
                row=HeaderStructureFrameConfig.Layout.INPUT_ROW,
                column=column,
                sticky="news",
                padx=padx,
                pady=(0, 7),
            )

        self.__info_label.grid(
            row=HeaderStructureFrameConfig.Layout.INFO_ROW,
            column=0,
            sticky="news",
            padx=(25, 0),
            pady=(7, 7),
        )

        self.__info_box.grid(
            row=HeaderStructureFrameConfig.Layout.INFO_ROW,
            column=1,
            columnspan=5,
            sticky="news",
            padx=(30, 30),
            pady=(7, 7),
        )
