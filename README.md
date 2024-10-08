# CSVision

 CSVision is a specialized user-friendly tool developed for individuals and professionals who need to analyze and visualize data stored in CSV files. It provides a straightforward solution for turning raw data into clear, interactive visual representations, making it easier to identify trends, patterns, and insights.

 With CSVision, users can load CSV files, export the data to XLSX format and manage and visualize large datasets by selecting specific data columns and displaying them in various chart formats, including line, scatter, bar, and stem charts. The tool is equipped with features that allow for flexible chart configurations and filtering data, making it useful for anyone who works with large amounts of CSV data.

 In addition to its visualization capabilities, CSVision features a search bar for quickly finding specific data columns and offers users a preset function to save  their configurations for future use or load old configurations into the GUI, streamlining the process of data analysis.

![Files](https://tokei.rs/b1/github/SamerKharabish/CSVision?category=files)
![Code](https://tokei.rs/b1/github/SamerKharabish/CSVision?category=code)
![Lines](https://tokei.rs/b1/github/SamerKharabish/CSVision?category=lines)

## Design

![Parameter Input](documentation/design.png)

## Features

- ```Accessibility```: The header frame can be toggled by pressing "Ctrl + B" or the "processor_panel_toggle_button" on the top of the navigation.
- ```Functionality```: CSV files can be selected and loaded with the "open_file_button" in the File Explorer section.
- ```Accessibility```: Once selected CSV files can be reselected and loaded in the "file_entry" in the File Explorer section.
- ```Functionality```: CSV files can be exported to xslx files with the "export_to_excel_button" in the File Explorer section.
- ```Feedback```: Processes are being displayed by a progressbar in the statusbar.
- ```Feedback```: File sizes are being displayed in the statusbar.

## Structure overview

To enhance maintainability, scalability, and testability of the application a Model-View-Controller (MVC) architecture pattern is used, which decouples the business logic from the UI.

```bash
CSVision/
├── configurations/                         # Configuration files.
│ ├── app_config.py                         # Application configuration file.
│ ├── config.py                             # Centralized configuration file.
│ ├── main_config.py                        # Main configuration file.
│ └── statusbar_controller.py               # Statusbar configuration file.
├── controllers/                            # Contains classes that act as intermediaries between
                                            # models and views. They handle user input,
                                            # update models, and reflect changes in views.
│ ├── sidebar_controllers/                  # Contains classes that act as intermediaries
                                            # between models and sidebar views.
│ ├── ├── filehandling_frame_controller.py  # Handles interactions in the file handling frame.
│ ├── ├── header_frame_controller.py        # Handles interactions in the header frame.
│ ├── └── navigation_panel_controller.py    # Handles interactions in the navigation.
│ ├── main_controller.py                    # Handles interactions in the main window.
│ ├── plot_frame_controller.py              # Handles interactions in the plot frame.
│ ├── sidebar_controller.py                 # Handles interactions in the sidebar.
│ └── statusbar_controller.py               # Handles interactions in the statusbar.
├── documentation/                          # Collection of documentations.
│ ├── app_ui.drwaio                         # Application component UI mapping.
│ ├── component_mapping_ui.drwaio           # Project component UI mapping.
│ ├── main_ui.drwaio                        # Main component UI mapping.
│ └── statusbar_ui.drwaio                   # Statusbar component UI mapping.
│ └── UML.drwaio                            # UML class diagram of the project.
├── models/                                 # Contains classes that represent the data
                                            # and business logic of the application.
│ ├── csv_data_manager.py                   # Handles CSV file related operations.
│ └── yaml_manager.py                       # Handles YAML file related operations.
├── resources/                              # Images, yaml files, etc.
│ ├── images/                               # Images.
│ ├── yaml-files/                           # YAML files.
│ ├── ├── file_paths.yaml                   # YAML file to store file paths.
│ ├── └── user_settings.yaml                # YAML file to store user settings.
├── unittests/                              # Automated tests for the application.
│ ├── test_csv_data_manager.py              # Tests the CSV file related operations.
│ └── test_yaml_manager.py                  # Tests the YAML file related operations.
├── utils/                                  # Utility functions and classes.
│ ├── helper_functions.py                   # General helper functions.
│ ├── input_entry_list.py                   # Custom input entry.
│ ├── observer_publisher.py                 # Observer pattern.
│ ├── threads.py                            # Thread classes.
│ └── tristate_button.py                    # Custom tristate button.
├── views/                                  # Contains classes that define the visual
                                            # representation of the application.
│ ├── sidebar_views/                        # Contains classes that define the visual
                                            # representation of the sidebar.
│ ├── ├── config_header_list_frame_view.py  # The visual representation of the configuration
                                            # header list frame.
│ ├── ├── filehandling_frame_view.py        # The visual representation of the file handling.
│ ├── ├── header_frame_view.py              # The visual representation of the header.
│ ├── ├── header_list_frame_view.py         # The visual representation of the header list.
│ ├── ├── navigation_panel_controller.py    # The visual representation of the navigation.
│ ├── ├── preset_frame_view.py              # The visual representation of the preset.
│ ├── └── searchbar_frame_view.py           # The visual representation of the searchbar.
│ ├── configurations_view.py                # The visual representation of all views.
│ ├── main_view.py                          # The visual representation of main window.
│ ├── plot_frame_view.py                    # The visual representation of the plot.
│ ├── sidebar_view.py                       # The visual representation of the sidebar.
│ └── statusbar_view.py                     # The visual representation of the statusbar.
├── .gitignore
├── app.py                                  # Entry point of the application.
├── LICENSE
├── README.md                               # README.
└── requirements.txt                        # Project dependencies.
```

## Feedback

If you have any feedback, please reach out to me.

## Author

- [@Samer Kharabish](<kharabishsamer@outlook.com>)
