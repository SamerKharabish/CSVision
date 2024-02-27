""" Defines the PlotFrameView class with the plot frame layout. """

from PIL import Image
import customtkinter as ctk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from views.configurations_view import Config


class PlotFrameView(ctk.CTkFrame):
    """
    Layout of the plot frame.
    """

    def __init__(self, master: ctk.CTkFrame = None) -> None:
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
        self.plot_frame = ctk.CTkFrame(self, fg_color=Config.Colors.PLOT_FRAME_COLOR)
        self.plot_types_segemented_button = ctk.CTkSegmentedButton(
            self,
            background_corner_colors=(
                self._fg_color,
                self._fg_color,
                Config.Colors.PLOT_FRAME_COLOR,
                Config.Colors.PLOT_FRAME_COLOR,
            ),
            font=Config.Fonts.LABEL_TEXTS,
            values=Config.Values.PLOT_TYPES,
        )
        self.plot_types_segemented_button.set(Config.Values.PLOT_TYPES[0])

        self.nav_toolbar_shell_frame = ctk.CTkFrame(self)
        self.nav_toolbar_frame = ctk.CTkFrame(self.nav_toolbar_shell_frame, fg_color="transparent")
        self.reset_button = ctk.CTkButton(
            self.nav_toolbar_frame,
            width=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
            height=Config.Dimensions.ACTION_BUTTON_WIDTH_HEIGHT,
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

    def create_layout(self) -> None:
        """
        Create layout.
        """
        self.plot_frame.pack(
            side="top", fill="both", expand=True, padx=(10, 10), pady=(20, 5)
        )

        self.plot_types_segemented_button.place(
            anchor="nw",
            x=40,
            y=7,
        )

        self.nav_toolbar_shell_frame.pack(
            side="bottom", fill="x", expand=False, padx=(10, 10), pady=(5, 10)
        )

        self.nav_toolbar_frame.pack(
            side="top", fill="y", expand=False
        )

        self.reset_button.pack(
            side="left",
            expand=False,
            padx=Config.Layout.STANDART_PAD,
            pady=Config.Layout.STANDART_PAD,
        )
        self.back_button.pack(
            side="left",
            expand=False,
            padx=Config.Layout.STANDART_PAD,
            pady=Config.Layout.STANDART_PAD,
        )
        self.forward_button.pack(
            side="left",
            expand=False,
            padx=Config.Layout.STANDART_PAD,
            pady=Config.Layout.STANDART_PAD,
        )
        self.pan_button.pack(
            side="left",
            expand=False,
            padx=Config.Layout.STANDART_PAD,
            pady=Config.Layout.STANDART_PAD,
        )
        self.zoom_button.pack(
            side="left",
            expand=False,
            padx=Config.Layout.STANDART_PAD,
            pady=Config.Layout.STANDART_PAD,
        )
        self.save_button.pack(
            side="left",
            expand=False,
            padx=Config.Layout.STANDART_PAD,
            pady=Config.Layout.STANDART_PAD,
        )

    def initialize_figure(self) -> None:
        """
        Initialize figure.
        """
        self.figure = Figure()  # Create a matplotlib figure
        self.figure.set_facecolor(Config.Colors.PLOT_FRAME_COLOR)
        self.figure.set_tight_layout(True)

        # Embed the Matplotlib figure in the custom frame
        self.canvas = FigureCanvasTkAgg(self.figure, self.plot_frame)
        self.canvas_widget = self.canvas.get_tk_widget()

        self.nav_toolbar = NavigationToolbar2Tk(self.canvas, self, pack_toolbar=False)

    def create_figure_layout(self) -> None:
        """
        Create figure layout.
        """
        self.canvas_widget.pack(
            fill=ctk.BOTH, expand=True, padx=(20, 20), pady=(20, 20)
        )
