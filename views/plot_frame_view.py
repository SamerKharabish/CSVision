""" Defines the PlotFrameView class with the plot frame layout. """

from PIL import Image
import customtkinter as ctk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from views.configurations_view import Config


class PlotFrameView(ctk.CTkFrame):
    """
    Layout of the plot frame.
    """

    def __init__(self, master: ctk.CTkFrame) -> None:
        super().__init__(
            master,
            corner_radius=Config.General.CORNER_RADIUS,
            border_width=Config.General.FRAME_BORDER_WIDTH,
        )

        self.initialize_widgets()
        self.create_layout()
        self.initialize_figure()
        self.create_figure_layout()

    def initialize_widgets(self) -> None:
        """
        Initialize widgets.
        """
        self.plot_area_frame = ctk.CTkFrame(
            self,
            fg_color=Config.Colors.PLOT_FRAME_COLOR,
            border_width=Config.General.FRAME_BORDER_WIDTH,
        )
        self.plot_types_segemented_button = ctk.CTkSegmentedButton(
            self,
            background_corner_colors=(
                self._fg_color,
                self._fg_color,
                Config.Colors.PLOT_FRAME_COLOR,
                Config.Colors.PLOT_FRAME_COLOR,
            ),
            font=ctk.CTkFont(
                family=Config.Fonts.LABEL_TEXTS[0], size=Config.Fonts.LABEL_TEXTS[1]
            ),
            values=Config.Values.PLOT_TYPES,
        )
        self.plot_types_segemented_button.set(Config.Values.PLOT_TYPES[0])

        self.nav_toolbar_frame = ctk.CTkFrame(
            self,
            corner_radius=Config.General.NAV_TOOLBAR_CORNER_RADIUS,
            background_corner_colors=(
                Config.Colors.PLOT_FRAME_COLOR,
                Config.Colors.PLOT_FRAME_COLOR,
                self._fg_color,
                self._fg_color,
            ),
            border_width=Config.General.FRAME_BORDER_WIDTH,
        )

        self.reset_button = ctk.CTkButton(
            self.nav_toolbar_frame,
            width=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            height=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            border_width=Config.General.FRAME_BORDER_WIDTH,
            fg_color=Config.Colors.TRANSPARENT,
            hover_color=Config.Colors.TRANSPARENT_BUTTON_HOVER,
            text="",
            image=ctk.CTkImage(
                light_image=Image.open(Config.ImageFormats.RESET_BUTTON_PNG),
                size=(
                    Config.Dimensions.ACTION_IMAGE_WIDTH_HEIGHT,
                    Config.Dimensions.ACTION_IMAGE_WIDTH_HEIGHT,
                ),
            ),
            anchor=Config.Layout.ACTION_BUTTON_TEXT_ANCHOR,
        )
        self.back_button = ctk.CTkButton(
            self.nav_toolbar_frame,
            width=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            height=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            border_width=Config.General.FRAME_BORDER_WIDTH,
            fg_color=Config.Colors.TRANSPARENT,
            hover_color=Config.Colors.TRANSPARENT_BUTTON_HOVER,
            text="",
            image=ctk.CTkImage(
                light_image=Image.open(Config.ImageFormats.BACK_BUTTON_PNG),
                size=(
                    Config.Dimensions.ACTION_IMAGE_WIDTH_HEIGHT,
                    Config.Dimensions.ACTION_IMAGE_WIDTH_HEIGHT,
                ),
            ),
            anchor=Config.Layout.ACTION_BUTTON_TEXT_ANCHOR,
        )
        self.forward_button = ctk.CTkButton(
            self.nav_toolbar_frame,
            width=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            height=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            border_width=Config.General.FRAME_BORDER_WIDTH,
            fg_color=Config.Colors.TRANSPARENT,
            hover_color=Config.Colors.TRANSPARENT_BUTTON_HOVER,
            text="",
            image=ctk.CTkImage(
                light_image=Image.open(Config.ImageFormats.FORWARD_BUTTON_PNG),
                size=(
                    Config.Dimensions.ACTION_IMAGE_WIDTH_HEIGHT,
                    Config.Dimensions.ACTION_IMAGE_WIDTH_HEIGHT,
                ),
            ),
            anchor=Config.Layout.ACTION_BUTTON_TEXT_ANCHOR,
        )
        self.pan_button = ctk.CTkButton(
            self.nav_toolbar_frame,
            width=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            height=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            border_width=Config.General.FRAME_BORDER_WIDTH,
            fg_color=Config.Colors.TRANSPARENT,
            hover_color=Config.Colors.TRANSPARENT_BUTTON_HOVER,
            text="",
            image=ctk.CTkImage(
                light_image=Image.open(Config.ImageFormats.PAN_BUTTON_PNG),
                size=(
                    Config.Dimensions.ACTION_IMAGE_WIDTH_HEIGHT,
                    Config.Dimensions.ACTION_IMAGE_WIDTH_HEIGHT,
                ),
            ),
            anchor=Config.Layout.ACTION_BUTTON_TEXT_ANCHOR,
        )
        self.zoom_button = ctk.CTkButton(
            self.nav_toolbar_frame,
            width=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            height=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            border_width=Config.General.FRAME_BORDER_WIDTH,
            fg_color=Config.Colors.TRANSPARENT,
            hover_color=Config.Colors.TRANSPARENT_BUTTON_HOVER,
            text="",
            image=ctk.CTkImage(
                light_image=Image.open(Config.ImageFormats.ZOOM_BUTTON_PNG),
                size=(
                    Config.Dimensions.ACTION_IMAGE_WIDTH_HEIGHT,
                    Config.Dimensions.ACTION_IMAGE_WIDTH_HEIGHT,
                ),
            ),
            anchor=Config.Layout.ACTION_BUTTON_TEXT_ANCHOR,
        )
        self.save_button = ctk.CTkButton(
            self.nav_toolbar_frame,
            width=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            height=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            border_width=Config.General.FRAME_BORDER_WIDTH,
            fg_color=Config.Colors.TRANSPARENT,
            hover_color=Config.Colors.TRANSPARENT_BUTTON_HOVER,
            text="",
            image=ctk.CTkImage(
                light_image=Image.open(Config.ImageFormats.SAVE_BUTTON_PNG),
                size=(
                    Config.Dimensions.ACTION_IMAGE_WIDTH_HEIGHT,
                    Config.Dimensions.ACTION_IMAGE_WIDTH_HEIGHT,
                ),
            ),
            anchor=Config.Layout.ACTION_BUTTON_TEXT_ANCHOR,
        )
        self.legend_button = ctk.CTkButton(
            self.nav_toolbar_frame,
            width=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            height=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            border_width=Config.General.FRAME_BORDER_WIDTH,
            fg_color=Config.Colors.TRANSPARENT,
            hover_color=Config.Colors.TRANSPARENT_BUTTON_HOVER,
            text="",
            image=ctk.CTkImage(
                light_image=Image.open(Config.ImageFormats.LEGEND_BUTTON_PNG),
                size=(
                    Config.Dimensions.ACTION_IMAGE_WIDTH_HEIGHT,
                    Config.Dimensions.ACTION_IMAGE_WIDTH_HEIGHT,
                ),
            ),
            anchor=Config.Layout.ACTION_BUTTON_TEXT_ANCHOR,
        )

    def create_layout(self) -> None:
        """
        Create layout.
        """
        self.plot_area_frame.pack(
            side=Config.Layout.PLOT_FRAME_PLOT_AREA_FRAME_SIDE,
            fill=Config.Layout.PLOT_FRAME_PLOT_AREA_FRAME_FILL,
            expand=Config.Layout.PLOT_FRAME_PLOT_AREA_FRAME_EXPAND,
            padx=Config.Layout.STANDART_PAD,
            pady=Config.Layout.PLOT_FRAME_PLOT_AREA_FRAME_PADY,
        )

        self.plot_types_segemented_button.place(
            x=Config.Layout.PLOT_FRAME_SEGMENTED_BUTTON_X,
            y=Config.Layout.PLOT_FRAME_SEGMENTED_BUTTON_Y,
            anchor=Config.Layout.PLOT_FRAME_SEGMENTED_BUTTON_ANCHOR,
        )

        self.nav_toolbar_frame.place(
            relx=Config.Layout.PLOT_FRAME_NAV_TOOLBAR_FRAME_RELX,
            rely=Config.Layout.PLOT_FRAME_NAV_TOOLBAR_FRAME_RELY,
            x=Config.Layout.PLOT_FRAME_NAV_TOOLBAR_FRAME_X,
            y=Config.Layout.PLOT_FRAME_NAV_TOOLBAR_FRAME_Y,
            anchor=Config.Layout.PLOT_FRAME_NAV_TOOLBAR_FRAME_ANCHOR,
        )

        self.reset_button.pack(
            side=Config.Layout.NAV_TOOLBAR_BUTTONS_SIDE,
            expand=Config.Layout.NAV_TOOLBAR_BUTTONS_EXPAND,
            padx=Config.Layout.NAV_TOOLBAR_LEFT_BUTTONS_PADX,
            pady=Config.Layout.STANDART_PAD,
        )
        self.back_button.pack(
            side=Config.Layout.NAV_TOOLBAR_BUTTONS_SIDE,
            expand=Config.Layout.NAV_TOOLBAR_BUTTONS_EXPAND,
            padx=Config.Layout.STANDART_PAD,
            pady=Config.Layout.STANDART_PAD,
        )
        self.forward_button.pack(
            side=Config.Layout.NAV_TOOLBAR_BUTTONS_SIDE,
            expand=Config.Layout.NAV_TOOLBAR_BUTTONS_EXPAND,
            padx=Config.Layout.STANDART_PAD,
            pady=Config.Layout.STANDART_PAD,
        )
        self.pan_button.pack(
            side=Config.Layout.NAV_TOOLBAR_BUTTONS_SIDE,
            expand=Config.Layout.NAV_TOOLBAR_BUTTONS_EXPAND,
            padx=Config.Layout.STANDART_PAD,
            pady=Config.Layout.STANDART_PAD,
        )
        self.zoom_button.pack(
            side=Config.Layout.NAV_TOOLBAR_BUTTONS_SIDE,
            expand=Config.Layout.NAV_TOOLBAR_BUTTONS_EXPAND,
            padx=Config.Layout.STANDART_PAD,
            pady=Config.Layout.STANDART_PAD,
        )
        self.save_button.pack(
            side=Config.Layout.NAV_TOOLBAR_BUTTONS_SIDE,
            expand=Config.Layout.NAV_TOOLBAR_BUTTONS_EXPAND,
            padx=Config.Layout.STANDART_PAD,
            pady=Config.Layout.STANDART_PAD,
        )
        self.legend_button.pack(
            side=Config.Layout.NAV_TOOLBAR_BUTTONS_SIDE,
            expand=Config.Layout.NAV_TOOLBAR_BUTTONS_EXPAND,
            padx=Config.Layout.NAV_TOOLBAR_RIGHT_BUTTONS_PADX,
            pady=Config.Layout.STANDART_PAD,
        )

    def initialize_figure(self) -> None:
        """
        Initialize figure.
        """
        self.figure = Figure()  # Create a matplotlib figure
        self.figure.set_facecolor(Config.Colors.PLOT_FRAME_COLOR)
        # self.figure.set_tight_layout(True)
        self.figure.tight_layout()

        # Embed the Matplotlib figure in the custom frame
        self.canvas = FigureCanvasTkAgg(self.figure, self.plot_area_frame)
        self.canvas_widget = self.canvas.get_tk_widget()

        self.nav_toolbar = NavigationToolbar2Tk(self.canvas, self, pack_toolbar=False)

    def create_figure_layout(self) -> None:
        """
        Create figure layout.
        """
        self.canvas_widget.pack(
            side=Config.Layout.CANVAS_SIDE,
            fill=Config.Layout.CANVAS_FILL,
            expand=Config.Layout.CANVAS_EXPAND,
            padx=Config.Layout.CANVAS_PADY,
            pady=Config.Layout.STANDART_PAD,
        )
