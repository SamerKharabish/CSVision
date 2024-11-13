""" Defines the PlotFrameView class with the plot frame layout. """

from __future__ import annotations
from typing import TYPE_CHECKING
from tkinter import Canvas
from PIL import Image
import customtkinter as ctk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from .configurations_view import Config

if TYPE_CHECKING:
    from .main_view import MainView


class PlotView(ctk.CTkFrame):
    """
    Layout of the plot frame.
    """

    def __init__(self, master: MainView) -> None:
        super().__init__(
            master,
            corner_radius=Config.General.CORNER_RADIUS,
            border_width=Config.General.FRAME_BORDER_WIDTH,
        )

        self.__initialize_widgets()
        self.__create_layout()
        self.__initialize_figure()
        self.__create_figure_layout()

    def __initialize_widgets(self) -> None:
        """
        Initialize widgets.
        """
        self.__plot_area_frame: ctk.CTkFrame = ctk.CTkFrame(
            self,
            fg_color=Config.Colors.ONYX_LIGHT,
            border_width=Config.General.FRAME_BORDER_WIDTH,
        )
        self.__plot_types_segemented_button: ctk.CTkSegmentedButton = (
            ctk.CTkSegmentedButton(
                self,
                background_corner_colors=(
                    self._fg_color,
                    self._fg_color,
                    Config.Colors.ONYX_LIGHT,
                    Config.Colors.ONYX_LIGHT,
                ),
                font=ctk.CTkFont(
                    family=Config.Fonts.FONT_SIZE_WEIGHT[0],
                    size=Config.Fonts.FONT_SIZE_WEIGHT[1],
                ),
                values=Config.Values.PLOT_TYPES,
            )
        )
        self.__plot_types_segemented_button.set(Config.Values.PLOT_TYPES[0])

        self.__nav_toolbar_frame: ctk.CTkFrame = ctk.CTkFrame(
            self,
            corner_radius=Config.General.NAV_TOOLBAR_CORNER_RADIUS,
            background_corner_colors=(
                Config.Colors.ONYX_LIGHT,
                Config.Colors.ONYX_LIGHT,
                self._fg_color,
                self._fg_color,
            ),
            border_width=Config.General.FRAME_BORDER_WIDTH,
        )

        self.__reset_button: ctk.CTkButton = ctk.CTkButton(
            self.__nav_toolbar_frame,
            width=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            height=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            border_width=Config.General.FRAME_BORDER_WIDTH,
            fg_color=Config.Colors.TRANSPARENT,
            hover_color=Config.Colors.ONYX_LIGHT,
            text="",
            image=ctk.CTkImage(
                light_image=Image.open(Config.ImageFormats.RESET_PNG),
                size=(
                    Config.Dimensions.ACTION_IMAGE_WIDTH_HEIGHT,
                    Config.Dimensions.ACTION_IMAGE_WIDTH_HEIGHT,
                ),
            ),
            anchor=Config.Layout.ACTION_BUTTON_TEXT_ANCHOR,
        )
        self.__back_button: ctk.CTkButton = ctk.CTkButton(
            self.__nav_toolbar_frame,
            width=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            height=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            border_width=Config.General.FRAME_BORDER_WIDTH,
            fg_color=Config.Colors.TRANSPARENT,
            hover_color=Config.Colors.ONYX_LIGHT,
            text="",
            image=ctk.CTkImage(
                light_image=Image.open(Config.ImageFormats.BACK_PNG),
                size=(
                    Config.Dimensions.ACTION_IMAGE_WIDTH_HEIGHT,
                    Config.Dimensions.ACTION_IMAGE_WIDTH_HEIGHT,
                ),
            ),
            anchor=Config.Layout.ACTION_BUTTON_TEXT_ANCHOR,
        )
        self.__forward_button: ctk.CTkButton = ctk.CTkButton(
            self.__nav_toolbar_frame,
            width=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            height=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            border_width=Config.General.FRAME_BORDER_WIDTH,
            fg_color=Config.Colors.TRANSPARENT,
            hover_color=Config.Colors.ONYX_LIGHT,
            text="",
            image=ctk.CTkImage(
                light_image=Image.open(Config.ImageFormats.FORWARD_PNG),
                size=(
                    Config.Dimensions.ACTION_IMAGE_WIDTH_HEIGHT,
                    Config.Dimensions.ACTION_IMAGE_WIDTH_HEIGHT,
                ),
            ),
            anchor=Config.Layout.ACTION_BUTTON_TEXT_ANCHOR,
        )
        self.__pan_button: ctk.CTkButton = ctk.CTkButton(
            self.__nav_toolbar_frame,
            width=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            height=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            border_width=Config.General.FRAME_BORDER_WIDTH,
            fg_color=Config.Colors.TRANSPARENT,
            hover_color=Config.Colors.ONYX_LIGHT,
            text="",
            image=ctk.CTkImage(
                light_image=Image.open(Config.ImageFormats.PAN_PNG),
                size=(
                    Config.Dimensions.ACTION_IMAGE_WIDTH_HEIGHT,
                    Config.Dimensions.ACTION_IMAGE_WIDTH_HEIGHT,
                ),
            ),
            anchor=Config.Layout.ACTION_BUTTON_TEXT_ANCHOR,
        )
        self.__zoom_button: ctk.CTkButton = ctk.CTkButton(
            self.__nav_toolbar_frame,
            width=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            height=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            border_width=Config.General.FRAME_BORDER_WIDTH,
            fg_color=Config.Colors.TRANSPARENT,
            hover_color=Config.Colors.ONYX_LIGHT,
            text="",
            image=ctk.CTkImage(
                light_image=Image.open(Config.ImageFormats.ZOOM_PNG),
                size=(
                    Config.Dimensions.ACTION_IMAGE_WIDTH_HEIGHT,
                    Config.Dimensions.ACTION_IMAGE_WIDTH_HEIGHT,
                ),
            ),
            anchor=Config.Layout.ACTION_BUTTON_TEXT_ANCHOR,
        )
        self.__save_button: ctk.CTkButton = ctk.CTkButton(
            self.__nav_toolbar_frame,
            width=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            height=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            border_width=Config.General.FRAME_BORDER_WIDTH,
            fg_color=Config.Colors.TRANSPARENT,
            hover_color=Config.Colors.ONYX_LIGHT,
            text="",
            image=ctk.CTkImage(
                light_image=Image.open(Config.ImageFormats.SAVE_PNG),
                size=(
                    Config.Dimensions.ACTION_IMAGE_WIDTH_HEIGHT,
                    Config.Dimensions.ACTION_IMAGE_WIDTH_HEIGHT,
                ),
            ),
            anchor=Config.Layout.ACTION_BUTTON_TEXT_ANCHOR,
        )
        self.__legend_button: ctk.CTkButton = ctk.CTkButton(
            self.__nav_toolbar_frame,
            width=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            height=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            border_width=Config.General.FRAME_BORDER_WIDTH,
            fg_color=Config.Colors.TRANSPARENT,
            hover_color=Config.Colors.ONYX_LIGHT,
            text="",
            image=ctk.CTkImage(
                light_image=Image.open(Config.ImageFormats.LEGEND_PNG),
                size=(
                    Config.Dimensions.ACTION_IMAGE_WIDTH_HEIGHT,
                    Config.Dimensions.ACTION_IMAGE_WIDTH_HEIGHT,
                ),
            ),
            anchor=Config.Layout.ACTION_BUTTON_TEXT_ANCHOR,
        )

    def __create_layout(self) -> None:
        """
        Create layout.
        """
        self.__plot_area_frame.pack(
            side=Config.Layout.PLOT_FRAME_PLOT_AREA_FRAME_SIDE,
            fill=Config.Layout.PLOT_FRAME_PLOT_AREA_FRAME_FILL,
            expand=Config.Layout.PLOT_FRAME_PLOT_AREA_FRAME_EXPAND,
            padx=Config.Layout.STANDARD_PAD,
            pady=Config.Layout.PLOT_FRAME_PLOT_AREA_FRAME_PADY,
        )

        self.__plot_types_segemented_button.place(
            x=Config.Layout.PLOT_FRAME_SEGMENTED_BUTTON_X,
            y=Config.Layout.PLOT_FRAME_SEGMENTED_BUTTON_Y,
            anchor=Config.Layout.PLOT_FRAME_SEGMENTED_BUTTON_ANCHOR,
        )

        self.__nav_toolbar_frame.place(
            relx=Config.Layout.PLOT_FRAME_NAV_TOOLBAR_FRAME_RELX,
            rely=Config.Layout.PLOT_FRAME_NAV_TOOLBAR_FRAME_RELY,
            x=Config.Layout.PLOT_FRAME_NAV_TOOLBAR_FRAME_X,
            y=Config.Layout.PLOT_FRAME_NAV_TOOLBAR_FRAME_Y,
            anchor=Config.Layout.PLOT_FRAME_NAV_TOOLBAR_FRAME_ANCHOR,
        )

        self.__reset_button.pack(
            side=Config.Layout.NAV_TOOLBAR_BUTTONS_SIDE,
            expand=Config.Layout.NAV_TOOLBAR_BUTTONS_EXPAND,
            padx=Config.Layout.NAV_TOOLBAR_LEFT_BUTTONS_PADX,
            pady=Config.Layout.STANDARD_PAD,
        )
        self.__back_button.pack(
            side=Config.Layout.NAV_TOOLBAR_BUTTONS_SIDE,
            expand=Config.Layout.NAV_TOOLBAR_BUTTONS_EXPAND,
            padx=Config.Layout.STANDARD_PAD,
            pady=Config.Layout.STANDARD_PAD,
        )
        self.__forward_button.pack(
            side=Config.Layout.NAV_TOOLBAR_BUTTONS_SIDE,
            expand=Config.Layout.NAV_TOOLBAR_BUTTONS_EXPAND,
            padx=Config.Layout.STANDARD_PAD,
            pady=Config.Layout.STANDARD_PAD,
        )
        self.__pan_button.pack(
            side=Config.Layout.NAV_TOOLBAR_BUTTONS_SIDE,
            expand=Config.Layout.NAV_TOOLBAR_BUTTONS_EXPAND,
            padx=Config.Layout.STANDARD_PAD,
            pady=Config.Layout.STANDARD_PAD,
        )
        self.__zoom_button.pack(
            side=Config.Layout.NAV_TOOLBAR_BUTTONS_SIDE,
            expand=Config.Layout.NAV_TOOLBAR_BUTTONS_EXPAND,
            padx=Config.Layout.STANDARD_PAD,
            pady=Config.Layout.STANDARD_PAD,
        )
        self.__save_button.pack(
            side=Config.Layout.NAV_TOOLBAR_BUTTONS_SIDE,
            expand=Config.Layout.NAV_TOOLBAR_BUTTONS_EXPAND,
            padx=Config.Layout.STANDARD_PAD,
            pady=Config.Layout.STANDARD_PAD,
        )
        self.__legend_button.pack(
            side=Config.Layout.NAV_TOOLBAR_BUTTONS_SIDE,
            expand=Config.Layout.NAV_TOOLBAR_BUTTONS_EXPAND,
            padx=Config.Layout.NAV_TOOLBAR_RIGHT_BUTTONS_PADX,
            pady=Config.Layout.STANDARD_PAD,
        )

    def __initialize_figure(self) -> None:
        """
        Initialize figure.
        """
        self.__figure: Figure = Figure()  # Create a matplotlib figure
        self.__figure.set_facecolor(Config.Colors.ONYX_LIGHT)
        # self.figure.set_tight_layout(True)
        self.__figure.tight_layout()

        # Embed the Matplotlib figure in the custom frame
        self.__canvas: FigureCanvasTkAgg = FigureCanvasTkAgg(
            self.__figure, self.__plot_area_frame
        )
        self.__canvas_widget: Canvas = self.__canvas.get_tk_widget()

        self.__nav_toolbar: NavigationToolbar2Tk = NavigationToolbar2Tk(
            self.__canvas, self, pack_toolbar=False
        )

    def __create_figure_layout(self) -> None:
        """
        Create figure layout.
        """
        self.__canvas_widget.pack(
            side=Config.Layout.CANVAS_SIDE,
            fill=Config.Layout.CANVAS_FILL,
            expand=Config.Layout.CANVAS_EXPAND,
            padx=Config.Layout.CANVAS_PADY,
            pady=Config.Layout.STANDARD_PAD,
        )
