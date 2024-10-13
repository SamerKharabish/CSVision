"""FileHandler configuration file."""

from .config import Config


class FileHandlerConfig:
    """
    Contains classes that define the specific configurations of the file handler.
    """

    class OwnArgs:
        """
        Arguments with values of self.
        """

        CORNER_RADIUS: int = Config.Widgets.CORNER_RADIUS
        BORDER_WIDTH: int = Config.Widgets.BORDER_WIDTH
        TRANSPARENT: str = Config.Colors.TRANSPARENT

        FILE_PATHS: str = Config.General.FILE_PATHS
        NR_OF_FILES_TO_SAVE: int = Config.General.NR_OF_FILES_TO_SAVE
        FILE_PATHS_FILE_TYPE: list[tuple[str, str]] = (
            Config.General.FILE_PATHS_FILE_TYPES
        )
        FILE_PATHS_INITIAL_DIR: str = Config.General.FILE_PATHS_INITIAL_DIR

    class Layout:
        """
        Layout.
        """

        FILE_ENTRY: dict[str, str | bool | tuple[int, int]] = {
            "side": "bottom",
            "fill": "x",
            "expand": True,
            "padx": (7, 7),
            "pady": (0, 7),
        }

        TITLE_LABEL: dict[str, str | bool | tuple[int, int]] = {
            "side": "left",
            "fill": "x",
            "expand": False,
            "padx": (10, 0),
            "pady": (1, 0),
        }

        EXPORT_TO_EXCEL_BUTTON: dict[str, str | None | bool | tuple[int, int]] = {
            "side": "right",
            "fill": None,
            "expand": False,
            "padx": (1, 3),
            "pady": (3, 1),
        }

        OPEN_FILE_BUTTON: dict[str, str | None | bool | tuple[int, int]] = {
            "side": "right",
            "fill": None,
            "expand": False,
            "padx": (1, 1),
            "pady": (3, 1),
        }

    class Widgets:
        """
        Arguments with values of each single widget.
        """

        TITLE_LABEL: dict[str, str | int] = {
            "text": "FILE EXPLORER",
            "family": Config.Typography.DEFAULT_FAMILY,
            "size": Config.Typography.NORMAL_SIZE,
            "weight": "bold",
            "anchor": "w",
        }

        OPEN_FILE_BUTTON: dict[str, str | int | tuple[int, int]] = {
            "width": Config.Dimensions.SQUARE_BUTTON_WIDTH_HEIGHT,
            "height": Config.Dimensions.SQUARE_BUTTON_WIDTH_HEIGHT,
            "fg_color": Config.Colors.TRANSPARENT,
            "hover_color": Config.Colors.ONYX_LIGHT,
            "text": "",
            "light_image": "resources/Images/open-file.png",
            "size": (18, 18),
            "anchor": "center",
        }

        EXPORT_TO_EXCEL_BUTTON: dict[str, str | int | tuple[int, int]] = {
            "width": Config.Dimensions.SQUARE_BUTTON_WIDTH_HEIGHT,
            "height": Config.Dimensions.SQUARE_BUTTON_WIDTH_HEIGHT,
            "fg_color": Config.Colors.TRANSPARENT,
            "hover_color": Config.Colors.ONYX_LIGHT,
            "text": "",
            "light_image": "resources/Images/excel.png",
            "size": (18, 18),
            "anchor": "center",
        }

        FILE_ENTRY: dict[str, str | int | tuple[int, int]] = {
            "border_width": 1,
            "fg_color": Config.Colors.ONYX,
            "border_color": Config.Colors.DIM_GRAY,
            "family": Config.Typography.DEFAULT_FAMILY,
            "size": Config.Typography.NORMAL_SIZE,
            "state": "readonly",
            "collection_filepath_yaml": "resources/yaml-files/file_paths.yaml",
        }
